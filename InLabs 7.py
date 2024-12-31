#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this assignments is for loops and while loop
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#===============================================================
import math
def displayMyInfo():
    print("\t",("*"*25))
    print("\t *   Mason Ingram \t *")
    print("\t *   Ingram61@pudue.edu\t *")
    print("\t *   CNIT155 InLab07 \t * ")
    print("\t","*"*25)
displayMyInfo() # this is to ensure that it doesn't get called back
def validate(a,b,c):
    d = a+b
    print("Validating a triangle.....") 
    if d>c:
        return True  #return overrides the need for def function     
    else:
        return False #return false will input to line 36
        
def ComputePerimeter(a,b,c):
    p = a+b+c
    return p
def main():
    choice = True # this is just set to define choice
    flag = True
    while flag == True:
        x = float(input("Enter length of side x:"))
        y = float(input("Enter length of side y:"))
        z = float(input("Enter length of side z:"))
        if (validate(x,y,z) == True): #if the the validate function is true then it will print the perimeter
            print(f"The perimeter of the triangle is {ComputePerimeter(x,y,z):.2f}")
            print("")
            choice = True #This will cause while choice is loop to run
        else:
            print("Invalid input Please enter valid number")
            flag = True
            choice = False # choice = false will cause the main input function to run again
        while choice == True:
            age = input("Do you want to compute again? (Y/N):")
            if age == ("Y") or age==("y"):
                choice = False              
            elif age == "N" or age =="n":
                print("End of Program")
                choice = False
                flag = False
            else: #else if for anything other than Y or N
                print("Invalid input")
                choice = True
                Flag = False
main()
    