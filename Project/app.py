from flask import Flask , render_template , request
import joblib


model = joblib.load('model.pkl')


# Initial
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/submit' , methods=['post'])
def submit():
    preg = eval(request.form.get("preg"))
    plas = eval(request.form.get("plas"))
    pres = eval(request.form.get("pres"))
    skin = eval(request.form.get("skin"))
    test = eval(request.form.get("test"))
    masss = eval(request.form.get("masss"))
    pedi = eval(request.form.get("pedi"))
    age = eval(request.form.get("age"))

    prediction = model.predict([[preg, plas, pres, skin, test, masss, pedi, age]])

    if prediction[0] == 0:
        return render_template('non_diabetic.html')
    else:
        return render_template('diabetic.html')


app.run(debug=True)

# http://127.0.0.1:5000

# https://www.tutort.net/

# POST :-
# PUT :-
# DELETE :-