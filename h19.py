import json


with open('failid/books.json', 'r', encoding='utf-8') as file:
    jason = json.load(file)


for tulem in tulemused:
    print(tulem)