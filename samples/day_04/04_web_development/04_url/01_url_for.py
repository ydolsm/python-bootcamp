from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return f'''
	    <a href="{url_for('login')}">Login Page</a>
        <a href="{url_for('profile', username='Ace')}">Ace</a>
    '''

@app.route("/login/")
def login():
    return "Login Page"

@app.route("/user/<username>")
def profile(username):
    return f"{username}'s Profile Page"

app.run()