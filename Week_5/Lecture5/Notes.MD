# TOPIC : Unit Tests

writing our own tests for our code to make sure it's running well

**assert** boldly saying something to happen, or like lets say we have a square function and doing assert square(2) = 5.. It returns if something is true or not. 

Anything false would lead to an **AssertionError**

# pytest

does the job of automating unit testing 

Below is the pytest function to handle errors. 

'''
with pytest.raises(TypeError):
'''

any folder with a **___init__.py** will be treated as a package.

**unit test** is the smallest type of test and it's typically testing very small component like a function, method and classes sometimes.
