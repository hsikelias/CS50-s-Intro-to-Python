import sys

import inflect

p = inflect.engine()

names = []

try:
    Name = input("Name: ")
    names.append(Name)
except EOFError, KeyboardInterrupt:
    if len(names) >= 1:
        joined_words = p.join(names)
        print(f"\n Adieu, adieu, to {joined_words}")
        sys.exit()
    else:
        sys.exit()
