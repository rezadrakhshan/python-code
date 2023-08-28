import random
import string
print("""
----enter type of password----
1-String
2-Integer
3-Both
""")
type = int(input("enter your choice(1/2/3):"))

if type == 2:
    S = 10
    ran = ''.join(random.choices(string.digits, k = S))
    print(ran)
if type ==1:
    S = 10
    ran = ''.join(random.choices(string.ascii_uppercase  , k = S)) 
    print("your password is :" + str(ran))
if type == 3:
    S = 10
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    print(ran)
    