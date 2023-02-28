from dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, director_id, genre_id, year):
        return self.dao.get_all(director_id, genre_id, year)

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def add(self, data):
        return self.dao.add(data)

    def update(self, data, mid):
        get_movie = self.get_one(mid)

        get_movie.title = data.get("title")
        get_movie.description = data.get("description")
        get_movie.trailer = data.get("trailer")
        get_movie.year = data.get("year")
        get_movie.rating = data.get("rating")

        self.dao.update(get_movie)

    def patch(self, data):
        mid = data.get("id")
        get_movie = self.get_one(mid)

        if "title" in data:
            get_movie.title = data.get("title")
        if "description" in data:
            get_movie.description = data.get("description")
        if "trailer" in data:
            get_movie.trailer = data.get("trailer")
        if "year" in data:
            get_movie.year = data.get("year")
        if "rating" in data:
            get_movie.rating = data.get("rating")

        self.dao.update(get_movie)

    def delete(self, mid):
        self.dao.delete(mid)
