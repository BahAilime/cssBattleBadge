import requests
from flask import Flask, request, redirect, url_for, render_template, redirect
import flask

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("https://github.com/BahAilime/cssBattleBadge")

@app.route("/badge/")
def get_badge():
    idd = request.args.get("id")
    username = request.args.get("username")
    url = f"https://us-central1-cssbattleapp.cloudfunctions.net/getRank?userId={idd}"
    response = requests.get(url)
    data = response.json()
    data["id"] = response.json()

    data["score"] = round(data["score"], 2)
    data["name"] = f"{username}'s CSSBattle.dev Stats" if username else "CSSBattle.dev Stats"
    # data["meanScore"] = round(float(data["score"]) / float(data["playedCount"]), 2)

    return flask.Response(
        render_template("badge.html", data=data),
        mimetype='image/svg+xml'
    )

# flask --app main.py run