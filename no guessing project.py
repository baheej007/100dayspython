import random
x=random.randint(1,100)
u=str(input("Choose your difficulty lavel (easy>e and hard>h): "))
if u=="e":
    c=10
elif u=="h":
    c=5
else:
    print("Invalid choice")

shouldguess=True
while shouldguess and c>0:
        print(f"You have {c} chance only")
        ug=int(input("Guess a number between 1 and 100: "))
        if ug==x:
            print("YOU WIN")
            print(f"YES {x}")
            shouldguess=False
        elif ug>x:
            c-=1
            if abs(ug-x)>20:
                print("Too high")
            else:
                print("high")
        else:
            c-=1
            if abs(ug-x)>20:
                print("Too low")
            else:
                print("low")
if c<1:
    print("YOU LOSE")
    print(f"NO IS {x}")