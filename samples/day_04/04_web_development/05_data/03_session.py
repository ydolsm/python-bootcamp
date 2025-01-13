from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    "admin": "password123",
    "user": "pass456"
}

@app.route('/')
def home():
    if 'username' in session:
        return f"""
            Welcome, {session['username']}!
            <a href='/logout'>Logout</a>
        """
    else:
        return f"""
        Welcome!
        <a href='/login'>Login</a>
    """

@app.get('/login')
def login_get():
    return """
        <form method="post">
            <label for="username">Username:</label>
            <input type="text" name="username"><br>
            <label for="password">Password:</label>
            <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    """

@app.post('/login')

def login_post():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login_get'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

app.run()