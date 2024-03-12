import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print("hashed password :" + hashed_password)

text = input("enter your password : ")
hash_password(text)

