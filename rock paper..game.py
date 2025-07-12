r='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
p='''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
s='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
x=int(input("Choose rock,paper or scissor(0,1,2 respectively): "))
y=random.choice([0,1,2])
if x==0:
    if y==0:
        print("Tie\ncomputer choose\n"+r+"\nyou choose\n"+r)
    elif y==1:
        print("Fail\ncomputer choose\n"+p+"\nyou choose\n"+r)
    else:
        print("Win\ncomputer choose\n"+s+"\nyou choose\n"+r)
elif x==1:
    if y==0:
        print("Win\ncomputer choose\n"+r+"\nyou choose\n"+p)
    elif y==1:
        print("Tie\ncomputer choose\n"+p+"\nyou choose\n"+p)
    else:
        print("Fail\ncomputer choose\n"+s+"\nyou choose\n"+p)
elif x==2:
    if y==0:
        print("Fail\ncomputer choose\n"+r+"\nyou choose\n"+s)
    elif y==1:
        print("Win\ncomputer choose\n"+p+"\nyou choose\n"+s)
    else:
        print("Tie\ncomputer choose\n"+s+"\nyou choose\n"+s)
else:
    print("Invalid input")
