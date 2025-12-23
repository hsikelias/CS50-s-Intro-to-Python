# breakfast: 7:00-8:00, lunch: 12:00-13:00, dinner: 18:00-19:00
def main():
  time = input("What time is it? (Enter XX:XX format) ")
  converted_time = convert(time)

  if 7 <= converted_time <= 8:
    print("breakfast time")
  elif 12 <= converted_time <=13:
    print("lunch time")
  elif 18 <= converted_time <=19:
    print("dinner time")

def convert(time):
  """
  converts time a str to 24hr format, float. 7:30(7 hours 30minutes) to 7.5
  """
  hours,minutes = time.split(":")
  minutes_to_hours = float(minutes)/60
  total_time = float(hours) + minutes_to_hours
  return total_time

if __name__ == "__main__":
  main()
