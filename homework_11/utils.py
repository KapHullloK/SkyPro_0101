import json


# возвращает candidates.json
def candidates_json():
    with open('candidates.json') as f:
        data = json.load(f)
        return data


# возвращает имена всех кандидатов
def load_candidates_from_json():
    conclusion = []
    for candidates in candidates_json():
        conclusion.append(candidates['name'])
    return conclusion


# возвращает одного кандидата по его id
def get_candidate(candidate_id):
    for id_ in candidates_json():
        if candidate_id == id_['id']:
            return [id_['name'], id_['position'], id_['picture'], id_['skills']]


# возвращает кандидатов по имени
def get_candidates_by_name(candidate_name):
    total_candidates_name = []
    total_candidates_id = {}
    for name in candidates_json():
        if candidate_name in name['name']:
            total_candidates_name.append(name['name'])
            total_candidates_id[name['id']] = name['name']
    return total_candidates_name, total_candidates_id


# возвращает кандидатов по навыку
def get_candidates_by_skill(skill_name):
    total_candidates_skills = []
    total_candidates_id = {}
    for skills in candidates_json():
        if skill_name in skills['skills']:
            total_candidates_skills.append(skills['name'])
            total_candidates_id[skills['id']] = skills['name']
    return total_candidates_skills, total_candidates_id
