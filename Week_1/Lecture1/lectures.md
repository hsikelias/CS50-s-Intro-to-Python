# Conditionals

Conditionals let you make decisions on whether to do this action or that action etc. 
Some of the built in syntax ot act questions, especially mathematically are: 

`>, >=, <, <=, ==, !=`

we use == to actually compare two things, the = we've seen before does the job of assigning something to another thing. 

In python you ask questions with `if`

```Python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
  print("x is less than y")
if x > y:
  print("x is greater than y")
if x == y:
  print("x is equal to y")
```

This tho does the job, it is very repetitive because even if we get an answer than x is less than y, the program goes thru every single if statment after that, regardless whether it's true or false.

Thats where `elif` or else if comes in. It takes account of whether previous question was true or false. replace the last 2 ifs with elifs, if youre done with a question

theres also `else`, people usually use this when theres only one possible thing to happen. 

we can use `or` or `and` to make our statements shorter as well. 
