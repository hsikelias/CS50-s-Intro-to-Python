#Exceptions


'''python
x = int(input("What's x? "))
print(f"x is {x}")
# no defense against string inputs.


# need error handling code, strong defence code
'''

**try**, **except**

'''python
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
'''

**ValueError** is when any variable or the value received is not what it's expecting.

**NameError** refers t