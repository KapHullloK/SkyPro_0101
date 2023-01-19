from app import app
from pytest import fixture


@fixture
def client():
    return app.test_client()


def test_api_posts(client):
    retur = client.get("/api/posts")
    assert retur.status_code == 200
    assert type(retur.json) == list
    assert len(retur.json) > 0
    for post in retur.json:
        assert set(post.keys()) == {'pic', 'pk', 'views_count', 'content',
                                    'likes_count', 'poster_name', 'poster_avatar'}


def test_api_inform(client):
    retur = client.get(f"/api/post/{2}")
    assert retur.status_code == 200
    assert type(retur.json) == dict
    assert set(retur.json.keys()) == {'pic', 'pk', 'views_count', 'content',
                                      'likes_count', 'poster_name', 'poster_avatar'}
    assert len(retur.json) > 0
