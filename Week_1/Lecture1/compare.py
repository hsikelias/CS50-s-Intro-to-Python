'''
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
  print("x is less than y")
if x > y:
  print("x is greater than y")
if x == y:
  print("x is equal to y")
'''

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
  print("x is less than y")
elif x > y:
  print("x is greater than y")
elif x == y:
  print("x is equal to y")
## instead of elif on x == y we can also use else because thats the only posssible condition. 