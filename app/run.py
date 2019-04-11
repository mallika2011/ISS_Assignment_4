from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/bit", methods=["GET", "POST"])
def index():
    return "4 BIT ADDITION"




@app.route("/exp", methods=["GET", "POST"])
def home():
    return render_template('index.html')


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





if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
