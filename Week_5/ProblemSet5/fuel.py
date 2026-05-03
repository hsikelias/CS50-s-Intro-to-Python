def main():
    fraction = input("Fraction (X/Y): ")

    try:
        percent = convert(fraction)
        print(gauge(percent))
    except Exception as e:
        print(f"error = {e}")


def convert(fraction):
    if fraction.count("/") == 1:
        split_fraction = fraction.split("/")
        x, y = split_fraction

        if len(split_fraction) == 2:
            try:
                int_x = int(x)
                int_y = int(y)

                if int_x < 0 or int_y <= 0:
                    raise ValueError("Invalid integers")
                if int_x > int_y:
                    raise ValueError("X can't be greater than y")
                else:
                    percent = round(int_x / int_y * 100)
                    return percent

            except ValueError:
                raise ValueError("Follow the proper format, only int allowed")
        else:
            raise Exception("Fololow the proper format, X/Y")

    else:
        raise ValueError("Invalid Format")


def gauge(percent):
    if percent >= 99.0:
        return "F"
    if percent <= 1.0:
        return "E"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()
