import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    # db_fd, app.app.config["DATABASE"] = tempfile.mkstemp()
    app.config["TESTING"] = True

    with app.test_client() as client:
        # with app.app.app_context():
        #     app.init_db()
        yield client

    # os.close(db_fd)
    # os.unlink(app.app.config["DATABASE"])


def test_client(client):
    rv = client.get("/")
    assert rv
