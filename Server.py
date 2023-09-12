from flask import Flask, request, render_template
import pickle

with open("lr_model.pkl", 'rb') as file:
    model_lr = pickle.load(file)


app = Flask(__name__,static_url_path='/static')


@app.route("/")
def root():

    return render_template("Result.html")


@app.route("/onclick", methods=["Get"])
def onclick():
    return render_template("index.html")

@app.route("/home", methods=["Get"])
def home():
    return render_template("Result.html")

@app.route("/details", methods=["Get"])
def details():
    return render_template("index.html")


@app.route("/predict", methods=["post"])
def predict():
    airline = int(request.form.get("airline"))
    category = int(request.form.get("Category"))
    source = int(request.form.get("from"))
    to = int(request.form.get("to"))
    dep_period = int(request.form.get("dep_period"))
    arr_period = int(request.form.get("arr_period"))
    day = int(request.form.get("day"))
    month_category = int(request.form.get("month"))
    days_left = int(request.form.get("Days_left"))
    duration = int(request.form.get("Duration"))
    stops_category = int(request.form.get("Stops_category"))
    # algo = request.form.get("algo")


    predictions = model_lr.predict([[airline, category, source, to, dep_period, arr_period,day, month_category, days_left,duration, stops_category]])

    return render_template("Welcome.html", prediction=predictions[0])


app.run(host="0.0.0.0", port=4001, debug=True)
