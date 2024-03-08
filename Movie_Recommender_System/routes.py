from flask import render_template
from Movie_Recommender_System import app

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")