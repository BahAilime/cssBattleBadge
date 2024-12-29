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

    if idd is None:
        if any("html" in str(mime) for mime in request.accept_mimetypes):
            return render_template("noid.html")
        elif any("image" in str(mime) for mime in request.accept_mimetypes):
            return flask.send_from_directory('static', 'noid.png')

    url = f"https://us-central1-cssbattleapp.cloudfunctions.net/getRank?userId={idd}"
    response = requests.get(url)
    data = response.json()
    data["id"] = response.json()

    data["score"] = round(data["score"], 2)
    data["name"] = f"{username.capitalize()}'s CSSBattle.dev Stats" if username else "CSSBattle.dev Stats"
    data["meanScore"] = f"{round(float(data["score"]) / (float(data["playedCount"]) if data["playedCount"] != 0 else 1), 2)} / 600"

    return flask.Response(
        render_template("badge.html", data=data),
        mimetype='image/svg+xml'
    )

# flask --app main.py run