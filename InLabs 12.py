#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this lab is the final lab and is about exception
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#===============================================================
def StepsToMiles(lst): #this function will convert steps to miles
    i = 0
    miles_walked = []
    for i in range (len(lst)):
        Miles = lst[i]/2000
        miles_walked.append(Miles)
    return miles_walked #returns the list

def main():
    age = 1
    newage = 1
    lst = []
    print("*"*50)
    print("******* \t\t\t\t   *******")
    print("*******     Step to Miles calculator       *******")
    print("******* \t\t\t\t   *******")
    print("*"*50)
    while age <= 7:
        try:
            x = int(input(f"number of steps for day {age:.0f}:"))
            if x < 0:
                raise ValueError #raise valueerror will cause the exception to occur
            else:
                lst.append(x) #add the input function into the list
                age += 1
        except ValueError: #only activate if a valueerror is called
            print("\nException: wrong value entered")
            print("Please enter an integer value in a correct format!\n")
    StepsToMiles(lst)#calls the function
    miles = StepsToMiles(lst) #returned list if sent to an eaiser way to enter
    print("\n*** The number of miles you walked this week ***")
    for i in range(len(lst)):
        print(f"day {newage:.0f}  :  {miles[i]:.2f} miles")
        newage += 1
    total = sum(miles) #sum adds all entires in the list
    avg = total/7 #seven was the total amount due to them not changing
    print(f"The average of miles is {avg:.2f}")
    print("\n End of program")
    
main()