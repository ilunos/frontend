from flask import render_template
from app import app
import requests
from requests.auth import HTTPBasicAuth
import json

@app.route('/')
@app.route('/index')
def index():
    response = requests.get("http://localhost:9000/",auth=HTTPBasicAuth('admin', 'admin'))

    decoded = json.loads(response.content.decode())

    return render_template('index.html', title='Home', data=decoded)