import math
def main():
    age = 0 #age must be zero to insure that an error does not happen
    while(age!="E"):
        print("\t\t While Loops")
        print("*"*50)
        print("A. Sum of odd natural number from 1 to N")
        print("B. Sum of cubes of odd natural number from 1 to N")
        print("C. Check if a natural number N is a prime number")
        print("D. Print the multipliation table of N")
        print("E. Exit")
        print("*"*50)
        age = input("Choose one of the options to preform:")
        if (age== "E"):
            print("Goodbye!")
        elif (age == "A"):
            print("option A selected")#option selected was for user feedback
            N = int(input("Enter natural number for N:"))
            i = 1
            sum = 0
            print("displaying odd natural number from", i, "to", N)
            while (i<=N):
                if i % 2 != 0:#if the count is divisble by two it will display the number
                    print(i, end= "\n")
                    sum +=i    
                i = i+1
            print(f"The sum of odd natural number from 1 to {N:.0f} is {sum:.0f}")
        elif (age == "B"):
            print("Option B selected")
            N = int(input("Enter natural number for N:"))
            i = 1
            l = 1
            sum = 0
            print("displaying odd natural number from", i, "to", N)
            while (i<=N):
                if l % 2 != 0:
                    print(l, end= "\n")
                
                i = i + 1
                l = i**3
                    
        elif (age == "C"):
            print("Option C selected")
            N = int(input("Enter natural number for N:"))
            f = 0
            i = 2
            while i <= N/2:
                if N%i==0:#this section will check for prime numblers
                    f=1
                i=i+1
            if f==0:
                print(N, "is a prime number")
            else:
                print(N,"is not a prime number")
        elif (age=="D"):
            print("Option D selected")
            N = int(input("Enter natural number for N:"))
            print("Multiplication table of", N)
            i = 1
            while(i<=10):
                Ni = N * i
                print(f"{N:.0f} x {i:.0f} = {Ni:.0f}")
                i = i + 1          
        else:
            print("none valid option")                
main()  