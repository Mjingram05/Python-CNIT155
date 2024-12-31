#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this lab is for function for pulling files from downloads
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#===============================================================
def main():
    try: #ensures the program does not crash if it does not complete task
        h = 0
        total = 0
        lst = []        
        InputFile = open("scores.txt", "r")  # Open the file for reading
        OutputFile = open("scores_stat.txt", "w") # open the new file to write in
        content = InputFile.readlines() #read the line of the file
        num_lst= content[3:]
        length = len(num_lst)
        for i in range(length):
            h = float(num_lst[i])
            lst.append(h)
        print("Printing the contents of the file...\n")
        print(lst)
        big = max(lst)
        small = min(lst)
        long = len(lst)
        for i in range(length):
            total += lst[i]
        avg = total/length
        OutputFile.write("The largest number in the set is " +str(big)) #writes this line into the new file
        OutputFile.write("\nThe smallest number in the set is " +str(small))
        OutputFile.write("\nThe number of score in the list is " +str(long))
        OutputFile.write("\nThe average number of scores in the set is " +str(avg))        
        
        
        InputFile.close
        OutputFile.close
        
        
    except:
        print("The program failed to open the file. Make sure of following: \n \t The file to read is located in the same folder where the program is! \n\tThe file's name is spelled correctly!")
main()