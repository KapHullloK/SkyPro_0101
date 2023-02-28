from dao.model.user import User
from sqlalchemy.orm.scoping import Session


class UserDAO:

    def __init__(self, session: Session):
        self.ses = session

    def get_all(self):
        return self.ses.query(User).all()

    def get_one(self, name):
        return User.query.filter_by(username=name).first()

    def add(self, data):
        new_user = User(**data)
        self.ses.add(new_user)
        self.ses.commit()
        return new_user

    def update(self, data):
        self.ses.add(data)
        self.ses.commit()
        return data

    def delete(self, mid):
        get_user = self.get_one(mid)
        self.ses.delete(get_user)
        self.ses.commit()
