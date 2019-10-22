import json

with open("data_sets/to-bike.json") as dataset:
    js = json.load(dataset)

# Calcolo tutte le stazioni online

# Calcolo tutte le free bikes e gli empty slot
stations = js['network']['stations']

online_stations = free_bikes = empty_slots = 0
for station in stations:
    if station['extra']['status'].lower() == "online":
        online_stations += 1

    free_bikes += station['free_bikes']
    empty_slots += station['empty_slots']

print(f"online stations: {online_stations}")
print(f"free bikes: {free_bikes}")
print(f"empty slots: {empty_slots}")