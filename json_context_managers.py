import json

with open('friends_json.txt', 'r') as file:

    #reads file and turn it to dictiobary
    file_contents = json.load(file)

print(file_contents['friends'][0])
#close the file automate



#convert python dictionary to json file

cars = [
    {'make':'Ford', 'model':'Fiesta'},
    {'make':'Ford', 'model':'Focus'}
]

with open('cars_json.txt', 'w') as file:
    #build file and it's name is cars_json.txt
    json.dump(cars, file)


#use json file in python file as string
# "" and '' difference is important in json
my_json_string = '[{"name": "Alfa Romeo"}, {"released": 1950}]'
anothe_cars = json.loads(my_json_string) #use loads NOT load
print(anothe_cars[0]['name'])
