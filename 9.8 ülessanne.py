#9.8
import random
for i in range(11):
    print(f"{i} * {i}= {i*i}")
    
#9.9
import random
tehe= ("*","+","-","/")
punktid =0
kysimuste_arv=10
for _ in range (10):
    arv1 = random.randint(1,10)
    arv2 = random.randint(1,10)
    t =random.choice(tehe)
    
if t=="+":
    print(f"{arv1} {t}{arv2}=")
    v= int (input("Vastus: "))
    if arv1+arv2 ==v :
        punktid+=1
elif t=="-":
    print(f"{arv1} {t}{arv2}={arv1 + arv2}")
    v= int (input("Vastus: "))
    if arv1-arv2 ==v :
        punktid+=1
elif t=="*":
    print(f"{arv1} {t}{arv2}={arv1 + arv2}")
    v= int (input("Vastus: "))
    if arv1*arv2 ==v :
        punktid+=1
elif t=="/":
    print(f"{arv1} {t}{arv2}={arv1 + arv2}")
    v= float(input("Vastus: "))
    if round(arv1/arv2,1) ==v :
        punktid+=1
if kysimuste_arv/punktid >=0.5:
    print("A")

else:
    print("MA")






        