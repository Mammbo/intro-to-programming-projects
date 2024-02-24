# M9 Project 9-1: Interest Calculator 
#Daniel Alvarez 
#2/18/24

#program that calculates the interest on a loan and displays formatted results 
# formula for caclulating the interest amount is loan_amount * (interst_rate / 100)

import locale

# Function to calculate interst and then format the output
def interest_cacl():
    loan = float(input("Enter Loan Amount: "))
    new_loan = round(loan, 2)
    interest_rate = float(input("Enter Interest Rate: "))
    new_int_rate = round(interest_rate, 3)
    interest_amount = new_loan * (new_int_rate / 100)
    new_interest_amount = round(interest_amount, 2)

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  

    formatted_loan = locale.currency(new_loan, grouping=True)
    formatted_new_interst_amount = locale.currency(new_interest_amount, grouping=True)

    print(f"\nLoan Amount:             {formatted_loan:>15}")
    print(f"Interest Rate:             {new_int_rate:>12.3f}%")
    print(f"Interst Amount:            {formatted_new_interst_amount:>13}")

#welcome message 
print("Interst Calculator")
#While loop to loop the code as many times as the user wants 
while True: 
    start_stop = input("\nDo you want to calculate interst? (y/n):")
    new_start_stop = start_stop.lower() 
    #runs main code 
    if new_start_stop == "y":
        interest_cacl()
    # breaks code 
    elif new_start_stop == "n":
        print("\nBye!")
        break
    #case for if there is an error in users y or n input
    else: 
        print("You may have typed something, try again :)")
    