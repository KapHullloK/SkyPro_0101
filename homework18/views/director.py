from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class Directors_view(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@directors_ns.route('/<int:mid>')
class Director_view(Resource):
    def get(self, mid):
        Director = director_service.get_one(mid)
        return director_schema.dump(Director), 200
