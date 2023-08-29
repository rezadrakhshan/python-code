from time import gmtime, strftime

def ATM():
    password = input("enter your password:")
    time = strftime("%a, %d %b %Y %H:%M:%S ", gmtime())
    print("""
    1-transfer cash
    2-gift card
    3-withdraw money
    4-by charge
    """)
    userchoice = int(input("enter your choice:"))
    if userchoice == 1:
        account_numebr = int(input("enter your account numebr:"))
        account_numebr2 = int(input("enter destination account number:"))
        print("""
        1-5$
        2-10$
        3-20$
        4-40$
        5-50$
        """)
        userchoice2 = input("enter amount:(like=20$)")
            
        if userchoice2 == "5$":
            print(f"account number : {account_numebr}\ndestination account numebr : {account_numebr2}\namount : {userchoice2}\ntime : {time}\nBOZORGATM")  
        if userchoice2 == "10$":
                print(f"account number : {account_numebr}\ndestination account numebr : {account_numebr2}\namount : {userchoice2}\ntime : {time}\nBOZORGATM") 
        if userchoice2 == "20$":
            print(f"account number : {account_numebr}\ndestination account numebr : {account_numebr2}\namount : {userchoice2}\ntime : {time}\nBOZORGATM") 
        if userchoice2 == "40$":
            print(f"account number : {account_numebr}\ndestination account numebr : {account_numebr2}\namount : {userchoice2}\ntime : {time}\nBOZORGATM") 
        if userchoice2 == "50$":
            print(f"account number : {account_numebr}\ndestination account numebr : {account_numebr2}\namount : {userchoice2}\ntime : {time}\nBOZORGATM") 
    if userchoice == 2:
        print("""
        1-birthday gift
        2-baby gift
        3-New house gift
        4-wedding gift
        """)
        input1 = input("choose card type:(string)")
        if input1 == "birthday gift":
            print("""
            1-5$
            2-10$
            3-20$
            4-40$
            5-50$
            """)
            input2 = input("choose amount:(like=10$)")
            if userchoice2 == "5$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")

            if userchoice2 == "10$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if userchoice2 == "20$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if userchoice2 == "40$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if userchoice2 == "50$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
        if input1 == "baby gift":
            print("""
            1-5$
            2-10$
            3-20$
            4-40$
            5-50$
            """)
            input2 = input("choose amount:")
            if input2 == "5$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "10$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "20$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "40$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "50$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
        if input1 == "New house gift":
            print("""
            1-5$
            2-10$
            3-20$
            4-40$
            5-50$
            """)
            input2 = input("choose amount:")
            if input2 == "5$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "10$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "20$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "40$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "50$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
        if input1 == "wedding gift":
            print("""
            1-5$
            2-10$
            3-20$
            4-40$
            5-50$
            """)
            input2 = input("choose amount:")
            if input2 == "5$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "10$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "20$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "40$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
            if input2 == "50$":
                input3 = input("enter text:")
                print(f"Card type : {input1}\namount : {input2}\ntext : {input3}\ntime : {time}\nBOZORGATM")
    if userchoice == 3:
        print("""
        1-5$
        2-10$
        3-20$
        4-40$
        5-50$
        6-i bring in
        """)
        amount = input("enter amount:(like=50$)")
        if amount == "5$":
            print(f"amount : {amount}\ntime : {time}\nBOZORGATM")
        if amount == "10$":
            print(f"amount : {amount}\ntime : {time}\nBOZORGATM")
        if amount == "20$":
            print(f"amount : {amount}\ntime : {time}\nBOZORGATM")
        if amount == "40$":
            print(f"amount : {amount}\ntime : {time}\nBOZORGATM")
        if amount == "50$":
            print(f"amount : {amount}\ntime : {time}\nBOZORGATM")
        if amount == "i bring in":
            price = input("enter amount(max=200$)")
            print(f"amount : {price}\ntime : {time}\nBOZORGATM")
    if userchoice == 4:
        print("""
        1-by charge
        2-transfer charge
        """)
        user_choice = int(input("enter your choice:(int)"))
        if user_choice == 1:
            numebr = int(input("enetr your number:"))
            charge = int(input("enter  the amount of charge you want:"))
            print(f"numebr : {numebr}\ncharge : {charge}\ntime : {time}\nBOZORGATM")
        if user_choice == 2:
            origin_number = int(input("enter origin numeber:"))
            destination_number = int(input("enter destination numeber:"))
            charge = int(input("enter  the amount of charge you want:"))
            print(f"origin number : {origin_number}\ndestination number : {destination_number}\ncharge : {charge}\ntime : {time}\nBOZORGATM")
ATM()
for i in range(1000):
    mm = input("do you have another transaction?(yes|no)")
    if mm == "yes":
        ATM()
    else:
        print("thank you for use BOZORGATM")
        break
