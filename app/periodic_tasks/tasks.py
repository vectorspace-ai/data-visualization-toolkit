from app.periodic_tasks.celery import app
from app.modules.pubmed_crawler.pubmed_crawler import PubMedCrawler
from app.modules.models.training_script import fine_tuning_preprocess

@app.task
def pubmed_crawler():
    dataframe = "pubmed.csv"
    filepath = f"data/train_datasource/{dataframe}"
    crawler = PubMedCrawler(dataframe)
    crawler.crawl()
    fine_tuning_preprocess(filepath)