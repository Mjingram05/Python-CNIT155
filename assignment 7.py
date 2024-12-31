#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this assignments is for user defined functions
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#===============================================================
def displayMyInfo():
    print("-"*49)
    print("| \t \t   Mason Ingram  \t \t|")
    print("| \t \tIngram61@purdue.edu \t \t|")
    print("| \t \tCNIT155 Assignment 07 \t \t|")
    print("-"*49)
displayMyInfo()
def factorial(n):#these user-defined function allow other people to easily know what this section is created for
    i = n #this line here just help me with the for i in range function
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact #return function send the output of the defined section
def maximumNo(x,y,z):
    highest = max(x,y,z) #max() function takes a look to see what is the highest number in the range
    return highest
def digits(x):
    s = 0
    for i in x:
        s += 1
    return s
def main(): #this function doesn't show anything unless the print function is in it
    flag = True
    while flag == True:
        age = 0
        print("============== User Defined Functions Menu ===============")
        print("1. Compute n Factorial")
        print("2. Find the Maximum")
        print("3. Find the number of digits")
        print("4. Exit")
        print("="*59 )
        age = int(input("please choose a User Defined Function:"))
        if age == 4:
            flag = False
            print("goodbye")
        elif age == 1:
            n = int(input("Enter a natural number of N:"))
            factorial(n)#this calls the function and (n) is the variable being used for the factorial equation
            print(f"The factorial of {n:.0f} is {factorial(n):.0f}")#the whole function had to be included for the program in the {factorial(n)} to display the correct number
        elif age == 2:
            x = int(input("Enter the 1st number:"))
            y = int(input("Enter the 2nd number:"))
            z = int(input("Enter the 3rd number:"))
            maximumNo(x,y,z)#the list here will use all the input vaiables and send it the the called function
            print(f"The greastest number among the three number: {maximumNo(x,y,z):.0f}")
        elif age == 3:
            x = input("Enter a Natural number for N:")
            digits(x)
            print("The number of digits in", x, " is", digits(x))
        else:
            print("Invalid input, please choose and option between 1 and 4")
            
                    
                  
        


main()
    

    
