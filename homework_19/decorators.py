import jwt
from flask import request, abort

from config import Config


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        token = request.headers['Authorization'].split("Bearer ")[-1]

        try:
            jwt.decode(token, Config.SECRET_HERE, algorithms=[Config.ALGO])

        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        global role
        if "Authorization" not in request.headers:
            abort(401)

        token = request.headers['Authorization'].split('Bearer ')[-1]

        try:
            user = jwt.decode(token, Config.SECRET_HERE, algorithms=[Config.ALGO])
            role = user.get('role')

        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        if role != 'admin':
            abort(401)

        return func(*args, **kwargs)

    return wrapper
