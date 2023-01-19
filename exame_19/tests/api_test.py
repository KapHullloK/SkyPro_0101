from app import app
from pytest import fixture


@fixture
def client():
    return app.test_client()


def test_api_posts(client):
    retur = client.get("/api/trains")
    assert retur.status_code == 200
    assert type(retur.json) == list
    assert len(retur.json) > 0


def test_api_inform(client):
    retur = client.get(f"/api/train/{5}")
    assert retur.status_code == 200
    assert type(retur.json) == dict
    assert len(retur.json) > 0
