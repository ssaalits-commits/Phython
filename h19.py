import json

# Kuva 12.klassi õpilaste nimekiri
# Kuva mitu õpilast õpib 10, 11 ja 12 klassis
# Kuva millistes trennides 12. klassi õpilased käivad
# Kuva 12 klassi õpilaste hinneteleht (nimi, ained, punktid)

with open('failid/tulemused.json', 'r', encoding='utf-8') as file:
    tulemused = json.load(file)



for tulem in tulemused:
    #print(tulem['klass'])
    if tulem['klass'] == "12":
        print(tulem['nimi'])