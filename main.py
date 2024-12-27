import requests
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>It works :D</h1>"

@app.route("/badge/<id>")
def get_badge(id):
    url = f"https://us-central1-cssbattleapp.cloudfunctions.net/getRank?userId={id}"
    response = requests.get(url)
    data = response.json()

    data["score"] = round(data["score"], 2)
    data["meanScore"] = round(float(data["score"]) / float(data["playedCount"]), 2)

    return render_template("badge.html", data=data)

# flask --app main.py run