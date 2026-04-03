import sys
import inflect

names = []
# adieu = goodbye
# assume user will enter at least one name

while True:
    try:
        Name = input("Name: ")
        names += Name
    except EOFError KeyboardInterrupt:
        sys.exit()
