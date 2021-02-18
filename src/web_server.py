from flask import Flask, json, jsonify, request
from . import infix, prefix
app = Flask(__name__)


@app.route("/")
def confirmation():
    return "Server has started!"


@app.route('/infix', methods=['POST'])
def infix_handler():
    req = request.get_json()
    data = json.loads(req)
    cmd = data['cmd']
    res = str(infix.run(cmd))
    return res


@app.route('/prefix', methods=['POST'])
def prefix_handler():
    req = request.get_json()
    data = json.loads(req)
    cmd = data['cmd']
    res = str(prefix.run(cmd))
    return res
