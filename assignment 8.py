#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this lab is funct lists
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#===============================================================
def Discount(Prices):
    length = len(Prices)
    update = [] #a new list must be created due drastic changes to the original list
    h = 0
    for i in range(0,length):
        dis = Prices[h] * 0.3
        new = Prices[h] - dis
        update.append(new)
        h +=1
    return update #this returns the new list for use
def PrintInfo(Names, IDs, Prices): #No return function is required for this function
    length = len(Names)
    h = 0
    n = 0
    print("\t Names \t\t ID \t Price")
    print("="*70)
    for i in range(0,length): #it was easier to copy this command line
        print("\t ",Names[h], "\t", IDs[h],f"\t {Prices[h]:.2f}")
        h += 1 #would change the output of the list
def Average(Prices):
    length = len(Prices) #check the  the amount of entries in the list
    k = 0
    avg = 0
    for i in range(0,length): #length is input here for if the list is extend or decreased the code will not break
        avg = avg + Prices[k]
        k += 1
    total = avg/length
    return total
def Search(Names, IDs, discount, avgDis): #this function checks to see if the discount price is less than avgDis and print it
    length = len(Names)
    h = 0#this is for making sure the variable is ready
    k = 0
    print("\t Names \t\t ID \t Price")
    print("="*70)    
    for i in range(0,length):
        if discount[h] <= avgDis: #check if the prices is less the average price and prints
            print("\t ",Names[h], "\t", IDs[h],f"\t {discount[h]:.2f}")
        h += 1
def main():
    print("*"*36)
    print("*******    Assignment 08    ********")
    print("*"*36)
    Names = ["Paint Brush","Sander","Hand Drill","Vac Cleaner","Roller","Chainsaw"] #The list will remain the same end does not require input
    IDs = [3750,4389,3986,9562,1967,2988]
    Prices = [12.99,82.49,117.89,178.99,57.49,199.99]
    PrintInfo(Names, IDs, Prices)
    Average(Prices) #calls the function and sends the list to it
    print("*"*45)
    print("================   Averages   ===============")
    print(f"The average prices before the Discount is ${Average(Prices):.2f}\n")
    print("*"*45)
    Discount(Prices)
    print("Prices have been adjusted!")
    PrintInfo(Names, IDs, Discount(Prices)) #the full function has to be stated for the return function to work
    discount = Discount(Prices) # this line make it easier to call the output
    print("*"*45)
    Average(Discount(Prices)) 
    avgDis = Average(Discount(Prices)) #this make it easier to transfer the data to other functions
    print("================   Averages   ===============")
    print(f"The average prices before the Discount is ${Average(Discount(Prices)):.2f}\n")
    print(f"======= Products under <= {avgDis:.2f} ========")
    Search(Names, IDs, discount, avgDis) #making the output in smaller calling output makes it easier to move between function
    
    
    
main()
        


        
    