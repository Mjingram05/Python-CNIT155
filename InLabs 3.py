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
def main():
    D1 = input("Enter a value for Depth 1 (D1):")
    D1 = float(D1)
    D2 = input("Enter a value for Depth 2 (D2):")
    D2 = float(D2)
    if  D2 > D1:
        W = input("Enter a value for the width (W):")
        W = float(W)
        L = input("Enter a value for the length (L):")
        L = float(L)
    else:
        print("Invalid input! D2 must be greater than D1!")
        
    SD = (D1+D2)*(L/2)
    SD = float(SD)
    print(f"the sides of the pool are :{SD:.2f}")
    
    D3 = D2-D1
    D3 = float(D3)
    
    HYP = math.sqrt(((D3)**2)+((L)**2))
    print(f"The bottom area of the pool is :{HYP:.2f}")
    
    
main()