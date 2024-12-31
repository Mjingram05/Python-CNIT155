#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this program to impot math operation
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
import math #this code imports the math library for more complex equations
print("+"*33)
print("+\t     Mason \t\t+")
print("+\t ingram61@purdue.edu \t+") 
print("+\t CNIT155 Assignment 4 \t+")
print("+"*33)
print("\n Second degreee quadratic equation roots calculator: aX^2+bX+c = 0")
a = float(input("\t Enter the coefficient a:"))
b = float(input("\t Enter the coefficient b:"))
c = float(input("\t Enter the coefficient c:"))
print(f"\t Quadratic Equation is: {a:.1f}x^2 + {b:.1f}x + {c:.1f} = 0")
d = ( (b**2)-4*a*c)
print(f"\tThe Discriminat is: {d:.3f}")
print("\n Calculating the roots........... \n")
if  d > 0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)    
    print(f"\tThe equation has two real root: {x1:.3f} and {x2:.3f}")
    V = min([a,b,c])
    print(f"\tThe smallest coefficeint is: {V:.2f}")    
elif d == 0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)    
    print(f"\tThe equation has one real root: {x1:.3f}")
    V = min([a,b,c])
    print(f"\tThe smallest coefficeint is: {V:.2f}")    
else:   
    print("\t The equation has no real roots.")
    V = min([a,b,c])
    print(f"\tThe smallest coefficeint is: {V:.2f}")