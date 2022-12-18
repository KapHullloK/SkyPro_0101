import utils
from flask import Flask, render_template

app = Flask(__name__)


# Выводит всех кандидатов
@app.route('/')
def home_page():
    return render_template('list.html', names=utils.load_candidates_from_json())


# Выводит кандидата по id
@app.route('/candidates/<int:id_>')
def inform_id_page(id_):
    information_candidate = utils.get_candidate(id_)
    return render_template('single.html', name=information_candidate[0], position=information_candidate[1],
                           image=information_candidate[2], skills=information_candidate[3])


# Выводит всех кандидатов по совпадению имени ввода
@app.route('/search/<string:candidate_name>')
def inform_name_page(candidate_name):
    information_candidate = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', total_candidates=len(information_candidate[0]),
                           id_candidates=information_candidate[1])


# Выводит всех кандидатов по совпадению скила ввода
@app.route('/skill/<string:skill_name>')
def inform_skills_page(skill_name):
    information_candidate = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', input_skill=skill_name, total_candidates=len(information_candidate[0]),
                           id_candidates=information_candidate[1])


app.run()
