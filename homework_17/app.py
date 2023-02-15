from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api = Api(app)
movie_ns = api.namespace('movies')
director_ns = api.namespace('directors')
genre_ns = api.namespace('genres')


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

director_schema = DirectorSchema
directors_schema = DirectorSchema(many=True)

genre_schema = GenreSchema
genres_schema = GenreSchema(many=True)


@movie_ns.route('/')
class MovieView(Resource):

    def get(self):
        direct = request.args.get("director_id", 0)
        genre = request.args.get("genre_id", 0)
        if direct and genre:
            return movies_schema.dump(Movie.query.filter(Movie.director_id == direct,
                                                         Movie.genre_id == genre)), 200

        if direct:
            return movies_schema.dump(Movie.query.filter(Movie.director_id == direct)), 200

        if genre:
            return movies_schema.dump(Movie.query.filter(Movie.genre_id == genre)), 200

        movies = Movie.query.all()
        return movies_schema.dump(movies), 200


@movie_ns.route('/<int:pk>')
class MovieView(Resource):
    def get(self, pk):
        movie = Movie.query.get(pk)
        return movie_schema.dump(movie), 200


@director_ns.route('/')
class DirectorView(Resource):

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@director_ns.route('/<int:pk>')
class DirectorView(Resource):

    def put(self, pk: int):
        direct = Director.query.get(pk)
        if not direct:
            return "", 404
        req_json = request.json
        direct.name = req_json.get("name")
        db.session.add(direct)
        db.session.commit()
        return "", 204

    def delete(self, pk: int):
        direct = Director.query.get(pk)
        if not direct:
            return "", 404
        Director.query.filter(Director.id == pk).delete()
        db.session.commit()
        return "", 204


@genre_ns.route('/')
class GenreView(Resource):

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201


@genre_ns.route('/<int:pk>')
class GenreView(Resource):

    def put(self, pk: int):
        genre = Genre.query.get(pk)
        if not genre:
            return "", 404
        req_json = request.json
        genre.name = req_json.get("name")
        db.session.add(genre)
        db.session.commit()
        return "", 204

    def delete(self, pk: int):
        genre = Genre.query.get(pk)
        if not genre:
            return "", 404
        Genre.query.filter(Genre.id == pk).delete()
        db.session.commit()
        return "", 204


@app.errorhandler(404)
def page_not_found(e):
    return f"Упс произошла ошибка 404"


@app.errorhandler(500)
def page_not_found(e):
    return f"Упс произошла ошибка 500"


if __name__ == '__main__':
    app.run(debug=True)
