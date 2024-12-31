#===============================================================
# Your Name & Lab Section: (ex: Purdue Pete, Friday 1:30pm)
# Your Purdue Email:
# Program Description: This program is to understand the concept of pythons variables like string, int, float, and
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def main():
    print("This is InLab02 for CNIT by Mason Ingram")
    
    v1 = input ("How many students are in CNIT 155:") #input allows user to add their own values in the Debug window
    v1 = int(v1) # this line of code forces the variable to be a integer rather than a string
    print(" The number of student in CNIT 155 is", v1)
    print(" the data type of the number of students is", type(v1)) #the type command looks at the variable to see if it's 
    
    #price and float
    v2 = input ("Enter the price of the textbook:")
    v2 = float(v2) #float is a integer with decimals
    print(" The number of student in CNIT 155 is", v2)
    print(" the data type of the number of students is", type(v2))
    
    #Fahrenheit to Celcius
    v3 = input ("What is todays temperature in Fahrenheit (°F):")
    v3 = float(v3)
    cel = (v3-32)*(5/9.0)
    cel = float(cel)
    print(f"The temperature in Celsius (°C) is {cel:.2f}°C")
    print("the data type of the temperature is", type(cel))
    
    #average speed
    v4 = input ("Enter the distance travelled by car in miles:")
    v4 = float (v4)
    v5 = input ("Enter the duration of the trip in hours:")
    v5 = float (v5)
    v6 = v4/v5
    v6 = float(v6)
    print(f"The average speed of the car for the trip is {v6:.2f} miles/hour")
    print(" the data type of the temperature is", type(v6))
    
main()