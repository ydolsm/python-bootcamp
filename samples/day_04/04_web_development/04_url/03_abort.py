from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
	return "Index Page"

@app.route('/login')
def login():
	abort(501)

app.run()