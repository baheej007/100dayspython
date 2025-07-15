import random



def dealcard():
     cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
     card=random.choice(cards)
     return card

usercard=[]
comcard=[]
is_game_over=False

for _ in range(2):
     usercard.append(dealcard())
     comcard.append(dealcard())
     print(f"your card: {usercard} , user score:{userscore}")
     print(f"computer card: {comcard[0]}")

def score(cards):
     if sum(cards)==21 and len(cards)==2:
          return 0
     if 11 in cards and sum(cards)>21:
          cards.remove(11)
          cards.append(1)
     return sum(cards)

userscore=score(usercard)
comscore=score(comcard)
