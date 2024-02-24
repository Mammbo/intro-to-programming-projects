#M4 Project 4-5: Dice Roller  
#Daniel Alvarez 
#2/18/24

#for random output 
import random 
# Create a function that rolls a single dice 
def die1(): 
    return random.randint(1, 6)
# Create a function that rolls the seconds die  
def die2():
   return random.randint(1, 6)
# Have code loop with a while lop and gives user the option to break out
while True: 
## calculates if a special message is needed to be displayed for two ones or two sixes and calculates and displays the dice values and total 
    def main():
        num = die1() 
        num2 = die2()
        result = num + num2 
        print(f"\nDie 1: {num} \nDie 2: {num2} \nTotal: {result}")

        if num == 1 and num2 == 1: 
            print("SnakeEyes!")
        elif num == 6 and num2 == 6:
            print("Boxcars!")
        else: 
            print("")
# Display welcome messge
    print("Hello Welcome to Dice Roller!!")
#run through code and offer restart or end
    roll = input("\nRoll the dice? (y/n): ")
    new_roll = roll.lower()

    if new_roll == "y": 
        main()
    elif new_roll == "n":
        break
    else: 
        print("You typed wrong try again")





