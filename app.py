from flask import Flask, url_for

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
with app.test_request_context():
    url_for("static", filename="login.html")
@app.route("/login")
def login():
    return "Please log in to continue."

