#Gabriela Canjura
#CSC 121_
#04/06/2018
#uses info from text file to create dictionaries and then display specific info

def main():

    keepGoing = "Y"

    while keepGoing == "Y":

        createDictionaries()

        keepGoing = input("\nWould you like to see another year? (Y/N)")
        keepGoing = keepGoing.upper() 
    
def createDictionaries():

    teams = []
    year = []
    count = {}
    years = {}
    

    infile = open('WorldSeriesWinners.txt', 'r')

    teams = infile.readlines()

    infile.close()

    index = 0

    y = 1902
    
    while index < len(teams):
        #creates a list from file
        teams[index] = teams[index].rstrip('\n')

        #gets the corresponding years for the teams
        #skips 1904 and 1994 as no world series were played these years
        if y == 1903 or y == 1993:
            y = y+2
        else:
            y+=1

        #makes y an element of list year
        year.append(y)
        
        index+=1

    #gets count of times a name shows up on the list teams
    #and creates a dictionary with the names as keys and the number
    # of times as the value
    count = dict([x,teams.count(x)] for x in set(teams))

    #takes list of years and list of teams and makes them into a dictionary
    years = dict(zip(year,teams))

    displayInfo(count, years)

def displayInfo (count, years):

    print("\nEnter a year to see which team won the world"+
        " series and how many times they won.\n" )

    userYear = int(input("Enter a year between 1903 and 2009: \n"))
 
    while userYear < 1903 or userYear > 2009:

        userYear = int(input("\nPlease enter a year between 1903 and 2009: \n"))

    while userYear == 1904 or userYear == 1994:

        userYear = int(input("\nThe World Series was not played this year."+
                               " Please enter another year: \n"))
   
    team = years.get(userYear)
    times = count.get(team)

    print ("\nIn ",userYear," the ",team," won. They won ",times,
           " time(s) between 1903 and 2009.")       
main()
                
            
