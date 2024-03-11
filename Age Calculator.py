import datetime


def agecalculator(y, m, d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days / 365.25)
    print(age)


year = int(input("enter year:"))
month = int(input("enter month:"))
day = int(input("enter day:"))
agecalculator(year, month, day)
