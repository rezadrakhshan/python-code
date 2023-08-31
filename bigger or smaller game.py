import random


print("----welcome to this game----")

point = 60
num1 = random.randint(1,10)
print(num1)


for i in range(10):
    num2 = random.randint(1,10)
    choices = input("the next number is bigger than pervius number or no?")
    if point <= 0:
        print("you lose")
        break
    if choices == "yes" and num2 > num1:
        result = point + 15
        point = result
        num1 = num2
        print(f"win\nnumber2:{num2}\npoint:{point}")
    else:
        result = point - 15
        point = result
        num1 = num2
        print(f'lose\nnumber2:{num2}\npoint:{point}')