import requests
from flask import Flask, request, redirect, url_for, render_template, redirect
import flask

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("https://github.com/BahAilime/cssBattleBadge")

@app.route("/badge/")
def get_badge():
    user_id = request.args.get("id")
    username = request.args.get("username")

    if user_id is None:
        if any("html" in str(mime) for mime in request.accept_mimetypes):
            return render_template("noid.html")
        elif any("image" in str(mime) for mime in request.accept_mimetypes):
            return flask.send_from_directory('static', 'noid.png')

    data = fetch_user_data(user_id)
    data = process_data(data, username)

    return flask.Response(
        render_template("badge.html", data=data),
        mimetype='image/svg+xml'
    )

# flask --app main.py run