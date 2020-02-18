import data.departures as departures_data
import services.tours as tours_services


def get_all_departures():
    return departures_data.departures


def get_departure_from_title(departure):
    return departures_data.departures.get(departure)


def get_departure_info(departure):
    tours = tours_services.get_tours_by_departure(departure).values()
    return {
        'min_price': min(tours, key=lambda x: x.get('price')).get('price'),
        'max_price': max(tours, key=lambda x: x.get('price')).get('price'),
        'min_nights': min(tours, key=lambda x: x.get('nights')).get('nights'),
        'max_nights': max(tours, key=lambda x: x.get('nights')).get('nights'),
    }
