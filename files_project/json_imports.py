import json

file = open('friends_json.txt', 'r')
file_content = json.load(file)
file.close()
print(file_content['friends'][0]['name'])


cars = [
    {'make': 'ford', 'model': 'Fiesta'},
    {'make': 'ford', 'model': 'Focus'}
]

car_file = open('cars_json.txt', 'w')
json.dump(cars, car_file)
car_file.close();


my_json_string = '[{"name": "Alfa Alfa", "Releases":1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
