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