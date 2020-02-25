from flask import Flask, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    print(url_for('static', filename='icon.png'))
    return app.send_static_file('icon.png')