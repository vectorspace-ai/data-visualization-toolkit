from celery import Celery

celery = Celery()
celery.config_from_object("app.celery.celeryconfig")