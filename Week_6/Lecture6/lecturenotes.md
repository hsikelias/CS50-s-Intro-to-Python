File input output is important as we want to store data in many cases and it's a waste of time if you have to enter the data again and again.

```python
file = open("names.txt","w")
file.write(name)
file.close()
```

above, you can see we use the open() function to open a file and then u define how you want to open the file, "w" is to write a file, which can also overwrite a file. To add add we need to use append. 

**.write()** is how we write any data
**.close()** is a manual way to close the file by saving data without any data loss or anything during program crash. 


```python
file = open("names.txt","a")
```
if we add data now it will be added and old data is saved but the new data will be on the same line with old ones.
write does not make a new line, only print did. 

```python
file.write(f"{name}\n")
```
this is one possible fix. 


a better practice to do instead of using __.close__ we should instead use __with__. This allows u to not worry if you forgot to use .close()

use __sorted()__ to sort a file by any condition or reverse it. 


# .csv
data seperated by ",", like text even in csv we get the entire line, meaning all the information present in that line.

```csv
Hermoine,Gryffindor
Harry,Gryffindor
Ron,Gryffindor
Draco,Slytherin
```

```python
with open("students.csv") as file:
  for line in file:
    row = line.rstrip().split(",")
```
This is how you commmonly split a csv file to access the individual items in a line, row is a list and you can access individiual details.

```python
students = [] 

students = [] 

with open("students.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    student = {"name":name,"house":house}
    students.append(student) # [{'name':'xyz','house':'xyz'},{},{}]

for student in students:
  print(f"{student['name']} is in {student['house']}")
```

But how to sort the name or even the house in the list with many dictionaries?

```python
def get_name(student):
  return student["name"]

for student in sorted(students,key=get_name):
  print(f"{student['name']} is in {student['name']}")
```

here we made a new function that returns a student name from the dictionary and by adding the key parameter to this function, we will sort based on the student name.Sorted doesnt know how to get the name from dictionary, this function will allow sorted to get the key thru other funciton which provides the key. this method will also allow house to be sorted if we want to, no more relying on english statements.   

# How to deal with functions that you use only once and forget later.

In this case you use a lambda

```python
for student in sorted(students,key=lambda student: student["name"]): # first is the parameter name and returns every name from the dictionary
  print(f"{student['name']} is in {student['house']}")
```

```csv
Harry,Number Four, Privet Drive
Ron,The Burrow
Draco,Malfoy Manor
```
The problem here is that the harry's home is sperated by , which makes python think there is 3 values, which would cause a value error. 
there are many ways to fix this like using a | between 2 values or using commas but that might be less secure or you might have to change your logic entirely. A better approach to solve this problem is to use the **csv library**.

# CSV LIBRARY

1. reader function:

```python
reader = csv.reader(file)
```

Reader goes into a csv file and figures out where the commas, double quotes.

```python
students = [] 

with open("students.csv") as file:
  reader = csv.reader(file)
  for name,home in reader:
    students.append({"name": name, "home": home})


for student in sorted(students,key=lambda student: student["name"]): # first is the parameter name and returns every name from the dictionary
  print(f"{student['name']} is in {student['home']}")
```

2. DictReader()

A way to avoid unpacking things manually, the data could be stored in their columns itself.. we will be using headers. 

```csv
name, home
Harry,Number Four, Privet Drive
Ron,The Burrow
Draco,Malfoy Manor
```
now the top row is not someones literal name/home, now that we've changed things in csv the way we get names and homes will be different so we will use __DictReader__. DictReader will do what reader does but instead of list of columns its dictionary of columns.

```python
with open("students.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    students.append({"name":row["name"], "home":row["home"]}) # now even if we change the rows of name/home, the program would still work. 
```


# Writing CSVs

```python
with open("students.csv", "a") as file:
  writer = csv.writer(file)
  writer.writerow([name,home])
```

another way to write files without needing to worry about the order of name and house is again, to use a dictionary writer, so that we can associate the inputs with keys. 
