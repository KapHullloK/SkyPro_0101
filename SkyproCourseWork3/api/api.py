from flask import Blueprint, jsonify

from logger import get_logger
from utils import get_posts_all, get_post_by_pk

blu_api = Blueprint("api", __name__)

log = get_logger(__name__)


@blu_api.route("/api/posts")
def api_posts():
    posts = get_posts_all()
    log.info("Загрузка постов")
    return jsonify(posts)


@blu_api.route("/api/post/<int:pk>")
def api_inform(pk):
    post = get_post_by_pk(pk)
    log.info(f"Загрузка поста {pk}")
    return jsonify(post)
