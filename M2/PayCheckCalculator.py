#Python Pay Check Calculator
#Daniel Alvarez
#1/31/24


#Title
print("Pay Check Calculator")

# Asks for hours worked 
hours_wrkd = float(input("How many hours did you work? "))
#asks for hourly rate 
hrly_rate = float(input("What is your hourly rate? "))
#calculates gross pay
gross_pay = hours_wrkd * hrly_rate 
#asks for tax rate 
tax_rate = float(input("What is your tax rate? "))

#calculates tax rate 
tax_amount = gross_pay * (tax_rate / 100)

#calculates take home pay 
take_home_pay = gross_pay - tax_amount
#prints tax home pay, gross pay, and the tax amount 
#uses an fstring to input the variable and then uses a \n to print them on other lines
print(f"\nYour gross pay is: {gross_pay:.2f}\n\nYour tax amount is:  {tax_amount:.2f}\n\nYour take home pay is: {take_home_pay:.2f}")
