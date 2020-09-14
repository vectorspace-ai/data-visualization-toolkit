CELERY_IMPORTS = ("app.celery.task")
CELERY_IGNORE_RESULT = False
BROKER_URL = "redis://"
BROKER_HOST = "localhost"
BROKER_PORT = 6379

from datetime import timedelta
from celery.schedules import crontab

beat_schedule = {
    "pubmed_crawler": {
        "task": "task.pubmed_crawler",
        "schedule": crontab(hour=23, minute=59),
    },
}
