#Farenheit & Celcius Conversion 
#Daniel Alvarez 
#Date Created: 1/25/24

import math 

# ask for choice of Fahrenheit or Celcius conversion 

while True: 
  unit = input("What are you trying to convert, Farenheit to Celcius or Celcius to Farenheit?: ")
  new_unit = unit.lower()
  
#converts farenheit to celcius and prints the answer
  if new_unit == "farenheit":
    num = float(input("What is the degree in farenheit?: "))
    celc_conver = (num - 32) * 5 / 9 
    print(celc_conver)
    
#converts celcius to farenheit and prints the answer
  elif new_unit == "celcius":
    num = float(input("What is the degree in celcius?: "))
    faren_conver = (num * 9/5) + 32  
    print(faren_conver)
    
