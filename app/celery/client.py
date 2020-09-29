from celery import Celery
from datetime import timedelta
from celery.schedules import crontab
from app.modules.pubmed_crawler.pubmed_crawler import PubMedCrawler
from app.modules.models.training_script import fine_tuning_preprocess



app = Celery("tasks", broker = "redis://localhost:6379")

app.conf.beat_schedule = {
    "pubmed_crawler": {
        "task": "task.pubmed_crawler",
        "schedule": crontab(hour=23, minute=58),
    },
}
app.conf.timezone = 'UTC'


@app.task
def pubmed_crawler():
    print("yes")
    dataframe = "pubmed.csv"
    filepath = "data/train_datasource/pubmed.csv"
    crawler = PubMedCrawler(dataframe)
    crawler.crawl()
    fine_tuning_preprocess(filepath)