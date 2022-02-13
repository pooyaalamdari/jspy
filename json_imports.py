import json

file = open('friends_json.txt', 'r')

#reads file and turn it to dictiobary
file_contents = json.load(file)

file.close()

print(file_contents['friends'][0])


#convert python dictionary to json file

cars = [
    {'make':'Ford', 'model':'Fiesta'},
    {'make':'Ford', 'model':'Focus'}
]

file = open('cars_json.txt', 'w')
#build file and it's name is cars_json.txt
json.dump(cars, file)
file.close()

#after run the json file will be created in the cars_json.txt
