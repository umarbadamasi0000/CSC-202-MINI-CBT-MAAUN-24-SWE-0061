from flask import Flask, render_template, request
from models import Question, Result

app = Flask(__name__, template_folder='Assignment4/templates')

# Questions (OOP objects, not dictionaries)
questions = [
    Question("Capital of Nigeria?", ["Abuja", "Lagos", "Kano"], "Abuja"),
    Question("2 + 2 = ?", ["3", "4", "5"], "4"),
    Question("Python is a?", ["Snake", "Programming Language", "Car"], "Programming Language")
]

# Stack (LIFO) → store results history
results_stack = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


@app.route("/submit", methods=["POST"])
def submit():
    score = 0

    for i, question in enumerate(questions):
        user_answer = request.form.get(f"q{i}")
        if question.check_answer(user_answer):
            score += 1

    result = Result(score)
    results_stack.append(result)  # STACK used here

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)