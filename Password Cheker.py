# ------------------- Variable ---------------------#

password = input("enter your password : ")
lowercase_letter = [c for c in password if c.islower()]
spec = ["~", "`", "!", "@", "#", "$", "$", "%", "^", "&", "*", "(", ")"]
uppercase_letter = [c for c in password if c.isupper()]
isnum = [c for c in password if c.isalnum()]
category = ""
point = 0
count = 0

# ------------------- for ---------------------#

for char in password:
    if char in spec:
        count += 1


# ------------------- if ---------------------#

if len(password) < 8:
    print("pleas enter good password")
    category = "weak"
elif len(password) >= 8 and len(password) < 12:
    result = point + 8 + (len(password) * 6)
    point = result
    category = "medium"
    if len(lowercase_letter) == 1:
        s = point + 6
        point = s
    elif len(lowercase_letter) == 2:
        s = point + 12
        point = s
    else:
        s = point + 18
        point = s
    if len(isnum) == 1:
        s = point + 6
        point = s
    elif len(isnum) == 2:
        s = point + 12
        point = s
    else:
        s = point + 18
        point = s
    if len(uppercase_letter) == 1:
        s = point + 6
        point = s
    elif len(uppercase_letter) == 2:
        s = point + 12
        point = s
    else:
        s = point + 18
        point = s
    if count == 1:
        s = point + 6
        point = s
    elif count == 2:
        s = point + 12
        point = s
    else:
        s = point + 18
        point = s
else:
    result = point + 16
    point = result
    category = "strong"
    if len(lowercase_letter) == 1:
        s = point + 7
        point = s
    elif len(lowercase_letter) == 2:
        s = point + 14
        point = s
    else:
        s = point + 21
        point = s
    if len(isnum) == 1:
        s = point + 7
        point = s
    elif len(isnum) == 2:
        s = point + 14
        point = s
    else:
        s = point + 21
        point = s
    if len(uppercase_letter) == 1:
        s = point + 7
        point = s
    elif len(uppercase_letter) == 2:
        s = point + 14
        point = s
    else:
        s = point + 21
        point = s
    if count == 1:
        s = point + 7
        point = s
    elif count == 2:
        s = point + 14
        point = s
    else:
        s = point + 21
        point = s

# ------------------- OutPut ---------------------#

print(f"your password is : {password}\npassword category : {category}\npoint : {point}")
