import json

with open('friends_json.txt', 'r') as file:
    file_content = json.load(file)

print(file_content['friends'][0]['name'])


cars = [
    {'make': 'ford', 'model': 'Fiesta'},
    {'make': 'ford', 'model': 'Focus'}
]

with open('cars_json.txt', 'w') as car_file:
    json.dump(cars, car_file)

my_json_string = '[{"name": "Alfa Alfa", "Releases":1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
