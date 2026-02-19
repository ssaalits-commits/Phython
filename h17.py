# Pangakonto – pangakonto.txt
# Sinu ülesandeks on kirjutada Pythoni skript, mis loeb andmeid failist pangakonto.txt. Fail sisaldab eraldi ridadel pangatehingute summasid: positiivsed summad tähistavad sissetulekuid ja negatiivsed summad väljaminekuid. Skript peab arvutama ja väljastama:
# kogu tehingute arvu
# positiivsete tehingute arvu
# positiivsete tehingute kogusumma
# Tulemused tuleb väljastada konsooli
with open("pangakonto.txt") as fail:
    for rida in fail:
        print(rida.strip()) 