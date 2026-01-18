def main():
  camel_word = input("Enter camelCase word: ")
  convert(camel_word)

def convert(camel_word_2):
  snake_word = [] 

  for int, char in enumerate(camel_word_2):
    if char.isupper():
      if int > 0:
          snake_word.append('_')
      snake_word.append(char.lower())  
    else:
      snake_word.append(char)
    snake_case_word = ''.join(snake_word)
    print(snake_case_word)

main()

# enumerate 