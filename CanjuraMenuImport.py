# creates a shell that calls funtions and runs a loop
# 02/05/2018
# CSC-121 In Class
# Gabriela Canjura

import functions 

def main():
      
    keepGoing = "Y"
    
    while keepGoing == "Y":
     
        mainMenu()

        keepGoing = input("Would you like to keep going? (Y/N)")
        keepGoing = keepGoing.upper()
        print("")

def mainMenu():

    print("1. Calculate Celsius")
    print("2. Calculate Fahrenheit")
    print("3. Addition")
    print("4. Multiplication")
    print("5. Division")
    print("6. Subtraction\n")

    selection = int(input("What would you like to do? \n"))

    if selection == 1:
      functions.calcCelsius()
    elif selection == 2:
        functions.calcFahr()
    elif selection == 3:
        functions.calcAdd()
    elif selection == 4:
        functions.calcMult()
    elif selection == 5:
        functions.calcDiv()
    elif selection == 6:
        functions.calcSub()
    else:
        print ("Invalid option, try again.\n")
        temp=mainMenu()

main()   
        
