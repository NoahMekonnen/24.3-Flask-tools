from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def satisfaction_survey():
    print(satisfaction_survey)
    return render_template('sat_survey.html' ,title = satisfaction_survey.title, instructions = satisfaction_survey.instructions)

@app.route("/questions/<n>")
def give_question(n):
    return render_template(form.html, question = sat_survey.questions[n].question, choices = satisfaction_survey[n].choices)