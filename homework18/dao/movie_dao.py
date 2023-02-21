from dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.ses = session

    def get_all(self, director_id, genre_id, year):
        res = self.ses.query(Movie)

        if director_id:
            res = res.filter(Movie.director_id == director_id)
        if genre_id:
            res = res.filter(Movie.genre_id == genre_id)
        if year:
            res = res.filter(Movie.year == year)

        return res.all()

    def get_one(self, mid):
        return self.ses.query(Movie).get(mid)

    def add(self, data):
        new_movie = Movie(**data)
        self.ses.add(new_movie)
        self.ses.commit()

    def update(self, data):
        self.ses.add(data)
        self.ses.commit()
        return data

    def delete(self, mid):
        get_movie = self.get_one(mid)
        self.ses.delete(get_movie)
        self.ses.commit()
