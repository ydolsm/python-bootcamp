from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route("/user/<username>")
def profile(username):
    if username != "admin":
        return redirect(url_for('login'))
    else:
        return "Welcome Admin"

@app.route('/login')
def login():
    return "Please login"

app.run()
