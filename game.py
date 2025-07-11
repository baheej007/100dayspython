print("Welcome to this game.Go and find the tressure")
x=input('Choose "Left" or "Right" : ')
if x=="Right":
    print("Game over.There is no way to go")
elif x=="Left":
    print("Wow go to next.There is river")
    y=input("'Swim' or 'Wait' : ")
    if y=="Swim":
        print("Game over .There is a Crocodile")
    elif y=="Wait":
        print("Nice decision.There is 3 Doors.")
        z=input("Choose 'Red' or 'Green' or 'Blue' : ")
        if z=='Red':
            print("Game over Wrong door")
        elif z=='Green':
            print("Game over Wrong door")
        elif z=='Blue':
            print("Wow congradulations.You won\n")

