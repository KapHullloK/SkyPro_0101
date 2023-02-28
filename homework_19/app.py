from flask import Flask
from flask_restx import Api

from config import Config
from create_db import create_data
from setup_db import db

from views.movie import movies_ns
from views.director import directors_ns
from views.genre import genres_ns
from views.user import user_ns, auth_ns


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    register(app)
    return app


def register(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    create_data(app, db)


app = create_app(Config())

app.url_map.strict_slashes = False


# @app.errorhandler(404)
# def page_not_found(e):
#     return f"Упс произошла ошибка 404"
#
#
# @app.errorhandler(500)
# def page_not_found(e):
#     return f"Упс произошла ошибка 500"


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
