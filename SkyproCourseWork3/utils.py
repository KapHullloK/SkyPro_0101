# Получение всех данных из posts.json
def get_posts_all():
    import json
    with open("data/posts.json", 'r', encoding="utf-8") as f:
        return json.load(f)


# Поиск пользователя по его имени
def get_posts_by_user(user_name):
    result_posts = []
    all_users = []
    for user_post in get_posts_all():
        all_users.append(user_post["poster_name"])
        if user_name == user_post["poster_name"]:
            result_posts.append(user_post)
    if user_name not in all_users:
        raise ValueError("the user is not")
    return result_posts


# Получение комментариев по id
def get_comments_by_post_id(post_id):
    import json
    with open("data/comments.json", 'r', encoding="utf-8") as file:
        comments = json.load(file)

    check_posts = False
    for pk_post in get_posts_all():
        if post_id == pk_post["pk"]:
            check_posts = True

    if not check_posts:
        raise ValueError("there is no such post")

    result_comments = []
    for comment in comments:
        if post_id == comment["post_id"]:
            result_comments.append(comment)

    return result_comments


# Получение постов по ключевому слову
def search_for_posts(query):
    keyword_posts = []
    for keyword in get_posts_all():
        if query.lower() in keyword["content"].lower():
            keyword_posts.append(keyword)
    return keyword_posts


# Получение поста по id
def get_post_by_pk(pk):
    for pk_post in get_posts_all():
        if pk == pk_post["pk"]:
            return pk_post
