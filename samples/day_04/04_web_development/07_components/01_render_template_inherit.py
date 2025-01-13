from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/child/')
def child():
    return render_template('child.html')

@app.route('/parent/')
def parent():
    return render_template('parent.html')

app.run()