from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/submit", methods=["POST"])
def submit():
    preg = request.form["preg"]
    plas = request.form["plas"]
    pres = request.form["pres"]
    skin = request.form["skin"]
    test = request.form["test"]
    masss = request.form["masss"]
    pedi = request.form["pedi"]
    age = request.form["age"]

    # Just to verify (you can remove later)
    return f"""
    Preg: {preg}, Plas: {plas}, Pres: {pres}, Skin: {skin},
    Test: {test}, Mass: {masss}, Pedi: {pedi}, Age: {age}
    """


if __name__ == "__main__":
    app.run(debug=True)
