#prompts user for a string, outputs the same word but removes all the vowels (A,E,I,O,U).
#twitter = twttr

vowels = ["a","e","i","o","u","A","E","I","O","U"] #maybe use later
output = ""
full_word = input("Input: ") #first convert 

for letter in full_word:
  if letter in vowels:
    vowel_position = full_word.index(letter) #gives the position of vowel in the full_word
    new_word_temp = full_word[:vowel_position] + full_word[vowel_position + 1:] #new_word_temp = bes
    full_word = new_word_temp
print(full_word, end="")

