name = input("What's your name? ")
'''
if name == "Harry" or name == "Hermione" or name == "Ron":
  print("Gryffindor")
elif name == "Draco":
  print("Slytherin")
elif name == "Ron":
  print("Sweryew")
else:
  print("Who?")
'''

match name:
  case "Harry" | "Jack" | "Bill":
    print("Gryffindor")
  case "Hermione":
    print("Blabla")
  case "Draco":
    print("Slytherin")
  case _:
    print("Who?")