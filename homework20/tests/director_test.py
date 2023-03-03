import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    data = DirectorDAO(None)
    dir1 = Director(id=1, name='Mixa')
    dir2 = Director(id=2, name='Dixxx')
    dir3 = Director(id=3, name='Picha')

    data.get_one = MagicMock(return_value=dir1)
    data.get_all = MagicMock(return_value=[dir1, dir2, dir3])
    data.create = MagicMock(return_value=Director(id=1))
    data.update = MagicMock()
    data.delete = MagicMock()
    return data


class TestService():
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director_one = self.director_service.get_one(1)
        assert director_one is not None
        assert director_one.id == 1
        assert director_one.name == 'Mixa'

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        new_director = {"id": 1, "name": "hali"}
        add = self.director_service.create(new_director)
        assert add is not None

    def test_update(self):
        new_director = {"id": 1, "name": "vali"}
        add = self.director_service.update(new_director)
        assert add is not None

    def test_delete(self):
        delete = self.director_service.delete(1)
        assert delete is None
