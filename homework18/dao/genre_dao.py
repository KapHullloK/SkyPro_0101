from dao.model.genre import Genre


class GenreDAO:

    def __init__(self, session):
        self.ses = session

    def get_all(self):
        return self.ses.query(Genre).all()

    def get_one(self, gid):
        return self.ses.query(Genre).get(gid)

    def add(self, data):
        new_genre = Genre(**data)
        self.ses.add(new_genre)
        self.ses.commit()

    def update(self, data):
        self.ses.add(data)
        self.ses.commit()
        return data

    def delete(self, gid):
        get_genre = self.get_one(gid)
        self.ses.delete(get_genre)
        self.ses.commit()
