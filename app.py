from flask import Flask, render_template, request, redirect
from models import Patient

app = Flask(__name__)

# Queue to store patients
patient_queue = []

# Counter for served patients
patients_served_today = 0


@app.route("/")
def home():
    return render_template(
        "home.html",
        queue=patient_queue,
        served=patients_served_today
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    global patient_queue

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        problem = request.form["problem"]

        new_patient = Patient(name, age, problem)

        # Add patient to queue (FIFO)
        patient_queue.append(new_patient)

        return redirect("/")

    return render_template("register.html")


@app.route("/serve")
def serve():
    global patients_served_today

    if patient_queue:
        patient_queue.pop(0)
        patients_served_today += 1

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)