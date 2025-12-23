# Loops

Why do we loop? to avoid repeating something. Imagine having to print a certain word 100 times manually. 

**while**

```python
i = 3
while i != 0:
  print("meow")
# loops forever, ctrl-c to exit terminal when stuck in loop. 
```

```python
i = 3
while i != 0:
  print("meow")
  i -= 1
# this wont loop forever because our condition will be false after some time.
```

**for**
`for` lets us iterate over a data, lets say a list

```python
for i in [0,1,2]:
  print("Meow")
## this is readable but not effective. 

for i in range(10):
  print("meow")

# notice how i is never used, use "_" instead of i because to tell ourselves we are not using it anywhere. 

print("Meow " * 3) #output = meowmeowmeow
print("Meow \n" * 3) #fixed output is in a new line everytime with an extra line in the end
print("Meow \n" * 3, end="") # a struggle to read this but no new line in the end
```


***list**
Let's us add list of data

```python
students = ["Hermione","Harry","Ron"]
print(students) #output =['Hermione', 'Harry', 'Ron']

# this prints the entire list
```


```python
students = ["Hermione","Harry","Ron"]

print(students[0])
print(students[1])
print(students[2])

# this lets us be more specific but it's still repetitive if we add more students, so we can loop. 
```