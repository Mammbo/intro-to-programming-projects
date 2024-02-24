#Title: Project 3-1: Letter Grade Converter 
#Daniel Alvarez 
#2/18/24


#fuction that takes  users input and translates the letter grade
def grade_convertor(grade):
    if grade >= 88 : 
        print("Letter Grade: A")
    elif grade >= 80 : 
        print("Letter Grade: B") 
    elif 79 <= grade or grade >= 67 : 
        print("Letter Grade: C")
    elif 66 <= grade or grade >= 60:
        print("Letter Grade: D")
    else: 
        print("Letter Grade: F")
#Welcome message 
print("Letter Grade Convertor")
#while loop to loop the code until you want to stop 
while True: 
    start_stop = input("\nGrade Conversion? (y/n):")
    new_start_stop = start_stop.lower()
#continue code and run conversion via a variable with user input and then putting that into the grade convertor 
    if new_start_stop == "y":
        value = float(input("What is your numerical grade?: "))
        grade_convertor(value)
#break out of code and goobye :) 
    elif new_start_stop == "n":
        print("Bye!")
        break
#if you type something wrong, there will be a case to catch it and stop it 
    else: 
        print("Hey you typed y or n wrong, retype it and try again. :)")
        

#


 