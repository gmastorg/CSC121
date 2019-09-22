# This program will calculate a student's grade
# This program will demo the use of functions and how to pass parameters between functions
# Anthony Cameron
# 10-3-2016

# main function that will do all of the functions calls
def main():
# function call and return # of grades to enter
    num = get_input()
# function call and return average
    average = get_average(num)
# function call and return letter grade
    letter_grade = get_letter_grade(average)
# function call to print letter grade
    display_grade(average,letter_grade)


#get the input from the user

def get_input():
    num = int(input("How many grades do you want to input? "))
    return num

# function call and return average

def get_average(num):
    total = 0
    for x in range (num):
        grade = float(input("Enter a grade "))
        total = grade + total
        
    average = total / num
    return average
#get the letter grade from the average    
def get_letter_grade(ave):

    if ave >= 90:
        grade = "A"
    elif ave >= 80:
        grade = "B"
    elif ave >= 70:
        grade = "C"
    elif ave >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

# diplay average and letter grade
def display_grade(ave,grade):
    
    print("Your average is ", ave, " which is a letter grade of ", grade)
    

# main function call; basically where program starts

main()



    
