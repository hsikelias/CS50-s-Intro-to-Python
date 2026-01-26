import string

numbers = ["1","2","3","4","5","6","7","8","9"]
alphabets =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def main():
    plate = input("Plate: ")
    is_valid(plate)

def is_valid(s):
    if does_start_with_two_letters(s) and vanity_plate_length(s) and no_space_no_period(s) and numbers_in_end(s):
        print("Valid")
    else:
        print("Invalid")

def does_start_with_two_letters(s):
    if len(s) >= 2:
        first_word = s[0]
        second_word = s[1]
    else:
        return False

    if first_word in alphabets and second_word in alphabets:
        return True
    else:
        return False

def vanity_plate_length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def numbers_in_end(s):
    digit_started = False
    for char in s:
        if char.isdigit():
            if not digit_started:
                if char == "0":
                    return False
                digit_started = True
        else:
            if digit_started:
                return False
    return True

def no_space_no_period(s):
    for char in s:
        if char in string.punctuation:
            return False
    return True

main()