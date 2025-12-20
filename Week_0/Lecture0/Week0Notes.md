# WEEK 0: 


## Functions:

Action or verb that lets you do something in the program. The computer/language already knows how to do it, you just have to use it. 

```python
print("Hello World")
# here print is the function
```
the functions don't just do something random, they do what you ask for. This is called an **argument**, inside the `print()` we entered "Hello World", and it influences the results of the function. 


Asking questions to users using `input()`, it basically stops and asks users to type something. Nicely, `input()` takes in arguments so we can just ask our question insde of it. 

```python
input("What's your name? ")
```
This just takes the users input but does nothing with it unless we try to use it. That's where we get `return values` and `variables`. We return the value we get from user and then use variable to store it. 

Variable is like a container that stores data. 

## Comments:

Comments (#) are like notes to yourself, computers ignores everything inside the comments.Comments are very useful to document your code. 

-------

``` Python 
# one , in " " and the other , seperates arguments
print("Hello, ", name)
#         OR 
print("Hello, "+ name)
```


``` Python
print(*objects, sep=' ', end='\n')
# These are technically the parameters, these are the things you can pass to a function. When you actually use them and pass in values, those inputs are called ARGUMENTS. 

```

`sep` default value is a single blank spaces, `end` default value is \n.

\n = new line, moves the cursor to the next line. You don't see it everytime because its just a default value. 

you CAN override the deault values for both sep and end. 

## Types of Parameters:

1.) Positional Parameters: First thing passes gets done first, second thing you passed gets passed second, 

2.) Named Parameters: examples are `sep` and `end`. 


## Escape Characters:
```python
print("Hello, \"friend\"")
continues the line in a new line. 
```

## F-String:
formats things in a string
s
```python
print(f"Hello, {name}")
```

## String Methods:
![String Methods](Week_0\images\image.png)s

`split()` Imagine if you ask for users name and people usually enter full name and you don't want to greet them by full name. You can use split to just greet them by their first name.

``` Python
first, last = name.split(" ")
# first such occurance goes to first, and the other occurance goes to last. This totally depends on the order. 
```

## Integer:
Theres math so theres many symbols as well

+, -, *, /, %

% = modulous operator, the reminder you get after dividing one number from another. 


## Float:
Number but has decimal points. Float is not infinite entirely. 

## Round

```python
round(number[, ndigits])

# Basically rounds to 2 digits by default and later you can specify till where you want to round. 
```

You can create your own functions! you can use `def` to create a function 

```python
def butt():
  # bla bla bla
```
