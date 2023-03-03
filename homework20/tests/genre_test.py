import pytest
from unittest.mock import MagicMock

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    data = GenreDAO(None)
    gen1 = Genre(id=1, name='action')
    gen2 = Genre(id=2, name='comedy')
    gen3 = Genre(id=3, name='horror')

    data.get_one = MagicMock(return_value=gen1)
    data.get_all = MagicMock(return_value=[gen1, gen2, gen3])
    data.create = MagicMock(return_value=Genre(id=1))
    data.update = MagicMock()
    data.delete = MagicMock()
    return data


class TestService():
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre_one = self.genre_service.get_one(1)
        assert genre_one is not None
        assert genre_one.id == 1
        assert genre_one.name == 'action'

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        new_genre = {"id": 1, "name": "war"}
        add = self.genre_service.create(new_genre)
        assert add is not None

    def test_update(self):
        new_genre = {"id": 1, "name": "animation"}
        add = self.genre_service.update(new_genre)
        assert add is not None

    def test_delete(self):
        delete = self.genre_service.delete(1)
        assert delete is None
