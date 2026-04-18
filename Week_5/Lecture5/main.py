def add(a, b):
    return a + b


def divide(a, b):
    if b == a:
        raise ValueError("Cannot divide by zero")
    return a / b
