# creates a shell that calls funtions and runs a loop
# 02/05/2018
# CSC-121 In Class
# Gabriela Canjura

def main():

    keepGoing = "Y"

    while keepGoing == "Y":

        mainMenu()

        keepGoing = input("Would you like to keep going? (Y/N)")
        keepGoing = keepGoing.upper()

def mainMenu():

     print("1. Calculate Celsius")
     print("2. Calculate Fahrenheit")
     print("3. Addition")
     print("4. Multiplication")
     print("5. Division")
     print("6. Subtraction\n")

     selection = int(input("What would you like to do? "))

     if selection == 1:
         calcCelsius()
     elif selection == 2:
         calcFahr()
     elif selection == 3:
         calcAdd()
     elif selection == 4:
         calcMult()
     elif selection == 5:
         calcDiv()
     elif selection == 6:
         calcSub()
     else:
         print ("Invalid option, try again.\n")
         temp=mainMenu()

def calcCelsius():
                            
    print("Celsius")

def calcFahr():
    print("Fahrenheit")

def calcAdd():
    print ("Addition")

def calcMult():
    print ("Multiplication")
           
def calcDiv():
    print ("Division")       

def calcSub():
    print ("Subtraction") 

main()   
        
