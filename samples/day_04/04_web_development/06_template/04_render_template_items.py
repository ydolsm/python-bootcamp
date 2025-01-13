from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    items = ['Apple', 'Banana', 'Cherry']
    return render_template('items.html', items=items)

app.run()