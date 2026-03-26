
# user enters date order in MM/DD/YYYY order formatted like

# 9/8/1542 or September 8, 1636

# then output the same date in YYYY-MM-DD format
# prompt user again if format not valid
# assume every month has no more than 31 days, no need to validate exact num


months = [
    "Janruary",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

def main():
    while True:
        try:
            date = input("Date: ").strip()
            month, day, year = parse_date(date)  
            validate_date(month, day)            
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        except ValueError as e:
            pass                                  

def parse_date(date):

    if date.count("/") == 2:
        return parse_numeric(date)
    elif date.count(" ") == 2:
        return parse_worded(date)
    else:
        raise ValueError("Unrecognized format")

def parse_numeric(date):
    month_str, day_str, year_str = date.split("/")
    month, day, year = int(month_str), int(day_str), int(year_str)  
    return month, day, year

def parse_worded(date):
    month_str, day_str, year_str = date.split(" ")
    month_str = month_str.title()
    day_str = day_str.replace(",", "")

    if month_str not in months:
        raise ValueError(f"Unknown month: {month_str}")

    month = months.index(month_str) + 1    
    day = int(day_str)                     
    year = int(year_str)
    return month, day, year

def validate_date(month, day):
    if not 1 <= month <= 12:
        raise ValueError("Month out of range")
    if not 1 <= day <= 31:
        raise ValueError("Day out of range")

main()

"""
:) input of 9/8/1636 outputs 1636-09-08

:( input of September 8, 1636 outputs 1636-09-08
    expected: "...636-09-08"
    actual:   "...636-08-08\n"

:) input of 10/9/1701 outputs 1701-10-09

:( input of October 9, 1701 outputs 1701-10-09
    expected: "1701-10-09"
    actual:   "1701-09-09..."

:) input of " 9/8/1636 " outputs 1636-09-08

:( input of 23/6/1912 results in reprompt
    expected program to reject input, but it did not

:) input of 10 December, 1815 results in reprompt

:( input of October/9/1701 results in reprompt
    expected program to reject input, but it did not

:( input of 1/50/2000 results in reprompt
    expected program to reject input, but it did not

:( input of December 80, 1980 results in reprompt
    expected program to reject input, but it did not

:( input of September 8 1636 results in reprompt
    expected program to reject input, but it did not
"""