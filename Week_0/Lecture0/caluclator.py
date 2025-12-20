x = float(input("What's x? "))
y = float(input("What's y? "))

# on default inputs take in things like strings. To add like numbrs would we need to change the data type. 

z = round(x+y)
z = round(x /y, 2)

print(f"{z:,}")