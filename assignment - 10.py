#===============================================================
# #Mason Ingram Lab section: 13316-010
# Your Purdue Email: ingram61@purdue.edu
# Program Description: this lab is for adding list from other files
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#================================================================
from graphics import *
from button import *

def main():
    
    Window = GraphWin("#Assignment 10", 600, 450)
    
    title = Text(Point(220,25), "#Manipulating String in Python")
    title.setSize(20)
    title.setStyle("bold")
    title.setTextColor("purple")
    title.draw(Window)
    
    label1 = Text(Point(110,60), ("Enter a title of a book :"))
    label1.setSize(15)
    label1.setStyle("bold")
    label1.draw(Window)
    
    inputBox = Entry(Point(350,60), 20)
    inputBox.setSize(15)
    inputBox.setFill("white")
    inputBox.draw(Window)
    
    display = Rectangle(Point(15,100), Point(410, 350))
    display.setFill("white")
    display.draw(Window)
    
    btn = Button(Window, Point(530, 60), 50, 30, "Enter")
    btn.activate()
    
    quit = Button(Window, Point(530, 100), 50, 30, "Quit")
    quit.activate()
    
    rst1 = Text(Point(200, 110), "")
    rst1.setSize(15)
    rst1.draw(Window)
    
    rst2 = Text(Point(200, 130), "")
    rst2.setSize(15)
    rst2.draw(Window)
    
    rst3 = Text(Point(210, 150), "")
    rst3.setSize(15)
    rst3.draw(Window)
    
    while True:
        p = Window.getMouse()
        if btn.clicked(p):
            split = []
            List1 = []
            
            display = Rectangle(Point(15,100), Point(410, 350))
            display.setFill("white")
            display.draw(Window)            
            
            string=inputBox.getText()
            
            lowercase = string.count('a')
            uppercase = string.count('A')
            total = lowercase + uppercase
            
            String = string.title()
            
            List1.append(string)

            for i in range (len(List1)):
                List1.append(string)
                split_list = string.split(" ")
                split.append(split_list)                
                Length = len(split[i])
            rst1 = Text(Point(200, 110), f"The Title is.... : {String}")
            rst1.setSize(15)
            rst1.draw(Window)
            
            rst2 = Text(Point(200, 130), f" There is/are {total:.0f} A/a(s).")
            rst2.setSize(15)
            rst2.draw(Window)
            
            rst3 = Text(Point(210, 150), f"The number of words in the string is/are : {Length:.0f}")
            rst3.setSize(15)
            rst3.draw(Window)

            
        elif quit.clicked(p):
            return False
    
    
main()