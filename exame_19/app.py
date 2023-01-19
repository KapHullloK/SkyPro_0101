from flask import Flask, render_template, request, jsonify

from logger import get_logger
from utils import data_trains, filter_data

app = Flask(__name__)

log = get_logger(__name__)


# Получает расписание всех поездов и выводит их на главной странице
@app.route("/")
def main_page():
    schedule = data_trains()
    log.info("Главная страница")
    return render_template("index.html", schedule=schedule)


# Поиск поезда по его номеру
@app.route("/search")
def search_page():
    search_word = request.args.get("word")
    train = filter_data(search_word)
    log.info(f"Поиск поезда {search_word}")
    return render_template("train.html", train=train)


# Вывод API всего расписания
@app.route("/api/trains")
def api_posts():
    trains = data_trains()
    log.info("Загрузка данных JSON")
    return jsonify(trains)


# Вывод API расписания выбраного поезда
@app.route("/api/train/<int:pk>")
def api_inform(pk):
    train = filter_data(pk)
    log.info(f"Загрузка JSON поезда {pk}")
    return jsonify(train)


if __name__ == "__main__":
    app.run()
