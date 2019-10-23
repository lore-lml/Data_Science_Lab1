import json, sys
from math import cos, acos, sin
from random import randint


def distance_coords(lat1, lng1, lat2, lng2):
    """Compute the distance among two points."""
    deg2rad = lambda x: x * 3.141592 / 180
    lat1, lng1, lat2, lng2 = map(deg2rad, [ lat1, lng1, lat2, lng2 ])
    R = 6378100 # Radius of the Earth, in meters
    return R * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lng1 - lng2))


if __name__ == '__main__':
    with open("data_sets/to-bike.json") as dataset:
        js = json.load(dataset)

    # Calcolo tutte le stazioni online

    # Calcolo tutte le free bikes e gli empty slot
    stations = js['network']['stations']

    online_stations = []
    free_bikes = empty_slots = 0
    for station in stations:
        if station['extra']['status'].lower() == "online":
            online_stations.append(station)
            free_bikes += station['free_bikes']
            empty_slots += station['empty_slots']

    print(f"online stations: {len(online_stations)}")
    print(f"free bikes: {free_bikes}")
    print(f"empty slots: {empty_slots}")

    chosen_index = randint(0, len(online_stations))
    fixed_latitude = stations[chosen_index]['latitude']
    fixed_longitude = stations[chosen_index]['longitude']
    distance = sys.maxsize
    closest_station = -1

    for station in stations:
        if stations[chosen_index] == station:
            continue
        current_latitude = station['latitude']
        current_longitude = station['longitude']
        current_distance = distance_coords(fixed_latitude, fixed_longitude, current_latitude, current_longitude)
        if current_distance < distance:
            closest_station = station
            distance = current_distance

    print(f"\nChoosen Station: {stations[chosen_index]['name']}")
    print(f"Closest Station: {closest_station['name']}, {distance:.2f}m")


