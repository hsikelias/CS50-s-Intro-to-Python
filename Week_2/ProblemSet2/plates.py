# requesting license plate, valid plate only if all the requirements are meet:
'''
- plates must start with at least two letters
- maximum 6 characters minimum 2 characters
- numbers MUST come at the end of plate
- periods, spaces other punctuation mark not allowed
'''
# go through instructions and output if plate is valid or invalid
alphabets = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...    
    if not does_start_with_two_leters(s):
        return False
    if not vanity_plate_length(s):
        return False
    if not numbers_in_end(s):
        return False
    if not no_space_no_period(s):
        return False
    
    return True

def does_start_with_two_leters():
    '''
    Checks if the entered string is starting with at least two letters. Returns True if the word does start with two letters and false if not
    '''

def vanity_plate_length():
    '''
    Checks if the vanity plate lenght meets the min and max length requirement. Returns True if the word meets the requirement and false if not
    '''

def numbers_in_end():
    '''
    Checks if numbers come at the end, anything after that should be a number as well. AAA222 is fine but AAA22A isn't. and first number used cannot be a 0 
    '''

def no_space_no_period():
    '''
    Checks for any space/period and other fancy stuff in the plate. Returns False if there is space or any punctuation marks, returns True if there isn't any punctuation marks. 
    '''



main()