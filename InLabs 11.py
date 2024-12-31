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
    split=[]
    Title = []
    try:
        InputFile = open("books.txt", "r")
        OutputFile = open("books_analysis.txt","w")
        Input = InputFile.readlines()
        print("Printing the contents of the file....\n")
        print(Input)
        length = len(Input)
        OutputFile.write("=====Analysis Results======\n")
        OutputFile.write(f"\n1. The number of books in the file: {length:.0f}\n")
        OutputFile.write("\n2. Titles of Books with more than two words: \n\n")
        for i in range (length):
            newlist = Input[i] #creating a newlist by InputList section allows for the split function to work prefectly
            split_list = newlist.split(' ') #This sperates the section by spaces
            split.append(split_list) #This needs to be added to new list of find length of the section
            wordlen = len(split[i])
            if wordlen > 2:
                OutputFile.write(f"{Input[i]}") #this only print if the amount of words in a title exceeds 2
        OutputFile.write("\n\n3. Orginized Book Titles : \n\n")
        for i in range(length):
            name = Input[i]
            name = name.title() #capitalized the first word and decapatilze other words
            Title.append(name)
            OutputFile.write(f"{Title[i]}")
        
    
    
    except:
        print("The program failed to open the file. Make sure of following: \n \t The file to read is located in the same folder where the program is! \n\tThe file's name is spelled correctly!")
main()