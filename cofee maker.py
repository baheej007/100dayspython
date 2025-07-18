menulist={
         "water": 500,
         "milk": 200,
         "coffee": 100
         }
def coffee_maker():
    print("type report to give available resources ")
    u=input("what would you like (espresso/latte/cappuccino): ")
    if u=="report":
        for i in menulist:
            print(f"{i}={menulist[i]}")
        coffee_maker()
    elif u=="espresso" or u=="latte" or u=="cappuccino":
        print("How much you have")
        qu = int(input("quarters($0.25): "))
        di = int(input("dimes($0.10): "))
        ni = int(input("nickels($0.05): "))
        pe = int(input("penis($0.01): "))
        cost = qu * 0.25 + di * 0.10 + ni * 0.05 + pe * 0.01
        print(f"you have {cost}$")
        if u=="espresso":
             cost-=1.5
             menulist["water"]-=50
             menulist["coffee"]-=18
             print("YOUR DRINK IS HERE")
             coffee_maker()
        elif u=="latte":
            cost-=2.5
            menulist["water"] -= 200
            menulist["milk"] -= 158
            menulist["coffee"] -= 24
            print("YOUR DRINK IS HERE")
            coffee_maker()
        elif u=="cappuccino":
            cost-=3.0
            menulist["water"] -= 200
            menulist["milk"] -= 100
            menulist["coffee"] -= 54
            print("YOUR DRINK IS HERE")
            coffee_maker()

coffee_maker()


