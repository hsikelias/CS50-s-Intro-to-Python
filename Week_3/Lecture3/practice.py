def main():
    print(get_int())

def get_int():
    while True:
        try:
            return int(input("What's x? ")) 
        except ValueError:
            pass 
        # leave it at pass if you want to point out
        # the value error but just repeat without sayin
        # anything.
            print("x is not an integer")
            # return will break and also return the value
main()