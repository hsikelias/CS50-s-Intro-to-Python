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




1. I use Instagram a lot, I upload my own content in this app and also consume other creator's content for inspiration but sometimes I get too distracted when I'm supposed to be studying. When I notice this pattern repeating, I deliberately turn on focus mode to block apps like instagram and use a pomodoro when studying. So, I didn't find it too hard to unplug from instagram. 

2. I wasn't able to stay unplugged for the full 24 hours. In my opinion, It doesn't really matter because my goal is to stay away from these apps when I'm doing tasks like studying or programming that require focus. As I said earlier, I use instagram for content creation so I had to use it for that reason. 

3. The positives were that I was able to complete my assignments early,  I had so much free time left for my personal plans. I didn't find any negative effects of being unplugged from instagram. 

4. My addiction to technology is definitely not in a problematic level, I am able to complete my assignments before deadlines, manage time for my hobbies, self study and personal life. I just tend to get distracted when I'm doing something that requires large amount of my brain power, I slip up and do something that's less painful to do. But, I quickly realize what I'm doing and I turn it off immediately. I don't get distracted again for a long time, if i do I just quit everything and stare at the wall. I measure my level of addiction based on how much time I waste in my focus sessions, that is what matters to me the most. 

5. Technology helped me to stay connected with my closed one with the help of digital com