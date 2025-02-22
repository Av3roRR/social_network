from celery import Celery
from app.config import settings

celery = Celery(
    "tasks",
    broker=settings.BROKER,
    include=["app.tasks.tasks"],
    backend=settings.BACKEND
)
celery.conf.update(
    smtp_server=settings.SMTP_SERVER,
    smtp_port=settings.SMTP_PORT,
    smtp_username=settings.SMTP_USERNAME,
    smtp_password=settings.SMTP_PASSWORD,
    email_from=settings.EMAIL_FROM)