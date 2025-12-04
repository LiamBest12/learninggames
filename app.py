from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"

@app.route("/home")
def home():
    return "Welcome to the Home Page!"

@app.route("/username/<username>")
def show_username(username):
    return f"Hello, {username}!"