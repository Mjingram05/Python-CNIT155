#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this lab is for function for enhanced lists
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#===============================================================
def USDtoYuan(USD):
    Yuan = []
    length = len(USD)
    h = 0
    for i in range (0,length):
        con = 7.21*USD[h]
        Yuan.append(con)
        h+=1
    return Yuan
def PrintInfo(USD, Yuan): #Yuan was created in function USDtoYuan
    h = 0
    length = len(USD)
    print("\t USD \t\t Yuan")
    print("#"*45)
    for i in range (0,length):
        print(f"\t{USD[h]:.2f} \t\t {Yuan[h]:.2f}")
        h += 1
    print("#"*45)
def Average(Lst): #Lst is created by change input in main
    h = 0
    total = 0
    length = len(Lst)
    for i in range(0, length):
        total += Lst[h]
        h += 1
    avg = total/length
    return (avg) #return function is for calling the function 
def FindPrice(USD, Yuan):
    action = 0
    print("########Price(s) under $70 is(are)#########")
    print("\t USD \t\t Yuan")
    print("\t-----\t\t------")
    length = len(USD)
    for i in range (0,length):
        if USD[i] < 70:#i is used here to make sure the sure the list does not go beyond limit 
            print(f"\t {USD[i]:.2f} \t\t {Yuan[i]:.2f}") #the print function must happen here due to it satifify the if clause
        else:
            action += 2
    
def main():
    USD = []
    action = 0
    List = "l"
    while action < 1:
        List = (input("Enter a price is USD. Use NN or nn to stop data entry:"))
        if List == ("NN") or List == ("nn"):
            action += 2         
        elif List != ('NN') or  List != ('nn'):
            Lst = int(List)
            USD.append(Lst)
    length = len(USD)
    print("Number of prices entered:",length)
    USDtoYuan(USD)
    Yuan = USDtoYuan(USD) #this make the list easier to call
    PrintInfo(USD, Yuan) #if the full length of Yuan was called would create an error
    Lst = USD
    Average(Lst)
    print("######## Averages #########") #for some reason this print line would happen twice if it was in the average function
    print(f"The averge of USD is {Average(Lst):.2f}")
    Lst =Yuan
    Average(Lst)#doing this changes Lst to satifify the one list input for average
    print(f"The averge of Yuan is {Average(Lst):.2f}\n\n")
    FindPrice(USD,Yuan)
main()
        