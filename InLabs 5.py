#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this inlab is for loops and using the "while" functions
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def main():
    age = 0
    while(age!=4): #While functions checks the code to see if it statement is meet
        print("\t \t While loop lab")
        print("="*50)
        print("1. all natural number between 1 and N")
        print("2. Display all even natural numbers from 1 to N. Compute their sum and average")
        print("3. Factorial of N")
        print("4. Exit")
        print("="*50)
        age = int(input("What option would you like to choose(1,2,3,4):"))
        if(age==4): #this is before everything to make sure the invalid statement doesn't appear.
            print("Goodbye!")        
        elif (age== 1):
            print("Option 1 selected: All natural numbers between 1 and N")
            N =int(input("Please input a natural number you want for N:"))
            i = 1
            while (i<=N):#this section will increase till is meets requirements
                print(i)
                i = i+1
        elif (age== 2):
            count = 1
            sum = 0
            counte = 0 #counte is sepreate to include into the average calculation
            print("Option 2 selected: Even natural from 1 to N and their sum and average")
            N =int(input("Please input a natural number you want for N:"))
            while count<=N:
                if count % 2 == 0:#if the count is divisble by two it will display the number
                    print(count, end= "\n")
                    sum +=count
                    counte += 1
                count = count + 1
            print(f"sum of the evens is: {sum}")
            avg = sum/counte
            print(f"The average of the even number are {avg:.1f}")
        elif (age==3):
            print("option 3 selected: facorial of N")
            N = int(input("Enter a natural number for N:"))
            i = 1
            f=1 #f is 1 here because mutipling by zero is zero
            while(i<=N):
                f *= i
                i = i+1
            print("The factorial of",N,"is",f)
        else:
            print("invalid option please choose a valid number")
            
        
        
            
    
    
main()