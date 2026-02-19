
print("")
autode_hind = 0
autode_hind_kokku=0



ev_data = [
    ['vehicle', 'range', 'price'],
    ['Tesla Model Y Long Range', '330', '58990'],
    ['Volkswagen ID.4 Pro', '260', '39995'],
    ['Ford Mustang Mach-E', '300', '42995'],
    ['Audi e-tron GT', '238', '102700'],
    ['Nissan Leaf', '149', '27400'],
    ['BMW iX xDrive50', '324', '83995'],
    ['Polestar 2', '265', '45500'],
    ['Kia EV6 Long Range', '310', '47795'],
    ['Mercedes-Benz EQS 450+', '350', '102310'],
    ['Hyundai Kona Electric', '258', '37400']
]



for i in ev_data:
    print(f"{i[0]:26} {i[1]:6} {i[2]:8}")
    
for i in range(1,len(ev_data)):
    autode_hind+=int(ev_data[i][2])
    autode_hind_kokku+=1

print(f"Keskmine hind: {autode_hind/autode_hind_kokku}")











