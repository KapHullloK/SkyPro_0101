import json


# Загружает все данные
def load_data():
    with open("data/schedule.json", "r", encoding="utf-8") as f:
        return json.load(f)


# Выгружает данные за текущий день
def data_trains():
    data = load_data()
    return data


# Поиск поезда по pk
def filter_data(pk):
    for train in load_data():
        if int(pk) == train["pk"]:
            return train


print(set(filter_data(2).keys()))
