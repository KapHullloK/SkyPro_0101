from dao.model.director import Director


class DirectorDAO:

    def __init__(self, session):
        self.ses = session

    def get_all(self):
        return self.ses.query(Director).all()

    def get_one(self, did):
        return self.ses.query(Director).get(did)

    def add(self, data):
        new_director = Director(**data)
        self.ses.add(new_director)
        self.ses.commit()

    def update(self, data):
        did = data.get("id")
        get_director = self.get_one(did)

        get_director.name = data.get("name")

        self.ses.add(get_director)
        self.ses.commit()
        return get_director

    def patch(self, data):
        did = data.get("id")
        get_director = self.get_one(did)

        if "name" in data:
            get_director.title = data.get("name")

        self.ses.add(get_director)
        self.ses.commit()
        return get_director

    def delete(self, did):
        get_director = self.get_one(did)
        self.ses.delete(get_director)
        self.ses.commit()
