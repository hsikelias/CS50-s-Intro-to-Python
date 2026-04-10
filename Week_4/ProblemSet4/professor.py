import random


def main():
    questions = 10
    correct = 0
    n = get_level()

    while questions > 0:
        x = generate_integer(n)
        y = generate_integer(n)
        assert x is not None
        assert y is not None
        answer = x + y
        chance = 3

        while chance > 0:
            try:
                user_ans = int(input(f"{x} + {y} = "))
                if user_ans == answer:
                    correct += 1
                    break
                else:
                    print("EEE")
                    chance -= 1
            except ValueError:
                print("EEE")
                chance -= 1

        if chance == 0:
            print(f"{x} + {y} = {answer}")
        questions -= 1

    print(correct)


def get_level():
    """prompts user for level and returns it"""
    while True:
        try:
            n = int(input("Level: "))

            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass


def generate_integer(level):
    """returns a single randomly generated non-negative integer with level digits"""
    # assume level = 3
    if level == 1:
        int = random.randint(0, 9)
        return int
    elif level == 2:
        int = random.randint(10, 99)
        return int
    elif level == 3:
        int = random.randint(100, 999)
        return int


if __name__ == "__main__":
    main()
