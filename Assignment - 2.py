#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email:
# Program Description: this program is to build upon InLab 2 on conversion rate
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def main():
    print("*"*42)
    print("* \t  CNIT155 Assignment 02 \t *")
    print("* \t \t \t \t \t *")
    print("* \t  Conversion Calculator \t *")
    print("*"*42)
    name = input("Enter your full name:")
    print("My name is", name, "\n")
    
    print("**1st, Pounds to Kilograms conversion** \n" )
    
    lb = input ("The amount of pounds to convert to Kilograms:")
    lb = float(lb)
    kg = (lb/2.2046)
    kg = float(kg)
    print(f"The weight entered in pounds is {lb:.2f} lbs and it is {kg:.2f} kg \n")
    
    print("**2nd. Celsuis to Fahrenheit conversion** \n")
    
    C = input ("the current temperature in Celcuis:")
    C = float(C)
    F = (C*(9/5)+32)
    F = float(F)
    print(f"The entered temperature in Celcuis is {C:.2f} °c and Fahrenheit is {F:.2f}°F \n")
    
    print("**3rd. Miles to Kilometers conversion** \n")
    
    m = input ("Enter miles to convert it to kilometers:")
    m = float(m)
    km = (m*1.609344)
    km = float(km)
    print(f"The entered distance in miles is {m:.2f} mi and in Kilometers {km:.2f} \n")
    
    print("**4th. Yard to Meters conversion** \n")
    
    yd = input("Enter yard to convert it to meters:")
    yd = float(yd)
    Met = (yd*0.9144)
    Met = float(Met)
    print(f"The entered distance in yards is {yd:.2f} yds and in meters {Met:.2f} m \n")
    
    print("**5th. Feet and Inches to Centimeters** \n")
    
    print("What is you height in Feet and Inches:")
    Ft = input("Feet?:")
    Ft = int(Ft)
    inch = (Ft*12)
    inch = float(inch)
    In = input("Inches?:")
    In = int(In)
    tol = (inch+In)
    tol = float(tol)
    Cen = (tol*2.54)
    Cen = float(Cen)
    print("The entered distance in", Ft,"feet", In,f"inches and in centimeters {Cen:.2f} cm \n")
    
    
main()