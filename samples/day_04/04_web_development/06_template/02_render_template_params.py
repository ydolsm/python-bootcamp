from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        "index_variable.html",
        title="Template App",
        message="Template Demo Page",
        additional_message="Template used",
    )

app.run()