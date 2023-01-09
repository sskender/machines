import time
from app import celery
from flask import current_app


@celery.task(name="heavy_math_task")
def heavy_math_task(n):
    app = current_app._get_current_object()
    app.logger.info(f"New task received: n = {n}")
    time.sleep(5)
    r = n**2
    app.logger.info(f"Task finished: n = {n} r = {r}")
