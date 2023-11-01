import os
import tempfile
from behave import fixture, use_fixture

## Via: https://behave.readthedocs.io/en/stable/usecase_flask.html

from app import app, init_db

fixture
def flaskr_client(context, *args, **kwargs):
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    app.testing = True

    context.client = app.test_client()
    with app.app_context():
        init_db()
    yield context.client

    # -- CLEANUP:
    os.close(context.db)
    os.unlink(app.config['DATABASE'])

def before_feature(context, feature):
    # -- HINT: Recreate a new app client before each feature is executed.
    use_fixture(flaskr_client, context)

def after_feature(context, feature):
    pass

