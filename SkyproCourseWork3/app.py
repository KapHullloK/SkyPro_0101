from flask import Flask, render_template, request

from logger import get_logger
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

from api.api import blu_api

app = Flask(__name__)

log = get_logger(__name__)


# Вывод всех пользователей
@app.route("/")
def show_posts():
    posts = get_posts_all()
    log.info("Главная страница")
    return render_template("index.html", posts=posts)


# Вывод пользователя по pk
@app.route("/post/<int:pk>")
def show_inform(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    log.info("Информация о выбранном пользователе")
    return render_template("post.html", post=post, comments=comments)


# Вывод постов по ключевому слову
@app.route("/search")
def search_inform():
    search_word = request.args.get("word")
    search = search_for_posts(search_word)
    log.info("Поиск по ключевому слову")
    return render_template("index.html", posts=search)


# Все посты пользователя
@app.route("/user/<name>")
def user_feed(name):
    post = get_posts_by_user(name)
    log.info("Все потсты пользователя")
    return render_template("user-feed.html", posts=post, name=name)


# Обработка ошибки 404
@app.errorhandler(404)
def page_not_found(e):
    return f"Упс произошла ошибка 404"


# Обработка ошибки 500
@app.errorhandler(500)
def page_not_found(e):
    return f"Упс произошла ошибка 500"


app.register_blueprint(blu_api)

if __name__ == "__main__":
    app.run()
