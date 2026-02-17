import os

import pytest
from dotenv import load_dotenv

from utils.api_client import APIClient

load_dotenv()


@pytest.fixture(scope="session")
def api_client():

    client = APIClient(base_url=os.getenv("BASE_URL"))

    yield client

    client.close()


@pytest.fixture
def create_test_user(api_client):

    def _create_user(name: str = "Test User", job: str = "Test Job"):
        payload = {"name": name, "job": job}
        response = api_client.post("/users", data=payload)
        return response

    return _create_user
