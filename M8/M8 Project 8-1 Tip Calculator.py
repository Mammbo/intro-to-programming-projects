#M8 Project 8-1: Tip Calculator 
#Daniel Alvarez 
#2/18/24


#Welcome message 
print("Tip Calculator\n")
print("INPUT")
while True: 
#validate if user's input is a positive float not a string nor a negative number nor 0 for each cost and tip 
#ask for user input of cost of meal
    cost = input("Cost of meal: ")
    if not cost.replace('.', '').isdigit():
        print("Must be valid decimal number. Please try again.")
    else: 
        new_cost = float(cost)
        if new_cost <= 0: 
            print("Cost must be greater than 0. Please try again")
        else:
            break 
#ask for user input of tip percent 
while True: 
    tip = input("Tip Percent: ")
    if not tip.isdigit():
        print("Must be a valid integer. Please try again.")
    else: 
        new_tip = int(tip)
        if new_tip <= 0: 
            print("Tip must be greater than 0. Please try again.")
        else:
            break 
#calculate tip amount 
tip_amount = new_cost * new_tip / 100
round_tip_amount = round(tip_amount, 2)
#calculate total amount 
total_cost = new_cost + tip_amount
round_total_cost = round(total_cost, 2)
#print the output of cost of meal, tip percent, tip amount, and total amount, and round all answers to two decimal places
print(f"\nOUTPUT\nCost of meal: {new_cost}\nTip percent: {new_tip}%\nTip amount: {round_tip_amount} \nTotal amount: {round_total_cost}")
