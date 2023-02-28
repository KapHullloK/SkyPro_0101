from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from dao.movie_dao import MovieDAO
from dao.user import UserDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from service.user import UserService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)
