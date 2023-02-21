from flask_restx import Resource, Namespace
from flask import request
from dao.model.movie import MovieSchema
from implemented import movie_service

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class Movies_view(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        all_movies = movie_service.get_all(director_id, genre_id, year)
        return movies_schema.dump(all_movies), 200

    def post(self):
        data = request.json
        movie_service.add(data)
        return "OK", 201


@movies_ns.route('/<int:mid>')
class Movie_view(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        movie_service.update(data, mid)
        return "OK", 201

    def delete(self, mid):
        movie_service.delete(mid)
        return "OK", 204
