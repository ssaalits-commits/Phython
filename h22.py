
import csv
# Autorent
# Kasuta seda faili: rentals.csv


# Rendite arv – leia mitu ronditehingut on tehtud


# Unikaalsed kliendid ja keskmine vanus – arvutage, mitu unikaalset klienti (customer ID) andmetes esineb ja mis on teie klientide keskmine vanus


# Tagastamine – milline osakaal broneeringutest hõlmab risti-kontori rentimist, kus klient võtab auto ühest kohast ja tagastab selle teise kontorisse?


# Keskmine rentimise kestus – mis on keskmine rentimise kestus?


rentid_arv = 0
faili_nimi= 'rentals.csv'
with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)

























# # Lihtne kuupäev
# import datetime
# # Kuva praegune päev, kuu, aasta, tund, minut
# kp = datetime.datetime.now()
# print(kp)
# # Vorminda praegune kuupäev järgmiselt: d.m Y,  H:M:S
# print(kp.strftime("%d.%m %Y,  %H:%M:%S"))

# # Lisa oma sünniaeg, arvuta ja kuva, mitu päeva vana oled
# sp = datetime.datetime(2008, 7, 16)
# vanus_paevades = kp - sp
# print(f"vanus_paevades {vanus_paevades.days}")
# # Kuva vanus aastates
# vanus_aastates = vanus_paevades.days // 365
# print(f"vanus_aastates {vanus_aastates}")
# # Kuva, kas tegemist on juubeliaastaga
# if vanus_aastates%5 == 0:
#     print("juubel")
# else:
#     print("apache helikopter")

