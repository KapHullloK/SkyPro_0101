from flask import request
from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from decorators import auth_required, admin_required
from implemented import genre_service

genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class genres_view(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    @admin_required
    def post(self):
        data = request.json
        genre_service.add(data)
        return "OK", 201


@genres_ns.route('/<int:mid>')
class genre_view(Resource):
    @auth_required
    def get(self, mid):
        genre = genre_service.get_one(mid)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, mid):
        data = request.json
        genre_service.update(data, mid)
        return "OK", 201

    @admin_required
    def delete(self, mid):
        genre_service.delete(mid)
        return "OK", 204
