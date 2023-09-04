import time

my_time = int(input("enter time per second: "))


for i in reversed(range(0, my_time)):
    print(i)
    time.sleep(1)

print("Time is Up")