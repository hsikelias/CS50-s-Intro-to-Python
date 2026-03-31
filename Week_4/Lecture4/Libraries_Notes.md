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

obviously this is not good all the time and some could say using random along with the function is 
helpful to read and just easy to categorize. 

# APIS
Application Programming Interface
3rd party services that we write code to communicate to, many APIs live on the internet

python has a package called "requests", this allows web requests from python code. 

# JSON - Javascript Object NOtation