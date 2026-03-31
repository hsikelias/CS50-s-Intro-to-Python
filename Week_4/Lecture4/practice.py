import random
import statistics


# random library
number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]

random.shuffle(cards)

for card in cards:
    print(card)


# statastics library
print(
    statistics.mean(
        [
            1,
            2,
            3,
            4,
            5,
            6,
        ]
    )
)
