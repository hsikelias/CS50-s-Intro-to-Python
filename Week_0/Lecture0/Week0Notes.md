# WEEK 0 — Python Basics

## Functions

A **function** is an action (or verb) that lets you do something in a program. The computer or programming language already knows how to perform the action—you just need to use it.

```python
print("Hello World")
# print is the function
```
Functions do exactly what you ask them to do. The value you pass inside the parentheses is called an argument, and it affects the result of the function.


## input()

The **input()** function asks the user for input and pauses the program until something is typed.
```python
input("What's your name? ")
```
This only collects the input. To use it, you must store it in a variable.

## Variables & Return Values

A variable is like a container that stores data.
```python
name = input("What's your name? ")
```
Here, input() returns a value and name stores that value so it can be reused.

## Comments

Comments start with #. The computer ignores them. They are used to document and explain code.

```python
# This is a comment
```

## print() with Multiple Arguments

```python
print("Hello, ", name)
# OR
print("Hello, " + name)
```

## print() Parameters
```python
print(*objects, sep=' ', end='\n')
```

These are **parameters—placeholders** defined by the function. When you pass values to them, those values are called arguments.

Default values:
- sep = ' ' (single space)
- end = '\n' (new line)

`\n` moves the cursor to the next line. You can override both `sep` and `end`.

### Types of Parameters

**1. Positional Parameters**
The order matters. The first value goes to the first parameter, the second to the second parameter.

**2. Named Parameters**
You explicitly specify the parameter name. Examples include sep and end.

## Escape Characters
Escape characters allow special characters to appear inside strings.

```python
print("Hello, \"friend\"")
```

Common escape characters:

- ``\n - new line``

## F-Strings

F-strings allow you to format variables directly inside strings.

```python
print(f"Hello, {name}")
```
They are cleaner and easier to read than string concatenation.

## String Methods

String methods allow you to manipulate text stored in strings.

**split()**

If a user enters their full name and you only want the first name:
```python
first, last = name.split(" ")
```
The first occurrence goes into first, and the second goes into last. Assignment depends on order.


**Integers**
Integers are whole numbers.

Math operators:
- + addition
- - subtraction
- *  multiplication
- / division
- % modulus

The modulus operator `(%)` returns the remainder after division.

## Floats

Floats are numbers with decimal points.

```python
3.14
```
Floats are not infinitely precise.

## round()

```
round(number[, ndigits])
```
Rounds a number to the nearest value. By default, it rounds to the nearest whole number. You can specify how many decimal places using ndigits.

## Defining Your Own Functions
You can create your own functions using the ``def`` keyword.

```python
def butt():
    # function body
```