def maxvalue(dic):
    winner=""
    max=0
    for i in dic:
        ba=dic[i]
        if ba>max:
            max=ba
            winner=i


bids = {}
continue_bidding=True
while continue_bidding:
    name=input("Enter your name: ")
    price=int(input("Enter your price: "))
    bids[name]=price
    should_continue = input("Do you want to continue? (y/n): ")
    if should_continue=='n':
        continue_bidding=False
        maxvalue(bids)
    elif continue_bidding=='y':
        print("\n"*20)





