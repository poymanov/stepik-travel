from flask import Flask
from flask import render_template

import services.tours as tours_service

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', tours=tours_service.get_random_tours(6))


@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html')


@app.route('/from/<direction>/')
def direction(direction):
    return render_template('direction.html')
