#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this lab is for lists
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#===============================================================
def main():
    n = int(input("What is the number of students:"))
    Names =[]#This generates a list 
    GPA = []
    g = 1
    h = 0
    for i in range(0,n):
        check = -1
        name = input(f"Input student #{g} name:") #{g} is in the loop for the number to increase after successfull loops
        Names.append(name)#this command adds the input to the list
        while check < 0:#this while loop is to check if the restart the input if the grade is not valid
            grade = float(input(f"Input student #{g} GPA:"))
            if grade <= 4.0 and grade >= 0: #This check if the grade is inbetween 4.0 and 0
                GPA.append(grade)
                check = check + 2
            else:
                print("A GPA must be in between 4.0 and 0 (both inclusive)! \n")
                check = -1
        g += 1
    print("=================== List ====================")
    print("\t  Name                   GPA")
    print("\t----------          -----------")    
    for i in range(0,n): #it was easier to copy this command line
        print("\t ",Names[h],"  \t\t ",GPA[h])
        h += 1 #would change the output of the list
    print("="*50)
    k = 0
    avg = 0
    for i in range(0,n):
        avg += GPA[k]
        k += 1
    average = avg/n
    print("The average of entered GPA is",average)
    print("The Maximum GPA is", max(GPA))
    print("The minimum GPA is", min(GPA))
    print("="*50)
            
        
        
main()
    