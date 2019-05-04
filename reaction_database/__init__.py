from flask import Flask, jsonify
from .database import get_top_reactions

app = Flask(__name__)

@app.route('/top/<field>/<of>')
def top(field, of):
    return jsonify(list(get_top_reactions(field, of)))