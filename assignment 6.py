#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this assignments is for loops and using the "for" functions
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#===============================================================
def main():
    age = 0 #age must be defined in order for the program not to crash
    while(age!="E"):
        print("For Loops Assigment \n")
        print("=" * 30)
        print("\n A. Display natural number from N1 to N2, Where N2>N1")
        print("\n B. Find the Factorial of N")
        print("\n C. Display right rangled triangle of Stars")
        print("\n D. Display centered triangle of Stars")
        print("\n E. Exit")
        age = input("Enter an option:")
        if(age == "E"): #I find putting this infront makes it easier to work with
            print("Goodbye!")
        elif(age == "A"):
            print("Option A selected")#for user feedback to confirm option
            x = 0
            while (x!= 1): #I have the while function for a bit of flair and allowing user to continusly input number if N2 < N1
                N1 = int(input("Enter a natural number for N1:"))
                N2 = int(input("Enter a natural number for N2:"))
                i = N1
                if (N2>N1): #if N2 < N1 then there would be no list of odd numbers
                    print(f"Displaying Odd natural number from {N1:.0f} to {N2:.0f}")
                    for i in range (N1,N2+1):
                        if i %2 != 0: #%2 = 0 display even number making it not equal zero will display odd numbers
                            print(i, end= "\n")
                            i = i+1
                    x = x+1
                else:
                    print("Invalid! \n N2 must be greater than N1")
                    print("Please enter number for N1 and N2 again")
        elif(age=="B"):
            print("Option B selected")
            factorial = 1
            x=0
            while(x!=1):
                N1 = int(input("Enter a natural number for N1:"))
                if N1 < 0:
                    print("Sorry, N1 can't be negative\n")
                    H = input("Want to enter it again, Y or N:")
                    if H=="Y": #some more flair to make sure user can still input with out restarting the program
                        print("\nPlease enter a positive number\n")
                    elif H=="N":#this action will close the factorial calculator than the entire program
                        print("Ok, Goodbye!\n\n")
                        x = x+1
                elif N1==0:
                    print("The factorial of 0 is 1")
                    x = x+1
                else:
                    i = N1
                    for i in range(1, N1+1):
                        factorial = factorial*i
                    print(f"The factorial of {N1:.0f} is {factorial:.0f}")
                    x = x+1 #this path will close the factorial calculator due to a successful operation
        elif (age=="C"):
            print("Option C selected")
            N = int(input("Enter a number of rows to print triangle of number:"))
            i = 1
            for i in range(1,N+1):
                print("*"*i)
                i = i+1
        elif (age=="D"): #I want to have age be two different option but it let to option A only being choosed
            print("Option D selected")
            N = int(input("Enter a number of rows to print *s:"))
            print("Centered Triangle of Stars with",N,"Rows:")
            i=1
            k=0
            for i in range(1, N+1):
                for space in range(1, (N-i)+1):
                    print(end=" ")
                while (k!=2*i-1):
                    print("*",end="")
                    k+=1
                
                k=0
                print()
        else:
            print("\nInvalid option!\n")
            print("please enter a valid option\n")# the \n is to clean up the debug I/O
            
main()