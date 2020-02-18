from flask import Flask
from flask import render_template

import services.departures as departures_service
import services.tours as tours_service

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', tours=tours_service.get_random_tours(6))


@app.route('/from/<direction>/<id>/')
def tour(direction, id):
    from_title = departures_service.get_departure_from_title(direction)
    tour_info = tours_service.get_tour_by_departure_and_id(direction, id)
    return render_template('tour.html', from_title=from_title, tour=tour_info)


@app.route('/from/<direction>/')
def direction(direction):
    tours = tours_service.get_tours_by_departure(direction)
    from_title = departures_service.get_departure_from_title(direction)
    departure_info = departures_service.get_departure_info(direction)
    return render_template('direction.html', tours=tours, from_title=from_title, departure_info=departure_info)


@app.context_processor
def global_data():
    return dict(departures=departures_service.get_all_departures())
