# Week 4:  Libraries

Code others or that you wrote to share across differnet projects, these are called **modules**. 
Some common python built in moduels is "random"

modules are accessible only after you **import** it. 


# Random Library

```python
import random # this is how u import a module


random.choice([]) # choice function
```

`random.choice(seq)`, seq is a parameter it can be a list of anything.


you can also be more functional with from, by just using import (module name) you import everything.
and also everytime you use the choice function you need to write `random.` something. 

```python
from random import choice

coin = choice(["heads"],["tails"])
print(coin)
```


**random.randint(a, b)** provides a number between a and b, inclusive. 


**random.shuffle(x)** takes a list of instances, and shuffles them




# Statistics Library: 
- Does things like mean, median and other statistics. 


# Command - Line Arguments:
- **sys** these are the commands specific to your system



# Packages: 3rd Party Libraries
users can install this on their own system.
one of the location to download these packages are
**pypi.org**

**pip** is python's package manager that installs the packages for you 
