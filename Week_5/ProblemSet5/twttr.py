vowels = ["a","e","i","o","u","A","E","I","O","U"]

def main():
    try:
        word = input("Word: ")
        result = shorten(word)
        print(result)
    except ValueError:
        print("Enter only strings")
    except EOFError:
        print("Exiting..")
    except KeyboardInterrupt:
        print("Exiting..")

def shorten(word):
    new_list = []
    for char in word:
        if char not in vowels:
            new_list.append(char)
    return "".join(new_list)

if __name__ == "__main__":
    main()