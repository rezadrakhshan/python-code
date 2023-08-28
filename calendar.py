import calendar

year = int(input("enter year:"))
month = int(input("enter month:"))

page = calendar.month(year, month)
print(page)