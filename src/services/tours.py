import random

import data.tours as tours_data


def get_random_tours(count):
    tours = tours_data.tours
    random_tours = {}
    tours_length = len(tours)

    while True:
        if len(random_tours) == count:
            break

        random_tour_id = random.randrange(1, tours_length)
        existed_item = random_tours.get(random_tour_id)

        if existed_item is not None:
            continue

        random_tours[random_tour_id] = tours[random_tour_id]

    return random_tours


def get_tours_by_departure(departure):
    tours = {}

    for id, tour in tours_data.tours.items():
        if tour.get('departure') != departure:
            continue

        tours[id] = tour
    return tours


def get_tour_by_departure_and_id(departure, tour_id):
    tours = get_tours_by_departure(departure)

    for id, tour in tours.items():
        if int(tour_id) == int(id):
            return tour
