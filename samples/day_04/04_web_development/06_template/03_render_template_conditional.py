from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('conditional.html', logged_in=True)

app.run()