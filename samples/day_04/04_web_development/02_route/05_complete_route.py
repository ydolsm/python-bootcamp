from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/profile/")
@app.route("/profiles/")
@app.route("/profile/<username>")
def profile(username=None):
    if username:
        return f"Profile {username} Page"
    else:
        return "Profile Page"

app.run()