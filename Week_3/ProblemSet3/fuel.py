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
        x, y = split_fraction # [x = 5, y = 6]
        int_x = int(x)
        int_y = int(y)


        if len(split_fraction) == 2 and x.isdigit() and y.isdigit():
            fraction_answer(int_x, int_y)
        else:
            raise ValueError
            main()

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

    elif x > y:
        print("X is greater than Y, X should be smaller than Y")
        main()
    elif y == 0:
        print("Y can't be 0, try again")
        main()


def get_percentage(answer):
    ''''''
    print(f"{(answer)}%")

main()


# Tests
'''
:) input of 3/4 yields output of 75%
:) input of 1/3 yields output of 33%
:) input of 2/3 yields output of 67%
:( input of 0/100 yields output of E
    expected: "E"
    actual:   ""
:( input of 1/100 yields output of E
    expected: "E"
    actual:   ""
:( input of 100/100 yields output of F
    expected: "F"
    actual:   ""
:( input of 99/100 yields output of F
    expected: "F"
    actual:   ""
:) input of 100/0 results in reprompt
:) input of 10/3 results in reprompt
:( input of three/four results in reprompt
    expected program to reject input, but it did not
:( input of 1.5/4 results in reprompt
    expected program to reject input, but it did not
:( input of 3/5.5 results in reprompt
    expected program to reject input, but it did not
:) input of 5-10 results in reprompt
:) input of -1/4 results in reprompt

'''