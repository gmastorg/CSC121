# Allows user to type in the name of a baseball team and
# it tells you how many times they won taking info from text file
# 02/14/2018
# CSC-121 M2HW2 - World Series
# Gabriela Canjura

def main():

    infile = open('WorldSeriesWinners.txt', 'r')

    teams = infile.readlines()

    infile.close()

    index = 0
    
    while index < len(teams):
        teams[index] = teams[index].rstrip('\n') #creates a list from file
        index+=1

        while name in teams:
            num = index

    get_count(teams)

   
    
def get_count(teams):

     name = input('Enter the name of the team you would like to search: ')

     count = 0
    
     if name in teams:
        count = teams.count(name) #counts the number of times
        print("The", name, "won", count, "times.")
     else:
        print("The", name, "have not won the world series.")
    
main()
