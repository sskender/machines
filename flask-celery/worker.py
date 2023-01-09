from app import celery
from app import create_app

app = create_app()
app.app_context().push()
