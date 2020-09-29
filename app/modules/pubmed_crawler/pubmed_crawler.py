import time
from os import path
import pandas as pd
import urllib.request, json
from app.modules.pubmed_crawler.time_string import stime
from datetime import datetime


HTTP_ERROR = "HTTP Error 404"

AUTHOR_INFO = "Author information"
DOI = "DOI"
COPYRIGHT = "©"
AT = "@"
EMAIL = "e-mail"
PMID_TAG = "PMID"
PMCID = "PMCID"

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


class PubMedCrawler:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.path = "data/train_datasource"
        self.dataframe_path = path.join(self.path, self.dataframe)
        self.columns = ["name", "text"]


        if not path.isfile(self.dataframe_path):
            with open(self.dataframe_path, 'w') as w:
                w.write(", ".join(self.columns))
        
        self.crawled_pmids = None
        self.today = datetime.now()
        self.url_string_today = None
        self.url_string_startdate = self.today.strftime("%Y%%2F%m%%2F%d")
        self.url_articles = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id="


    def crawl(self):
        self.df = pd.read_csv(self.dataframe_path)
        self.crawled_pmids = list(self.df["name"].astype(str))
        df_today = pd.DataFrame(columns=self.columns)
        dataframe_today_path=path.join(self.path, datetime.today().strftime('%Y-%m-%d')+"_"+self.dataframe)
        with open(dataframe_today_path, 'w') as w:
            w.write(", ".join(self.columns))


        url_string_today = self.today.strftime("%Y%%2F%m%%2F%d")
        url_pmids = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=("' + self.url_string_startdate + '"%5BDate%20-%20Publication%5D%20%3A%20"' + url_string_today + '"%5BDate%20-%20Publication%5D)&retmode=json&retmax=1000000'


        print("["+stime()+"]: Getting newly published articles...")
        response = urllib.request.urlopen(url_pmids)
        data = json.loads(response.read())
        pmid_list = [i for i in data["esearchresult"]["idlist"] if i not in self.crawled_pmids]
        if len(pmid_list) is not 0:
            start = time.time()
            print("["+stime()+"]: New articles published: ", len(pmid_list))
            print("Starting crawl in 5 seconds...")
            time.sleep(5)
            for pmid in pmid_list:
                try:
                    response = urllib.request.urlopen(self.url_articles + pmid)
                except (KeyboardInterrupt, SystemExit):
                    raise
                except urllib.error.HTTPError:
                    print(HTTP_ERROR, file=sys.stderr)

                article = str(response.read().decode("utf-8"))
                article = article.split('\n\n')
                if len(article) > 5:

                    abstract = "\n".join([i for i in article[3:] if
                                          AUTHOR_INFO not in i and DOI not in i and COPYRIGHT not in i and AT not in i and EMAIL not in i and PMID_TAG not in i and PMCID not in i])
                    if len(abstract) is not 0:
                        self.crawled_pmids.append(pmid)
                        df = pd.DataFrame([[pmid, abstract]], columns=self.columns)
                        df.to_csv(dataframe_today_path, mode='a', index=False, header=False)
                        df_today = df_today.append({"name": pmid, "text": abstract}, ignore_index=True)
                        print("["+stime()+"]: Crawled abstact: ", pmid)
                        print("Length: ", len(abstract))
            self.df = pd.concat([self.df, df_today], ignore_index=True)
            self.df.to_csv(self.dataframe_path, index=False)
            print("Crawling finished.")
            print("Elapsed time: ", round(time.time() - start, 4))

        else:
            print("["+stime()+"]: No new articles published")
