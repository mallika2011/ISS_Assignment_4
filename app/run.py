from flask import Flask
from flask import render_template
from flask import request, json, jsonify
from add import answer
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ans1 = db.Column(db.Integer, unique=False)
    ans2 = db.Column(db.Integer, unique=False)
    ans3 = db.Column(db.Integer, unique=False)
    ans4 = db.Column(db.Integer, unique=False)

    def __init__(self, ans1, ans2, ans3, ans4):
        # self.id=id
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4

    def __repr__(self):
        return '< User %r >' % self.ans1 % self.ans2 % self.ans3 %self.ans4



@app.route("/answer", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # print("mallika")
        req_data = request.get_json()
        # print(req_data)
        x1 = req_data['x1']
        x2 = req_data['x2']
        x = (answer(x1, x2))
        # print(x)
    return jsonify(x)


@app.route("/quiz", methods=["POST"])
def userAdd():
    ans1 = request.form['ans1']
    ans2 = request.form['ans2']
    ans3 = request.form['ans3']
    ans4 = request.form['ans4']

    db.create_all()
    new_person = User(ans1,ans2,ans3,ans4)
    db.session.add(new_person)
    db.session.commit()
    temp = {}
    temp['status'] = (type(new_person) == User)
#     return jsonify(temp)
    return render_template("quizzes.html")


@app.route("/quiz/results")
def userFetch():
    db.create_all()
    allUsers = User.query.all()
    strf = ''
    # return jsonify(allUsers)
    for user in allUsers:
        strf += str(user.ans1) + " " + str(user.ans2) + " " + str(user.ans3) + " " + str(user.ans4)+"\n"
    return render_template("quiz_res.html", user=allUsers)





@app.route("/exp1", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/exp2", methods=["GET", "POST"])
def home2():
    return render_template('page2.html')


@app.route("/help", methods=["GET", "POST"])
def help():
    return render_template('help.html')

@app.route("/introduction", methods=["GET", "POST"])
def intro():

    return render_template('introduction.html')


@app.route("/experiment", methods=["GET", "POST"])
def experiment():

    return render_template('experiment.html')


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    return render_template('feedback.html')


@app.route("/manual", methods=["GET", "POST"])
def manual():

    return render_template('manual.html')


@app.route("/obj", methods=["GET", "POST"])
def obj():

    return render_template('objective.html')


@app.route("/procedure", methods=["GET", "POST"])
def proc():

    return render_template('procedure.html')


@app.route("/quizzes", methods=["GET", "POST"])
def quiz():

    return render_template('quizzes.html')


@app.route("/references", methods=["GET", "POST"])
def ref():

    return render_template('references.html')


@app.route("/theory", methods=["GET", "POST"])
def theory():

    return render_template('theory.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
