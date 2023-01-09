from flask import Flask
from celery import Celery
from config import Config


celery = Celery(
    __name__, broker=Config.CELERY_BROKER_URL, result_backend=Config.RESULT_BACKEND
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config())
    celery.conf.update(app.config)

    register_blueprints(app)
    register_error_handlers(app)

    return app


def register_blueprints(app):
    from routes import bp

    app.register_blueprint(bp)


def register_error_handlers(app):
    from routes import handle_exception

    app.register_error_handler(Exception, handle_exception)
