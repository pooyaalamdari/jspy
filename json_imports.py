import json

file = open('friends_json.txt', 'r')

#reads file and turn it to dictiobary
file_contents = json.load(file)

file.close()

print(file_contents['friends'][0])
