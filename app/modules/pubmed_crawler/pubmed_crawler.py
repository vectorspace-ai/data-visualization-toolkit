import time
import pandas as pd
import urllib.request, json
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
        self.df = pd.read_csv(self.dataframe)
        self.today = datetime.now()
        self.url_string_today = None
        self.url_string_startdate = self.today.strftime("%Y%%2F%m%%2F%d")
        self.crawled_pmids = list(self.df["name"].astype(str))
        self.url_articles = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id="

    # self.test_pmid=["32867002","32867001","32867000"]
    def crawl(self):
        url_string_today = self.today.strftime("%Y%%2F%m%%2F%d")
        url_pmids = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=("' + self.url_string_startdate + '"%5BDate%20-%20Publication%5D%20%3A%20"' + url_string_today + '"%5BDate%20-%20Publication%5D)&retmode=json&retmax=1000000'
        print("Getting newly published articles...")
        response = urllib.request.urlopen(url_pmids)
        data = json.loads(response.read())
        pmid_list = [i for i in data["esearchresult"]["idlist"] if i not in self.crawled_pmids]
        if len(pmid_list) is not 0:
            start = time.time()
            print("New articles published: ", len(pmid_list))
            print("Starting crawl in 5 seconds...")
            time.sleep(5)
            for pmid in pmid_list:
                print("Parsing PubMed article: ", pmid)
                try:
                    response = urllib.request.urlopen(self.url_articles + pmid)
                except:
                    print(HTTP_ERROR)
                article = str(response.read().decode("utf-8"))
                article = article.split('\n\n')
                if len(article) > 5:

                    abstract = "\n".join([i for i in article[3:] if
                                          AUTHOR_INFO not in i and DOI not in i and COPYRIGHT not in i and AT not in i and EMAIL not in i and PMID_TAG not in i and PMCID not in i])
                    if len(abstract) is not 0:
                        print("Abstract length: ", len(abstract))
                        print(abstract)
                        self.crawled_pmids.append(pmid)
                        df = pd.DataFrame([[pmid, abstract]], columns=["name", "text"])
                        df.to_csv(self.dataframe, mode='a', index=False, header=False)
            print("Crawling finished.")
            print("Elapsed time: ", round(time.time() - start, 4))


        else:
            print("No new articles published")
