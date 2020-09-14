from celery.task import task
from app.modules.pubmed_crawler.pubmed_crawler import PubMedCrawler
from app.modules.models.training_script import fine_tuning_preprocess


@task
def pubmed_crawler():
    filepath = "data/train_datasource/pubmed_data.csv"
    crawler = PubMedCrawler(filepath)
    crawler.crawl()
    fine_tuning_preprocess(filepath)

