vowels = ["a","e","i","o","u"]

def main():
  try:
    word = input(f"Word: ").lower()
    result = shorten(word)
    print(result)
  except ValueError:
    print("Enter only strings")
  except EOFError:
    print("Exiting..")
  except KeyboardInterrupt:
    print("Exiting..")


def shorten(str):
  ''''''
  word_list = list(str)
  new_list = []
  for str in word_list:
    if str not in vowels:
      new_list.append(str)
  final_word = "".join(new_list)
  return final_word 

if __name__ == "__main__":
  main()