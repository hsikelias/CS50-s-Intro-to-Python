
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
  date = input("Date: ")
  date_verification(date)

def date_verification(date):
  """
  splits the input given by the user and verifies entries on a basic level before moving to output processing.
  """
  while True:
    if date.count("/") == 2:
      split_date = date.split("/")
      month, day, year = split_date

      try:
        int_month = int(month)
      except ValueError:
        pass
      try:
        int_day = int(day)
      except ValueError:
        pass
      try:
        int_year = int(year)
      except ValueError:
        pass
    
      date_verification_level2(int_month,int_day,int_year)
    exit()

    if date.count(" ") ==2:
      split_date = date.split(" ")
      month, day_withcoma, year = split_date

      char_to_remove = ","
      day = day_withcoma.replace(char_to_remove, "")    

      try:
        titled_month = month.title()
      except Exception:
        pass
      if month in months:
        try:
          int_day = int(day)
        except ValueError:
          pass
        try:
          int_year = int(year)
        except ValueError:
          pass

        date_verification_level2(titled_month,int_day,int_year)
    else:
      break

def date_verification_level2(month, day, year):

  if day > 31:
    raise Exception("Day's can't be greater than 31") 

main()

"""
1. input 9/8/1636 should output 1636-09-08

2. input September 8, 1636 should output 1636-09-08

3. input 32/6/1912 should output a reprompt 

4. input December 80, 1980 should output a reprompt
"""
