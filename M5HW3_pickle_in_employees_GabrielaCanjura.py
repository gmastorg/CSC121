# Gabriela Canjura
# CSC 121_M5HW3_EmployeeClass
# 04/18/2018
# accesses data from file and assigns it to an object displays data in objects

import pickle 
import Employee

FILENAME = 'employees.dat'

def main():

    end_of_file = False

    input_file = open(FILENAME, 'rb')

    spacing = '{:<15}{:<10}{:<15}{:<15}'
    intro = spacing.format("Employee Name", "ID Number",
                           "Department", "Job Title")
    
    print(intro)
    print("-"*55)
    
    while not end_of_file:
        try:
            employee = pickle.load(input_file)
            displayData(employee)

        except EOFError:

            end_of_file = True

    input_file.close()

def displayData(employee):

    spacing = '{:<15}{:<10}{:<15}{:<15}'

    text = spacing.format(employee.get_name(),employee.get_IDnumber(),
                            employee.get_department(),employee.get_jobTitle()) 
    print(text)

main()
