def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
# make sures main function isn't always called.
# code under this will only run when the script
# is run directly, not when it's imported.

