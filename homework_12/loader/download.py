import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
import json

download_blueprint = Blueprint('download_blueprint', __name__)


@download_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    if request.method == 'GET':
        return render_template('post_form.html')
    elif request.method == 'POST':
        pict_inform = request.files.get("picture")
        cont_inform = request.form.get("content")

        if pict_inform is None and cont_inform is None:
            return 'ошибка загрузки'

        last_pict = checking_the_extension(pict_inform)

        if last_pict == "Ошибка расширения":
            return "Ошибка расширения"

        if save_data(last_pict, cont_inform) != "Файл не найден":

            return render_template('post_uploaded.html', pict=last_pict, cont=cont_inform)

        else:
            return "Файл не найден"


def checking_the_extension(pict):
    pict_name = pict.filename
    pict_extension = pict_name.split('.')[-1]

    if pict_extension.lower() in ["jpeg", "png"]:
        pict.save(f"uploads/images/{pict_name}")
        return f"uploads/images/{pict_name}"
    else:
        logging.info("загруженный файл - не картинка")
        return "Ошибка расширения"


def save_data(pict, cont):
    try:
        with open('posts.json', encoding='utf-8') as f:
            data = json.load(f)
        data.append({"pic": pict, "content": cont})

        with open('posts.json', "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    except FileNotFoundError:
        logging.error("ошибка при загрузке файла")
        return "Файл не найден"

    except JSONDecodeError:
        return "Файл не найден"
