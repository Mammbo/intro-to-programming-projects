#Currency Convertor 
#Daniel Alvarez 
#Date Created: 1/25/24

import math 

USD = float(input("How much USD do you want to convert?: "))
choice = input("What do you want to convert Euros(1), Pounds(2), Yen(3), Yuan(4), Won(5)?: ")

if int(choice) == 1:
  euros = round(float(USD) * .92) 
  print(euros)
  
elif int(choice) == 2:
  pounds = round(float(USD) *  .79)
  print(pounds)
  
elif int(choice) == 3:
  yen = round(float(USD) * 148)
  print(yen)
  
elif int(choice) == 4:
  yuan = round(float(USD) * 7.10)
  print(yuan)
  
elif int(choice) == 5:
  won = round(float(USD) * 1337)
  print(won)