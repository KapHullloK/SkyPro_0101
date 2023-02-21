from dao.genre_dao import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def add(self, data):
        return self.dao.add(data)

    def update(self, data):
        gid = data.get("id")
        get_genre = self.get_one(gid)

        get_genre.name = data.get("name")
        self.dao.update(get_genre)

    def patch(self, data):
        gid = data.get("id")
        get_genre = self.get_one(gid)

        if "name" in data:
            get_genre.title = data.get("name")

        self.dao.update(get_genre)

    def delete(self, gid):
        self.dao.delete(gid)
