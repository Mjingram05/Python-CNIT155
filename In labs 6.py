#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this inlab is for loops and using the "for" functions
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def main():
    age = 0
    while age != 4: # the while function is the only way to create a looping system
        print("*"*50)
        print("\t \t For Loops lab")
        print("*"*50)
        print("\n 1. Display and Add Even number from 1 to N")
        print("\n 2. Multiplication table of N")
        print("\n 3. Print Triangle of Numbers")
        print("\n 4. Exit")
        print("*"*50)
        age = int(input("Choose one of the options to preform:"))
        if (age==4): #I find putting the ending loops option first get consitance result
            print("goodbye")
        elif (age == 1):
            print("option 1 selected")
            N = int(input("Enter a natural number for N:"))
            print("Displaying even number from 1 to", N)
            count = 1
            sum = 0
            i = 1
            for i in range (1,N+1): #N need a +1 to ensure the range gets the desired number
                if i % 2 == 0:#if the count is divisble by two it will display the number
                    print(i, end= "\n")
                    sum += i
                    i = i+1
            print(f"sum of the evens is: {sum}")
                    
        elif (age==2):
            print("Option 2 selected")
            N = int(input("Enter a natural number for N:"))
            print("Multiplication table of", N)
            i = 1
            for i in range (1,11): #N+1 is not required here due to having a set multiplication table
                Ni = N * i
                print(f"{N:.0f} x {i:.0f} = {Ni:.0f}")
                i = i + 1
        elif (age==3):
            print("option 3 selected")
            N = int(input("Enter a number of rows to print triangle of number:"))
            i = 1
            for i in range(1,N+2):#two for functions was required to create the triangle 
                for j in range (1, i):
                    print(j, end='')
                print()
        else:
            print("Invalid optio!n")
            print("Please choose and option between 1 and 4 \n")
            
            
                
    
    
    
main()
    