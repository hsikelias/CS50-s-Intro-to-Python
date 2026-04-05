import random
import sys


def main():
    try:
        n = int(input("Level: "))
        if n > 100 or n <= 0:
            main()
        else:
            guess(n)
    except ValueError:
        pass
        main()


def guess(number):
    random_number = random.randint(1, number + 1)
    while True:
        guess = int(input("Guess: "))
        if guess < 0:
            pass
        elif guess > random_number:
            print("Too large!")
        elif guess < random_number and guess > 0:
            print("Too small!")
        elif guess == random_number:
            print("Just right!")
            sys.exit()


main()
