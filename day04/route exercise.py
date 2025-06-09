from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return f"""
#             <h1>Welcome to my page</h1>
#
#             <a href="{url_for('login_get')}">Login Page</a>
#             <a href="{url_for('dynamic_profile', username='Ace')}">Ace</a>
#         """
@app.route("/")
def index():
    return "Welcome to my page"

@app.get("/login/")
def login_get():
    return render_template("index.html")

def valid(username, email , password ):
    return (
        username == "admin"
        and password == "pass"
        and email == "admin@gmail.com"
)

@app.post("/login/")
def login_post():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    if not valid(username, email, password):
        return 'Invalid credentials!'
    else:
        return 'Login successful!'

@app.route("/profile/<username>")
def dynamic_profile(username):
    return render_template(
        "profile.html",
        username = username
    )

@app.route("/page/")
@app.route("/page/<topic>")
def subject(topic=None):
    if topic:
        return f"Viewing page for {topic}"
    else:
        return "View Topics"

app.run()