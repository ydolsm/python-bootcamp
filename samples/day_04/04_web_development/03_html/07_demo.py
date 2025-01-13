from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """ 
        <h1>Welcome to Flask</h1> 
        
        <p>This is a simple example of HTML in Flask</p> 
        
        <ol> 
            <li>Learn Flask</li> 
            <li>Build a project</li> 
        </ol> 
        
        <a href="https://flask.palletsprojects.com/">Guide</a>
    """
app.run()
