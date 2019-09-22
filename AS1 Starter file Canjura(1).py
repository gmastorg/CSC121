#Gabriela Canjura
#AS1 Starter file
#01/24/2018
#Asks user to choose either Celcius or Fahrenheit then converts input temp to that

def main():
    keepGoing='Y'

    while keepGoing == 'Y' or keepGoing == 'y':
        
        temp=mainMenu()
        
        if temp == 'C' or temp == 'c':
            degrees=getInput()
            toCelsius(degrees)
        else:
            if temp =='F' or temp == 'f':
                degrees=getInput()
                toFahrenheit(degrees)
            else:
                print ("Invalid option, try again.\n")
                temp=mainMenu()
                
        keepGoing = input("Would you like to go again Y/N? ")
        print('')
        
def mainMenu():
    print("To convert from Fahrenheit to Celsius type C.")
    print("To convert from Celsius to Fahrenheit type F.\n")
    temp=input("What would you like to convert your temperature to? ")
    print('')
    
    return temp

def toCelsius(degrees):
    celsius = float(0)
    celsius = (degrees-32) * (5/9)
    print(degrees,"degrees Fahrenheit equals", celsius,"degrees Celsius.\n")
    
def toFahrenheit(degrees):
    fahrenheit = float(0)
    fahrenheit = (degrees*1.8) + 32
    print(degrees,"degrees Celsius equals", fahrenheit,"degrees Fahrenheit.\n")

def getInput():
    degrees = float(input("Enter temperature: "))
    print('')
    return degrees
    
main()


