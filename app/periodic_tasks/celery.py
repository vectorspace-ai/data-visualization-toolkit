from celery import Celery
from celery.schedules import crontab

app = Celery('app.periodic_tasks',
             include=['app.periodic_tasks.tasks'])
app.config_from_object('app.periodic_tasks.celeryconfig')
app.conf.beat_schedule = {
    'pubmed-crawler': {
        'task': 'app.periodic_tasks.tasks.pubmed_crawler',
        'schedule': crontab(hour=23, minute=59)
    }
}
