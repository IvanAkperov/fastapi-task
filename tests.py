import pytest
from fastapi.testclient import TestClient
from main import app, fetch_user_data


@pytest.fixture
def client():
    return TestClient(app)


@pytest.mark.asyncio
async def test_fetch_user_data():
    user_data = await fetch_user_data(1)
    assert 'id' in user_data
    assert 'name' in user_data
    assert 'email' in user_data


def test_get_user(client):
    response = client.get("/user/1")
    assert response.status_code == 200
    user_data = response.json()
    assert 'id' in user_data
    assert 'name' in user_data
    assert 'email' in user_data
