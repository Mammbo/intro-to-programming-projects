#Quadratic Equation Calulatorf
#Daniel Alvarez
#2/8/24

import cmath
#title 

#print quad equation out and ask what are the inputs for that quad eqaution 

print("ax^2 + bx + c = 0")
print("a:\nb:\nc:")

a = float(input('What is the value for a?: '))
b = float(input("What is the value for b?: "))
c = float(input("What is the value for c?: "))

print("Here is your formaula:", a,"x^2 +", b, "x +", c, "= 0")
print("Andddd them listed out") 
print("a = ", a, "b = ", b, "c = ", c)

#calculate values in the quad equation 
#complex solutions
if (b**2 - 4*a*c) > 0:
  x1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
  x2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)
 
  print(f"x1 = {x1}")
  print(f"x2 = {x2}")
  
else: 
  x1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
  x2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)
  print(f"x1 = {x1}")
  print(f"x2 = {x2}")
 