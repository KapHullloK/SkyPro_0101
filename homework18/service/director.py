from dao.director_dao import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def add(self, data):
        return self.dao.add(data)

    def update(self, data):
        mid = data.get("id")
        get_Director = self.get_one(mid)

        get_Director.title = data.get("title")
        get_Director.description = data.get("description")
        get_Director.trailer = data.get("trailer")
        get_Director.year = data.get("year")
        get_Director.rating = data.get("rating")

        self.dao.update(get_Director)

    def patch(self, data):
        mid = data.get("id")
        get_Director = self.get_one(mid)

        if "title" in data:
            get_Director.title = data.get("title")
        if "description" in data:
            get_Director.description = data.get("description")
        if "trailer" in data:
            get_Director.trailer = data.get("trailer")
        if "year" in data:
            get_Director.year = data.get("year")
        if "rating" in data:
            get_Director.rating = data.get("rating")

        self.dao.update(get_Director)

    def delete(self, mid):
        self.dao.delete(mid)
