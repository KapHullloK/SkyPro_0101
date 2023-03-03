import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    data = MovieDAO(None)
    mov1 = Movie(
        id=1,
        title="Йеллоустоун",
        description="Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
        trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
        year=2018,
        rating=8.6,
        genre_id=17,
        director_id=1,
    )
    mov2 = Movie(
        id=2,
        title="Омерзительная восьмерка",
        description="США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.",
        trailer="https://www.youtube.com/watch?v=lmB9VWm0okU",
        year=2015,
        rating=7.8,
        genre_id=4,
        director_id=2,
    )
    mov3 = Movie(
        id=3,
        title="Вооружен и очень опасен",
        description="События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...",
        trailer="https://www.youtube.com/watch?v=hLA5631F-jo",
        year=1978,
        rating=6.0,
        genre_id=17,
        director_id=3,
    )
    data.get_one = MagicMock(return_value=mov1)
    data.get_all = MagicMock(return_value=[mov1, mov2, mov3])
    data.create = MagicMock(return_value=Movie(id=1))
    data.update = MagicMock()
    data.delete = MagicMock()
    return data


class TestService():
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie_one = self.movie_service.get_one(1)
        assert movie_one is not None
        assert movie_one.id == 1
        assert movie_one.title == 'Йеллоустоун'
        assert movie_one.rating == 8.6

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        new_movie = {
            "title": "Чикаго",
            "description": "Рокси Харт мечтает о песнях и танцах и о том, как сравняться с самой Велмой Келли, примадонной водевиля. И Рокси действительно оказывается с Велмой в одном положении, когда несколько очень неправильных шагов приводят обеих на скамью подсудимых.",
            "trailer": "https://www.youtube.com/watch?v=YxzS_LzWdG8",
            "year": 2002,
            "rating": 7.2,
            "genre_id": 18,
            "director_id": 6
        }
        add = self.movie_service.create(new_movie)
        assert add is not None

    def test_update(self):
        new_movie = {
            "title": "Одержимость",
            "description": "Эндрю мечтает стать великим. Казалось бы, вот-вот его мечта осуществится. Юношу замечает настоящий гений, дирижер лучшего в стране оркестра. Желание Эндрю добиться успеха быстро становится одержимостью, а безжалостный наставник продолжает подталкивать его все дальше и дальше – за пределы человеческих возможностей. Кто выйдет победителем из этой схватки?",
            "trailer": "https://www.youtube.com/watch?v=Q9PxDPOo1jw",
            "year": 2013,
            "rating": 8.5,
            "genre_id": 4,
            "director_id": 8
        }
        add = self.movie_service.update(new_movie)
        assert add is not None

    def test_delete(self):
        delete = self.movie_service.delete(1)
        assert delete is None
