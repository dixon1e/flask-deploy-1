from app import create_app

app = create+app()
app.app_context().push()

from tasks import celery
