#Gabriela Canjura
#AS1 Starter file
#01/24/2018
#Asks user to choose either Celcius or Fahrenheit then converts input temp to that

def main():
    keepGoing = 'Y'

    while keepGoing == 'Y':
        
        mainMenu()
                      
        keepGoing = input("Would you like to go again? (Y/N) ")
        keepGoing = keepGoing.upper()
        
        print('')
        
def mainMenu():
    print("To convert from Fahrenheit to Celsius type C.")
    print("To convert from Celsius to Fahrenheit type F.\n")
    temp=input("What would you like to convert your temperature to? ")
    temp = temp.upper()
    print('')
    
    if temp == 'C':
        toCelsius()
    else:
        if temp =='F':
            toFahrenheit()
        else:
            print ("Invalid option, try again.\n")
            temp=mainMenu()
    

def toCelsius():

    degrees=getInput()
    celsius = (degrees-32) * (5/9)
    print(degrees,"degrees Fahrenheit equals", celsius,"degrees Celsius.\n")
    
def toFahrenheit():

    degrees=getInput()
    fahrenheit = (degrees*1.8) + 32
    print(degrees,"degrees Celsius equals", fahrenheit,"degrees Fahrenheit.\n")

def getInput():

    degrees = float(input("Enter temperature: "))
    print('')
    return degrees
    
main()


