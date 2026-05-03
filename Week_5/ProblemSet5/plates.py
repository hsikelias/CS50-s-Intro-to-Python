import string

numbers = ["1","2","3","4","5","6","7","8","9"]
alphabets =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def main():
  plate = input("Plate: ")
  answer = is_valid(plate)
  print(answer)

def is_valid(s):
  if 2 <= len(s) <= 6:
    first_word = s[0]
    second_word = s[1]
    if first_word.upper() in alphabets and second_word.upper() in alphabets:
      for char in s:
        if char in string.punctuation:
          return False
    else:
      return False
  else:
    return False
  
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

if __name__ == "__main__":
  main()