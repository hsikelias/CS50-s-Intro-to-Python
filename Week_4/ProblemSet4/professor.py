import random
import sys


def main():
    qn_count = 10
    attempts = 0
    level = get_level()

    while qn_count > 10:
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        try:
            user_answer = int(input(f"{x} + {y}= "))
            if user_answer == correct_answer:
                qn_count -= 1
            else:
                print("EEE")
                attempts += 1
        except ValueError:
            print("EEE")
            attempts += 1


def get_level():
    try:
        n = int(input("Level: "))
        if n == 1 or n == 2 or n == 3:
            return n
    except ValueError:
        pass


def generate_integer(number_count):
    if number_count == 1:
        return random.randint(0, 9)
    elif number_count == 2:
        return random.randint(10, 99)
    elif number_count == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid Level entered")


if __name__ == "__main__":
    main()
