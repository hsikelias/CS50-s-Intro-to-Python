def main():
    ...
    greeting = input("Greeting: ").strip().lower()
    value(greeting)
    money = value(greeting)
    print(money)

def value(greeting):
    '''takes in a string, returns an int'''
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        money = 0
    elif greeting.startswith("h"):
        money = 20
    else:
        money = 100
    return money

if __name__ == "__main__":
    main()
