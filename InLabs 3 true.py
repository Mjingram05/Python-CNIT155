#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this leabs assignment is for more complex math operations
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
import math
def main():
    print(" \t Properties of a Truncated Cone")
    print("\t","-"*30)
    R1 = input("Enter a value for radius 1 (R1):")
    R1 = float(R1)
    H = input("enter a value for height of the cone:")
    H = float(H)
    S = input("Enter value for slant height of the cone")
    S = float(S) #S =float changes to state of S from a string to a float
    R2 = input("Enter a value for radius (R2):")
    R2 = float(R2)    
    print("_"*70, "\n")
    print("Calculating.. \n")
    V = 1/3*math.pi*H*((R1)**2+(R2)**2+R1*R2)# the ** means for a function to square root a number or variable
    V = float(V)
    print(f"The volume of the truncatedcone is: {V:.2f}")
    LA = S*math.pi*(R1+R2) #math. function goes into the math library to run a specific code like pi
    LA = float(LA)
    print(f"The lateral area of the truncated cone is: {LA:.2f}")
    TSA = LA+math.pi*((R1)**2+(R2)**2)
    TSA = float(TSA)
    print(f"the surface area of the truncated cone is: {TSA:.2f}")
    
    
    
main()