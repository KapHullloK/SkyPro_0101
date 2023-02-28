import jwt
from flask import abort
import calendar
import datetime
from dao.user import UserDAO
import hashlib
from config import Config


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao
        self.secret = Config.SECRET_HERE
        self.algo = Config.ALGO

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, name):
        return self.dao.get_one(name)

    def add(self, data):
        data['password'] = self.get_hash(data['password'])
        return self.dao.add(data)

    def get_hash(self, password):
        bytes = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode("utf-8"),
            salt=Config.PWD_HASH_SALT,
            iterations=Config.PWD_HASH_ITERATIONS
        ).hex()

        return bytes

    def post_tokens(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        if None in [username, password]:
            abort(401)

        user = self.get_one(username)

        if user is None:
            return {"error": "Неверные учётные данные"}, 401

        if self.get_hash(password) != user.password:
            return {"error": "Неверные учётные данные"}, 401

        data = {
            "username": user.username,
            "role": user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, self.secret, algorithm=self.algo)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, self.secret, algorithm=self.algo)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return tokens, 201

    def put_tokens(self, data):
        refresh_token = data.get("refresh_token")
        if refresh_token is None:
            abort(400)

        try:
            data = jwt.decode(jwt=refresh_token, key=self.secret, algorithms=[self.algo])
        except Exception as e:
            abort(400)

        username = data.get("username")

        user = self.get_one(username)

        data = {
            "username": user.username,
            "role": user.role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, self.secret, algorithm=self.algo)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, self.secret, algorithm=self.algo)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return tokens, 201

    # def update(self, data, uid):
    #     get_user = self.get_one(uid)
    #
    #     get_user.username = data.get("username")
    #     get_user.password = data.get("password")
    #     get_user.role = data.get("role")
    #
    #     self.dao.update(get_user)
    #
    # def patch(self, data):
    #     uid = data.get("id")
    #     get_user = self.get_one(uid)
    #
    #     if "username" in data:
    #         get_user.username = data.get("username")
    #     if "password" in data:
    #         get_user.password = data.get("password")
    #     if "role" in data:
    #         get_user.role = data.get("role")
    #
    #     self.dao.update(get_user)
    #
    # def delete(self, uid):
    #     self.dao.delete(uid)
