from flask import Flask, request

app = Flask(__name__)

@app.get('/login')
def login_get():
    return """
    <form method="post">
        <label for="username">Username:</label>
        <input type="text" name="username"><br>
        
        <label for="password">Password:</label>
        <input type="password" name="password"><br>
        
        <label for="email">Email:</label>
        <input type="email" name="email"><br>
        
        <input type="submit" value="Login">
    </form>
    """

def valid(username, email, password):
    return not (
        username == "admin"
        and password == "pass"
        and email == "admin@gmail.com"
    )

@app.post('/login')
def login_post():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    if not valid(username, email, password):
        return 'Invalid credentials!'
    else:
        return 'Login successful!'

app.run()