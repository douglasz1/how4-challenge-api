from .app import app
from .models import database

@app.before_request
def _db_connect():
    if database.is_closed():
        database.connect()
#those credentials from each transformations will be build into here
@app.teardown_request
def _db_close(exc):
    if not database.is_closed():
        database.close()