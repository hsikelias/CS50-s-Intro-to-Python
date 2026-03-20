# X/Y    X = non-negative      Y = positive
# output the percentage, if percentage 1% or less, output E
# if percentage 99% or more, output F
# if x and y not integer, x > y, y = 0, prompt again

def main():
    fraction = input("Fraction (X/Y): ")
    verify_input(fraction)

def verify_input(fraction):
    """ verifies if the entered input is in x /y format and if x and y are integers"""

    if fraction.count("/") == 1:
        split_fraction = fraction.split('/') # [5,6]
        x, y = split_fraction # [x ="5", y = "6"]

        if len(split_fraction) == 2:
            try:
                int_x = int(x)
                int_y = int(y)

                if int_x < 0 or int_y < 0:
                    main()
                    raise ValueError

                fraction_answer(int_x, int_y)
            except ValueError:
                print("Follow the proper format")
                main()
        else:
            print("Follow the proper format")
            main()
            raise ValueError

    else:
        print("Enter proper format again")
        main()

def fraction_answer(x,y):
    ''''''
    if x < y or x == y:
        percent_dec = round(x / y, 2) * 100
        percent = int(percent_dec)

        if percent==25.0 or percent==50.0 or percent == 75.0:
            get_percentage(percent)
        elif percent >= 99.0:
            print("F")
            return "F"
        elif percent <= 1.0:
            print("E")
            return "E"
        else:
            get_percentage(percent)
    
    if y == 0:
        print("y can't be 0")
        main()
        raise ZeroDivisionError
    if x > y:
        print("X is greater than Y, X should be smaller than Y")
        main()
   #  elif y == 0:
     #   print("Y can't be 0, try again")
      #  main()


def get_percentage(answer):
    ''''''
    print(f"{(answer)}%")

main()


# Tests
'''
input of -1/4 results in reprompt, needs to reject
'''