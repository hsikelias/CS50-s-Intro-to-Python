# requesting license plate, valid plate only if all the requirements are meet:
import string


'''
- plates must start with at least two letters
- maximum 6 characters minimum 2 characters
- numbers MUST come at the end of plate, first number cant be 0
- periods, spaces other punctuation mark not allowed
'''
# go through instructions and output if plate is valid or invalid

numbers = ["0","1","2","3","4","5","6","7","8","9"]
alphabets = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def main():
    plate = input("Plate: ")
    is_valid(plate)

def is_valid(s):
    '''
    Basically takes all the trues and falses from different functins and uses them to determine wether the plate is valid or not. 
   '''
    if does_start_with_two_letters(s) == True and vanity_plate_length(s) == True and no_space_no_period(s) == True and numbers_in_end(s) == True:
        print("Valid")
    else:
        print("Invalid")

def does_start_with_two_letters(s):
    '''
    Checks if the entered string is starting with at least two letters. Returns True if the word does start with two letters and false if not
    '''
    # take 0,1 index of the word and check if those are in the alphabets

    first_word = s[0]
    second_word = s[1]

    if first_word in alphabets and second_word in alphabets:
        return True
    else:
        return False

def vanity_plate_length(s):
    '''
    Checks if the vanity plate length meets the min and max length requirement. Returns True if the word meets the requirement and false if not
    '''
    if 2 <= len(s) <= 6: 
        return True
    else:
        return False

def numbers_in_end(s):
   '''
   Checks if numbers come at the end, anything after that should be a number as well. AAA222 is fine but AAA22A isn't. and first number used cannot be a 0 
   '''
   found_first_digit = False

def no_space_no_period(s):
    '''
    Checks for any space/period and other fancy stuff in the plate. Returns False if there is space or any punctuation marks, returns True if there isn't any punctuation marks. 
    '''
    for char in s:
        if char in string.punctuation:
            return False
    return True 
main()
