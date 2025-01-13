from flask import Flask, url_for, abort, redirect

app = Flask(__name__)

@app.route("/user/<username>")
def profile(username):
    if username in ['Alex', 'Steve']:
        return f"{username}'s Profile Page"
    elif username == 'Guest':
        return "Guest Profile"
    else:
        abort(401)

@app.errorhandler(401)
def handle_401_error(error):
    print("Undetected visitor")
    return redirect(url_for('profile', username='Guest'))

app.run()

