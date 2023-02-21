from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class genres_view(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genres_ns.route('/<int:mid>')
class genre_view(Resource):
    def get(self, mid):
        genre = genre_service.get_one(mid)
        return genre_schema.dump(genre), 200
