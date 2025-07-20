import random
import colorgram

rgbl=[]
colors=colorgram.extract('car.jpg',30)
for color in colors:
    rt=(color.rgb.r)
    gt=(color.rgb.g)
    bt=(color.rgb.b)
    
print(rgbl)
# cl=[]
# def ctf():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     ct = (r, g, b)
#     cl.append(ct)
#
#
# for i in range(10):
#     ctf()
#
# print(cl)