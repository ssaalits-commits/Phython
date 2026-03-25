 # Ülessanne 11
import turtle
import random


def pikim_sona(list):
    pikimArv = 0
    pikimNimi = ""
    for i in list:
        if len(i) > pikimArv:
            nime_pikkus =len(i)
            pikimNimi = i 
    return pikimNimi
nimed = ["Sergei", "Marek", "Andrus","AL", "ya lublu Anastasiiju"]



def kolm_pikimat_nime(list):
    pikimad = ["Sergei", "Marek", "Andrus"]
    if len(list)>2:
        list.sort(key=len, reverse= True)
        return list[0:3]
    else:
        return "list on liiga lühike"
    
def ruut(a):
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)


for _ in range(100):
    turtle.speed(0)
    ruut(100)
    turtle.penup()
    turtle.goto(random.randint (-400,200),random.randint (-400,200))
    turtle.pendown()
    
print(kolm_pikimat_nime(nimed))
print(pikim_sona(nimed))








turtle.done()