# gathers numbers from a file and averages them
# creates exceptions for characters that may have been entered incorrectly
# 02/05/2018
# CSC-121 M1HW2 - Exception_Handling
# Gabriela Canjura

def main():
    
    total = float(0)
    numOfNums = float(0)
    ave = float (0)

    try:
        numbersFile = open('numbers2.txt', 'r')

        line = numbersFile.readline()

        while line != '':
            num = float(line)

            total += num

            numOfNums += 1

            line = numbersFile.readline() 

        ave = total / numOfNums

        numbersFile.close()

        print ("The average is: ")
        print(format(ave, '.2f'))

    except IOError:
        print("An error occured trying to read the file.")
        
    except ValueError:
        print("Non-numeric data found in file on line",numOfNums+1,".") 

main()
    
    
