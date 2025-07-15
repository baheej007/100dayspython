# def opera():
#     x = int(input("Enter your first no: "))
#     y = str(input("Select operation(+,-,*,/): "))
#     z = int(input("Enter next no: "))
#     if y=="+":
#         return x+z
#     elif y=="-":
#         return x-z
#     elif y=="*":
#         return x*z
#     elif y=="/":
#         return x/z
#     else:
#         return "Invalid input"
# k=opera()
# print(f"ANSWER: {k}")
# cont=input("Do you want to continue? (y/n): ")
# while cont=="y":
#
#     print(opera())
# else:
#     print("Goodbye!")


def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

oper={
      "+":add,
      "-":substract,
      "*":multiply,
      "/":divide
     }

# print(oper["+"](2,3))
# print(oper["-"](4,3))
# print(oper["*"](5,3))
# print(oper["/"](6,3))
#
# def calc():
#         repeat=True
#         x = float(input("Enter your first no: "))
#         while repeat:
#                 y = str(input("Select operation(+,-,*,/): "))
#                 z = float(input("Enter your second no: "))
#
#                 ans=(oper[y](x,z))
#                 print(f"{x}{y}{z}={ans}")
#
#                 choice=input(f"Press y to continue with {ans} or n to new operation: ")
#                 if choice=="y":
#                     x=ans
#                 else:
#                     repeat=False
#                     print("\n"*2)
#                     calc()
# calc()





















