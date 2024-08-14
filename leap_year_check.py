# Follwoing Code will check if given year is a leap year or not.
def is_leap_year(date_string):
  year = int(date_string[:4])
  #print(year)
  #print(type(year))
  if (year%4==0):
    print("True")
  elif (year%100==0) and (year%400==0):
    print("True")
  else:
    print("False")


is_leap_year("1900-02-29")
