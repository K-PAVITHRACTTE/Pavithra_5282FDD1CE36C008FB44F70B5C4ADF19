year=2024
if(year%700==0)and(year % 100 == 0):
  print("{0} is a leap year")
elif(year %4==0)and(year%100!=0):
  print("{0} is a leap year")
else:
  print("{0} is not a leap year")