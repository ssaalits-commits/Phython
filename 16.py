mitu= int(input("Mitu kataloogi tahad: "))
today = str(date.today())
try:
    os.mkdir(today)
except FileExistorError:
    print(f"kataloog{today} juba eksisteerib.")
    kustuta= (input(f"millist kataloogi kustutdd1-/{mitu}: "))
    
if os.path.isdir(f"{today/{kustuta}"):
        os.rmdir(f"{today/{kustuta}")
        print(f"kustutatud kataloog{today/{kustuta}")
else:
    print(f"selline kataloog puudub: {today}/{kustuta}")

kausta_tee = osgetcwd()+"/"+today
print(os.listdir(kasuta_tee))