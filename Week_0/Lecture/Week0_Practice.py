# print("Hello World")

# print("What's your name? ")

# input("What's your name? ")

# name = input("What's your name? ")
# assigning the input value to name, copies from the right to the left. 

# name = name.strip().strip().title()

# we're using another function, tho techcnically called a method removes whitespace from str. It removes space from left and right in the string 

# name = name.capitalize()
# capitalizes only the first letter
# you can add multiple of these as well. 
# first, last = name.split() 

# says hello to user
# print("Hello,", name,end="???" )
# print("Hello,", first)

# Quotes in quotes
# 1. print("Hello, 'friend'")
# 2. print("Hello, \"friend\"")
# 3. print(f"Hello, {name}")

def hello(to="world"):  #parameter name
  print("Hello,",to)


name = input("What's your name?")
hello()
hello(name)