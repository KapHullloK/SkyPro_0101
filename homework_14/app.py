from flask import Flask

from utills import search_word, search_by_year_range, search_by_rating, fresh_films

app = Flask(__name__)


@app.route("/movie/<title>")
def movie(title):
    film = search_word(title)
    return film


@app.route("/movie/<int:year_1>/to/<int:year_2>")
def movies(year_1, year_2):
    films = search_by_year_range(year_1, year_2)
    return films


@app.route("/rating/<title>")
def rating_by_word(title):
    films_rating = search_by_rating(title)
    return films_rating


@app.route("/genre/<genre>")
def new_films(genre):
    fresh = fresh_films(genre)
    return fresh


@app.errorhandler(404)
def page_not_found(e):
    return f"Упс произошла ошибка 404"


@app.errorhandler(500)
def page_not_found(e):
    return f"Упс произошла ошибка 500"


if __name__ == "__main__":
    app.run()
