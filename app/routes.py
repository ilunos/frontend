from flask import render_template
from app import app
import requests
from requests.auth import HTTPBasicAuth
import json
import yaml

with open("app/config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

@app.route('/')
@app.route('/index')
def index():
    response = requests.get('http://' + cfg['docker-agent']['host'] + ':' +cfg['docker-agent']['port'].__str__(),auth=HTTPBasicAuth('admin', 'admin'))

    decoded = json.loads(response.content.decode())

    return render_template('index.html', title='Home', data=decoded)