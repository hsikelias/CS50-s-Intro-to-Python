greeting = input("Greeting: ").strip().lower()

# hello prints 20/100 and the $0 is ignored. 
if greeting.startswith("hello"):
  print("$0")
elif greeting.startswith("h"):
  print("$20")
else:
  print("$100")
