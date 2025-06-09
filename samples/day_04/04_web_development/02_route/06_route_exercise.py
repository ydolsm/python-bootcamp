from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
            <h1>Welcome to my page</h1>

            <a href="{url_for('login')}">Login Page</a>
            <a href="{url_for('dynamic_profile', username='Ace')}">Ace</a>
        """

@app.route("/login/")
def login():
    return "Please login"

@app.route("/profile/<username>")
def dynamic_profile(username):
    if username != "admin":
        return redirect(url_for('login'))
    else:
        return f"Welcome Admin"

@app.route("/page/")
@app.route("/page/<topic>")
def subject(topic=None):
    if topic:
        return f"Viewing page for {topic}"
    else:
        return "View Topics"

app.run()