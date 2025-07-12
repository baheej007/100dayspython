import random
letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=",
"{", "}", "[", "]", ":", ";", "'", "<", ">", ",", ".", "?", "/","|", "~", "`",]

# x=int(input("length of password: "))
# y=int(input("How many symbols in password: "))
# z=int(input("How many numbers in password: "))
# ls=x-(y+z)
# print(ls,y,z)
# password=""
# for i in range(0,ls):
#     password=password+str(random.choice(letters))
# for i in range(0,y):
#     password=password+str(random.choice(symbols))
# for i in range(0,ls):
#     password=password+str(random.choice(numbers))
# print(password)


x=int(input("length of password: "))
y=int(input("How many symbols in password: "))
z=int(input("How many numbers in password: "))
ls=x-(y+z)
print(ls,y,z)
password=[]
pstr=""
for i in range(0,ls):
    password.append(str(random.choice(letters)))
for i in range(0,y):
    password.append(str(random.choice(symbols)))
for i in range(0,z):
    password.append(str(random.choice(numbers)))
random.shuffle(password)
for i in password:
    pstr+=i
print(f"Your password is  :  {pstr}")