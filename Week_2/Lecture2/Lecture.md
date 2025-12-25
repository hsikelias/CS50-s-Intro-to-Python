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

```python

students = ["Hermione","Harry","Ron"]
for i in range(len(students)): # value of list 3, then its range 0,3
  print(i+1,students[i])

# so here we're using len function to find the length of the list instead of hardcoding and then printing student names.
```

# Dictionary
A dictionary usually has a bunch of words and its definition. Something and its something meaning, in programming we call these keys and values. `{}` dictionary syntax.

```python
students = ["Hermione","Harry","Ron","Draco"]
houses = ["Gryffindor", "Gryffindor","Gryffindor","Slytherin"]

#we have 2 lists now, imagine if we add more people and then the order needs to be changed everytime. So we use Dictionary to actually assign values
```


```python
students = {"Hermione": "Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin"}
```

## How to access the data in dictionary?
Unlike using `[]` to access stuff in a list, in dictionary we can directly use words, that means it should look something like this.

```python
print(students["Hermione"]) #output = Gryffindor
```
Now this can obviously be better if we want to print every student we need to use loops.


**For looping a dictionary**

```python
for student in students:
  print(student)
#output = this only gives out the keys not values
```

To loop inside a dictionary and get it's value we need to do something similar to what we did with lists. 

```python
for student in students:
  print(student, students[student])
  #              dic[key] = value
```

Imagine if you have more data to add to each student, right now we have house but what if we want to add more?

```python
students = [
  {"name": "Hermione","house":"Gryffindor","patronus":"Otter"},
  {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
  {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell terrier"},
  {"name":"Draco","house":"Slytherin","patronus":None}
]
# we make a list of dictionaries, each student is in a dictionary in itself
# None = means there is no value for that key.
```

```python
for student in students:
  print(student["name"], student["house"], sep=", ")
```

# Tuple

```python
def main():
  coordinates = (42.376, -71.114)

  latitude, longitude = coordinates
  # tuple allows us to unpack things and make thm their own variable. Coordinates first value goes to the first variable latitude and then -71.114 to longitude. 

  print(f"Latitude: {coordinates[0]}")
  print(f"Longitude: {coordinates[1]}")
  #output = Latitude: 42.376
  #output = Longitude: -71.114
```
A drawback of tuple is that you can't assign items 

```python
def main():
  coordinates = (42.376, -71.115)
  coordinates[0] = -42.376 # wont work
```

Only use tuple if you're sure you won't edit the data a lot and the data is small, tuple is very memory efficient as well. 



