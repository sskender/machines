import os


class Config:
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    RESULT_BACKEND = os.getenv("RESULT_BACKEND", "redis://localhost:6379/0")
