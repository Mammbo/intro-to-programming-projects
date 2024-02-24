#M6 Project 6-1: Prime Number Checker 
#Daniel Alvarez 
#2/18/24

#function that will check prime number and non prime numbers factors and store them into a list factors, if the list length is 2 it will print prime number if it is more than 2 it will print non prime and its factors. will use for loop it iterate over each number in the list to the final number 
def prime_and_factors_check(num):
    factor = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor.append(i)
    factor_length = len(factor)
    if factor_length == 2: 
        print(f"{num} is a prime number.")
    else:
        factor.sort()
        print(f"{num} is NOT a prime number.\nIt has {factor_length} factors: {factor} ")
#Welcome Message
print("Prime Number Checker")
#while looop to loop the code 
while True:
    #start and stop mechanism 
    start_stop = input("\nCheck A Prime Number? (y/n):")
    new_start_stop = start_stop.lower()
    # will ask for user input and then determine if the users input is valid or not
    if new_start_stop == "y":
        num = int(input("\nPlease enter an integer between 1 and 5000: "))
        if num > 5000 or num < 1: 
            print("Please enter a valid interger between 1 and 5000")
        #when users input is valid it will run the code. 
        elif num <= 5000 or num >= 1:   
            prime_and_factors_check(num)
    #break out of the code 
    elif new_start_stop == "n":
        print("Bye!")
        break 
    #case for when users input wrong data 
    else: 
        print("Hey you type something wrong, try it again :)")


