# bottle of coke for 50 cents only if coins given are 25 cent, 10 cents, 5 cents.
# make a program that repeats asking the user to enter amount until it hits atleast 50
# finally display the charge. If user enters anything else dont do anything to charge due
#  
amount_due = 50

while amount_due != 0:
    print(f"Amount Due: {amount_due}")
    user_cash = int(input("Insert Coin: "))

    match user_cash:
        case 5 | 10 | 25:
            amount_due = amount_due - user_cash
            print((f"Change Owed: {50 - amount_due}"))
        case _:
            amount_due 