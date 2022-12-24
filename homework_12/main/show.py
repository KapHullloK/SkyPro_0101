import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
import json

show_blueprint = Blueprint('show_blueprint', __name__)


@show_blueprint.route("/")
def page_index():
    return render_template('index.html')


@show_blueprint.route("/search")
def page_search():
    results = []
    s = request.args.get("s")
    logging.info("выполнен поиск")
    loads = load_json()
    if loads != "Файл не найден":
        for load in loads:
            if s in load["content"]:
                results.append(load)
        return render_template('post_list.html', s=s, loads=results)
    else:
        return "Файл не найден"


def load_json():
    try:
        with open('posts.json', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("ошибка при загрузке файла")
        return "Файл не найден"

    except JSONDecodeError:
        return "Файл не найден"
