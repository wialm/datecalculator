def calculator(day, month, year, name):
  #zeller's congruence formula applied
  total_days = (day + (int((13*(month + 1))/5)) + year + (int(year/4)) - (int(year/100)) + (int(year/400)))
  #result of formula
  if total_days%7 == 0:
    print("that day was on monday")
    print("",name ,"was born on a monday." )
  elif total_days%7 == 1:
    print("",name ,"was born on a tuesday." )
  elif total_days%7 == 2:
    print("",name ,"was born on a wednesday." )
  elif total_days%7 == 3:
    print("",name ,"was born on a thursday." )
  elif total_days%7 == 4:
    print("",name ,"was born on a friday." )
  elif total_days%7 == 5:
    print("",name ,"was born on a saturday." )
  elif total_days%7 == 6:
    print("",name ,"was born on a sunday." )
  else:
    print("oh no")

def menu():
  invalid_year = 0
  leap_year_counter = 0
  #ask for information from user
  print("what is your name?")
  name = input("")
  print("hi", name,"!!! pleas enter your date (in dd/mm/yyyy): ")
  date = input("")
  #splits information into separate variables
  split = date.split("/")
  day = int(split[0])
  month = int(split[1])
  year = int(split[2])
  #validation process
  if year%4 == 0:
    leap_year_counter = 1
  if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days_in_month = 31
  elif month == 2:
    days_in_month = 28 + leap_year_counter
  elif month == 4 or month == 6 or month == 9 or month == 11:
    days_in_month = 30
  else:
    print("that is not a valid month.")
    exit()
  if day > days_in_month:
    print("this month doesn't have enough days in it!")
    exit()
  elif day < 1:
    print("that is a VERY invalid day")
    exit()
  if day > 31:
    print("stop tryna break my program")
    exit()
    #enter calculator
  calculator(day, month, year, name)
menu()

