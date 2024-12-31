#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this lab is for adding list from other files
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#===============================================================
def main():
    try:
        trail = []
        Temp = []
        Names = []
        Scores = []
        Upscore=[]
        Letgrad=[]
        InputFile = open("input.txt", "r")
        OutputFile = open("output.txt", "w") #Opens a new file to write in
        Input = InputFile.readlines()
        for i in range(len(Input)):
            h = Input[i]
            Temp.append(h)
            x = Temp[i]
            split_list = x.split(',') #this splits list by the the comma
            name = split_list[0] #each section in put into their own list
            nums = float(split_list[1])
            name = name.title()
            Names.append(name)
            Scores.append(nums)
        print("Printing every content in the file......")
        print(Names)
        print(Scores)
        for i in range(len(Scores)):
                score = Scores[i]
                if score < 4.0:
                        score +=0.1
                        Upscore.append(score)
                else:
                        Upscore.append(score)
        for i in range(len(Upscore)):
                grade = Upscore[i]
                if grade > 3.7 and grade < 4.0: #the section must be inbetween or all letters will be applied
                        Let = "A"
                        Letgrad.append(Let)
                elif grade > 3.5 and grade < 3.7:
                        Let = "B"
                        Letgrad.append(Let) 
                elif grade > 3.0 and grade < 3.5:
                        Let = "C"
                        Letgrad.append(Let)
                elif grade > 2.5 and grade < 3.0:
                        Let = "D"
                        Letgrad.append(Let)
                else:
                        Let = "F"
                        Letgrad.append(Let)
        big = max(Scores)
        OutputFile.write("Maximum score is :" +str(big))
        OutputFile.write(f"\n{Names[2]}, {Scores[2]:.1f}") #had to write specific location due too both list being sepreate
        OutputFile.write(f"\n{Names[4]}, {Scores[4]:.1f}")
        OutputFile.write(f"\n{Names[9]}, {Scores[9]:.1f}")
        OutputFile.write("\n\nUpdated score(s) with letter grade:")
        for i in range(len(Names)):
                OutputFile.write(f"\n{Names[i]}, {Upscore[i]:.2f}, {Letgrad[i]}") #running this command in a loop will auto write the list
        
        InputFile.close #closes the files from the program
        OutputFile.close
                               
            
        
    except:
        print("The program failed to open the file. Make sure of following: \n \t The file to read is located in the same folder where the program is! \n\tThe file's name is spelled correctly!")
main()