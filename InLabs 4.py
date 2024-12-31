#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this program is for complex if statements and math problems
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
import math #this code imports the math library for more complex equations
def main():
    print("===========Menu===========")
    print("\n     Interest Calculator")
    print("="*26)
    print("A. Simple intrest calculator")
    print("B. Compund intrest calculator")
    print("="*26)
    H = input("What calculator would you like to use? Please type A or B:")
    if H =='A':
        print("you chosed option A, simple intrest calculator")
        P = float(input("Enter the inital amount of principal balance:"))
        r = float(input("Enter the intrest rate in percentage form:"))
        t = float(input("Enter the number of time period to elapse:")) #float(input) automatily make the input a float type
        rt = (r*t)
        a = P*(1+((rt)/100))
        a =float(a)
        print(f"the total amount of simple intrest is :{a:.2f}") # {a:.2f} makes the float round to two decimals
    elif H=='B': #elif doesn't check if the previous if statement was succesful
        print("you have chosen B, compound intrest calculator")
        P = float(input("Enter the inital amount of principal balance:"))
        n = float(input("Enter the number of terms per year:"))
        r = float(input("Enter the intrest rate in percentage %:"))
        t = float(input("enter the time in years:"))
        T = n*t #this was to make the full operation easier on the eyes
        O = (1+(r/(100*n)))
        K = math.pow(O, (T)) #math.pow is the allow a variable to be x ^ Y
        A = P*K
        print(f"the final amount of intrest is: {A:.2f}")
    else:
        print("invalid input")
        print("please chose A or B")
    
        
    
main()