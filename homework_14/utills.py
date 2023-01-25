import sqlite3


# Поиск по названию фильма и вывод самого нового фильма
def search_word(word):
    with sqlite3.connect("netflix.db") as f:
        cur = f.cursor()
        sqlite_query = ("""
        select title, country, max(release_year), listed_in, description
        from netflix
        where title like ? """)
        cur.execute(sqlite_query, (word,))
        executed_query = cur.fetchall()

        json_executed_query = {
            "title": executed_query[0][0],
            "country": executed_query[0][1],
            "release_year": executed_query[0][2],
            "genre": executed_query[0][3],
            "description": executed_query[0][4]
        }
        return json_executed_query


# Поиск по диапазону лет ввода (максимум вывода 100 фильмов)
def search_by_year_range(year_1, year_2):
    with sqlite3.connect("netflix.db") as f:
        cur = f.cursor()
        sqlite_query = ("""
        select title, release_year
        from netflix
        where release_year between ? and ?
        limit 100 """)
        cur.execute(sqlite_query, (year_1, year_2,))
        executed_query = cur.fetchall()

        json_executed_query = []

        for film in executed_query:
            json_executed_query.append(
                {"title": film[0],
                 "release_year": film[1]},
            )

        return json_executed_query


# Поиск по группе рейтингов (выводит группу с фильмами этого рейтинга)
def search_by_rating(rating):
    # children = ['TV-G', 'G']
    # family = ['PG-13', 'TV-14', 'TV-PG', 'PG', 'G']
    # adult = ['TV-MA', 'R', 'NC-17']
    json_search_by_rating = []

    with sqlite3.connect("netflix.db") as f:
        cur = f.cursor()
        if rating == "children":
            sqlite_query = ("""
            select title, rating, description
            from netflix
            WHERE rating = 'TV-G' or rating = 'G' """)

        elif rating == "family":
            sqlite_query = ("""
            select title, rating, description
            from netflix
            WHERE rating = 'PG-13' or rating = 'TV-14'
            or rating = 'TV-PG' or rating = 'PG' or rating = 'G' """)

        elif rating == "adult":
            sqlite_query = ("""
            select title, rating, description
            from netflix
            WHERE rating = 'TV-MA' or rating = 'R'
            or rating = 'NC-17' """)

        else:
            return "Enter specific groups -> children | family | adult"

        cur.execute(sqlite_query)
        executed_query = cur.fetchall()

        for rating_film in executed_query:
            json_search_by_rating.append(
                {
                    "title": rating_film[0],
                    "rating": rating_film[1],
                    "description": rating_film[2]
                },
            )
        return json_search_by_rating


# возвращает JSON с 10 самыми свежими фильмами
def fresh_films(genre):
    json_executed_query = []
    with sqlite3.connect("netflix.db") as f:
        cur = f.cursor()
        sqlite_query = ("""
        select title, description
        from netflix
        where listed_in = ?
        order by release_year DESC
        limit 10 """)
        cur.execute(sqlite_query, (genre,))
        executed_query = cur.fetchall()

        for film in executed_query:
            json_executed_query.append(
                {
                    "title": film[0],
                    "description": film[1]
                }
            )

        return json_executed_query


# Получает имена 2 актёров и по ним ищет актёров
# которые играли с ними больше 2 раз
def two_actors(act_1, act_2):
    result = {}
    ans = []
    with sqlite3.connect("netflix.db") as f:
        cur = f.cursor()
        sqlite_query = ("""
        select netflix.cast
        from netflix
        where netflix.cast like ? and netflix.cast like ? """)
        cur.execute(sqlite_query, (act_1, act_2,))
        executed_query = cur.fetchall()

        for actors in executed_query:
            for acts in actors:
                for act in acts.split(', '):
                    if act not in [act_1[1:-1], act_2[1:-1]]:
                        if act in result:
                            result[act] += 1
                        else:
                            result[act] = 1
    for k, v in result.items():
        if v > 2:
            ans.append(k)
    return ans


# Ищет фильмы по переданному типу, году, жанру
def picture_search(style, year, genre):
    json_executed_query = []
    with sqlite3.connect("netflix.db") as f:
        cur = f.cursor()
        sqlite_query = ("""
        select title, description
        from netflix
        where netflix.type like ? 
        and netflix.release_year like ? 
        and netflix.listed_in like ? """)
        cur.execute(sqlite_query, (style, year, genre,))
        executed_query = cur.fetchall()

        for films in executed_query:
            json_executed_query.append(
                {
                    "title": films[0],
                    "description": films[1]
                }
            )

        return json_executed_query
