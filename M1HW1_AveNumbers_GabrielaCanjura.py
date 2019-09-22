# gathers numbers from a file and averages them
# 02/05/2018
# CSC-121 M1HW1 - Average Numbers
# Gabriela Canjura

def main():

    total = float(0)
    numOfNums = float(0)
    ave = float (0)
    
    numbersFile = open('numbers.txt', 'r')

    line = numbersFile.readline()

    while line != '':

        num = float(line)

        total += num

        numOfNums += 1

        line = numbersFile.readline() # moves to next line

    ave = total / numOfNums

    print ("The average is: ")
    print(format(ave, '.2f'))

    numbersFile.close()

main()
    
    
