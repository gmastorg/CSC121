# gathers numbers puts them in a list
# determines correct number for each category
# 02/12/2018
# CSC-121 M2HW1 - NumberAnalysis
# Gabriela Canjura

def main():

    total = float(0) 
    numOfNumbers = int(20) # decides loop count and used for average
    
    total,numbers = get_values(numOfNumbers)
    get_lowest(numbers)
    get_highest(numbers)
    get_total(total)
    get_average(total, numOfNumbers)

def get_values(numOfNumbers):

    values = []  # holds list of numbers
    total = float(0)
    
    for x in range (numOfNumbers): #creates loop 

        num = float(input("Enter a number: "))

        total += num; # holds the total as numbers are entered in loop
        
        values.append(num) # creates list

    return total, values

def get_lowest(numbers):

    lowest = min(numbers) # gets lowest number

    print("The lowest number in the list is: " , lowest)

def get_highest(numbers):

    highest = max(numbers) # gets highest number

    print("The highest number in the list is: " , highest)

def get_total(total):

    print("The total of the numbers is: ", total)

def get_average(total, numOfNumbers):

    ave = total/numOfNumbers

    print("The average of the numbers is: ", ave)

main()

