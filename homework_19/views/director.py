from flask import request
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from decorators import auth_required, admin_required
from implemented import director_service

directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class Directors_view(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @admin_required
    def post(self):
        data = request.json
        director_service.add(data)
        return "OK", 201


@directors_ns.route('/<int:mid>')
class Director_view(Resource):
    @auth_required
    def get(self, mid):
        director = director_service.get_one(mid)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, mid):
        data = request.json
        director_service.update(data, mid)
        return "OK", 201

    @admin_required
    def delete(self, mid):
        director_service.delete(mid)
        return "OK", 204
