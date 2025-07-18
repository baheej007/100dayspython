import random
import maths
def mut(l1):
    l2=[]
    new=0
    for i in l1:
        new=i*2
        new+=random.randint(1,3)
        new=maths.add(new,i)
    l2.append(new)
    print(l2)

mut([1,2,3,4,5])