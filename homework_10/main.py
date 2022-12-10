from flask import Flask
import performance

app = Flask(__name__)


# главная страница
@app.route('/')
def home_page():
    return f"<pre>{performance.get_all()}</pre>"


# вывод кандидата по pk
@app.route('/candidates/<int:uid>')
def candidates_page(uid):
    return f"<pre>{performance.get_by_pk(uid)}</pre>"


# вывод кандидатов по skill
@app.route('/skill/<string:skill>')
def skills_page(skill):
    resuls = ''
    for condidate in performance.get_by_skill(skill):
        condidate_str = f"{condidate['name']}<br>" \
                        f"{condidate['position']}<br>" \
                        f"{condidate['skills']}<br><br>"
        resuls += condidate_str

    return f"<pre>{resuls}</pre>"


app.run()
