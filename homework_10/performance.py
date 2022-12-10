import json


# загружает данные из файла
def load_candidates():
    with open('candidates.json') as f:
        data = json.load(f)
        return data


# показывает всех кандидатов
def get_all():
    candidates = load_candidates()
    return f"{candidates[0]['name']}\n" \
           f"{candidates[0]['position']}\n" \
           f"{candidates[0]['skills']}\n" \
           f"\n" \
           f"{candidates[1]['name']}\n" \
           f"{candidates[1]['position']}\n" \
           f"{candidates[1]['skills']}\n" \
           f"\n" \
           f"{candidates[2]['name']}\n" \
           f"{candidates[2]['position']}\n" \
           f"{candidates[2]['skills']}\n" \
           f"\n" \
           f"{candidates[3]['name']}\n" \
           f"{candidates[3]['position']}\n" \
           f"{candidates[3]['skills']}\n" \
           f"\n" \
           f"{candidates[4]['name']}\n" \
           f"{candidates[4]['position']}\n" \
           f"{candidates[4]['skills']}\n" \
           f"\n" \
           f"{candidates[5]['name']}\n" \
           f"{candidates[5]['position']}\n" \
           f"{candidates[5]['skills']}\n" \
           f"\n" \
           f"{candidates[6]['name']}\n" \
           f"{candidates[6]['position']}\n" \
           f"{candidates[6]['skills']}"


# вернет кандидата по pk
def get_by_pk(pk):
    for pk_return in load_candidates():
        if pk == pk_return['pk']:
            return f"<img src='{pk_return['picture']}'>\n" \
                   f"{pk_return['name']}\n" \
                   f"{pk_return['position']}\n" \
                   f"{pk_return['skills']}"


# вернет кандидатов по навыку
def get_by_skill(skill_name):
    results = []
    for skill_return in load_candidates():
        if skill_name in (skill_return['skills']).split(', '):
            results.append(skill_return)

    return results
