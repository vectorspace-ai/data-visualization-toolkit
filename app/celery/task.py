from celery.task import task
from app.modules.pubmed_crawler.pubmed_crawler import PubMedCrawler


@task
def pubmed_crawler():
    crawler = PubMedCrawler("data/train_datasource/pubmed_data.csv")
    crawler.crawl()
