from api.api import app
from fastapi.testclient import TestClient

from testing_output import LIST_API_OUTPUT

client = TestClient(app)

def test_create_carousel():
    response = client.get("/carousel/list")
    assert response.status_code == 200
    assert response.json() == LIST_API_OUTPUT