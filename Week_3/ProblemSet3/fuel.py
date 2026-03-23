# X/Y    X = non-negative      Y = positive
# output the percentage, if percentage 1% or less, output E
# if percentage 99% or more, output F
# if x and y not integer, x > y, y = 0, prompt again

def main():
    fraction = input("Fraction (X/Y): ")
    verify_input(fraction)

def verify_input(fraction):

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


def get_percentage(answer):
    ''''''
    print(f"{(answer)}%")

main()

'''
Mistakes in my method:

1. too much use of recursions, main() is called so many times to reprompt.. USE WHILE LOOP
2. in many places I called main() and then raised a valueError or anything.. but main() moves the program to the function.. so the exceptions are never raised.
3. unecessary checks on some functions that make no sense to be there.
'''