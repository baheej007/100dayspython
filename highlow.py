import random
from hldata import celebrities
from hlpic import vs


sc=0
cont=True
while cont:
    print(f"SCORE : {sc}")
    x = celebrities[random.randint(0, len(celebrities) - 1)]
    cfory = [i for i in celebrities if i["name"] != x["name"]]
    y = cfory[random.randint(0, len(cfory) - 1)]
    print(x["name"],x["about"],x["country"])
    print(vs)
    print(y["name"], y["about"], y["country"])
    print("\n"*11)
    u=int(input("choose first or second (1 or 2): "))
    if u==1:
        if x["followers"]>y["followers"]:
            print("\n" * 200)
            sc+=1
            cont=True
        else:
            print("YOU FAIL")
            cont=False
    elif u==2:
        if x["followers"] < y["followers"]:
            print("\n"*200)
            sc += 1
            cont = True
        else:
            print("YOU FAIL")
            cont=False

print(f"YOUR SCORE : {sc}")



