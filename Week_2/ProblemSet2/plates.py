# requesting license plate but one of the requirements should meet:
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
    if len(s) >=2 and len(s) <=6:
        print("Valid")
    elif 
main()