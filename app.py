from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "HOME"


@app.route('/github', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'application/json':
        my_info = json.dumps(request.json)
        return my_info
