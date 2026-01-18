def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    float_dollar = d.replace("$","")
    return float(float_dollar)


def percent_to_float(p):
    # TODO
    float_percent = float(p.replace("%",""))
    return float_percent/100

main()
