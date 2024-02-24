#Temperture Statistics Python Program 
#Daniel ALlvarez 
#2/15/24


#exit code 

import sys 
def exit():
    sys.exit(0)
#welcome message
while True: 
    print("Welcome to Temperature Statistics, put in temperatures and we will print stats about them  :)") 
#input numbers into a list and convert it into an interger
    temp_nums = input("Enter temperature numbers seperated by commas: ")
    temp_nums_list = temp_nums.split(',')
    temp_nums_list = [int(i) for i in temp_nums_list]
#sort the output from lowest ouput to highest ouput 
    temp_nums_list.sort()
#calculate the average 
    average = sum(temp_nums_list) / len(temp_nums_list)
#Print the lowest temp, highest temp, and average temp 
    print(f"This is the lowest temperture: {temp_nums_list[0]}")
    print(f"This is the highest temperture: {temp_nums_list[-1]}")
    print(f"This is the average temperature: {average}")
 #ask the user if they want to repeat the code 
    restart = input("Do you want to restart the code?: ")
    new_restart = restart.lower()

    if new_restart == "yes":
        print("we restart")
    elif new_restart == "no":
        print("goodbye")
        exit()

    else: 
        print("hey you typed yes or no wrong retry")
    


