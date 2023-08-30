import random
print("Welcome to Number hunch Game")

ready = input("are you ready?")

point = 60
print("your pint is 60")
mylist=[]

for i in range(10):
    number = random.randint(1,10)
    choose = input("enter a number:")
    if choose == number:
        result = point + 15
        point = result
        print(f"you win\npoint:{result}")
    if 0 >= point:
        print("you lose")
        break
    else:
        result = point - 15
        point = result
        print(f"you lose\npoint:{result}")
