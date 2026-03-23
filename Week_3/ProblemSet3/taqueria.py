"""
user placing an order,add total price till user ctrl ds.. after use enters an item
output the total price so far, prefixed with $ sign and formatted two decimals
"""

# end of file error: handles when user enters ctrld or ctrlc

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total = 0


def main():
    """ask user to enter item and checks if theres a EOF error
    print("-*-*-*MENU LIST*-*-*-\n")
    for dic_item, dic_price in menu.items():
        print(f"{dic_item}: {dic_price}")
    print("-*-*-*-*-*-*-*-*-*-*-")"""

    while True:
        try:
            item = input("Item: ")
            return item_check(item.title())

        except EOFError:
            print("Thanks for using our service!")
            break


def item_check(order_item):

    global total

    if order_item in menu:
        order_price = menu[order_item]
        total += order_price

        print(f"Total: ${total}")
    else:
        main()


main()

