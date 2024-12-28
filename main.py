import requests
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>It works :D</h1>"

@app.route("/badge/")
def get_badge():
    idd = request.args.get("id")
    username = request.args.get("username")
    url = f"https://us-central1-cssbattleapp.cloudfunctions.net/getRank?userId={idd}"
    response = requests.get(url)
    data = response.json()
    data["id"] = response.json()

    data["score"] = round(data["score"], 2)
    data["name"] = username if username else "CSSBattle"
    # data["meanScore"] = round(float(data["score"]) / float(data["playedCount"]), 2)

    return render_template("badge.html", data=data)

# flask --app main.py run