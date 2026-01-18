''' Trying to check for a negative number.. this wont work if the user is really stupid. We can use loops tho
n = int(input("What's n? "))
if n <0:
  n = int(input("What's n?" ))
  if n<0:
    n = int(input("What's n?" ))
'''

while True:
  n = int(input("what's n? "))
  if n >0:
    break

for _ in range(n):
  print("meow")