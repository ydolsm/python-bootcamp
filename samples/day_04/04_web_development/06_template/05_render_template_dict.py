from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    user_info = {
        'name': 'Eren',
        'location': 'Manila'
    }
    return render_template(
        'profile.html',
        user=user_info,
    )

app.run()