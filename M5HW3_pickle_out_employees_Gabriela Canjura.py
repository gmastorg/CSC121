# Gabriela Canjura
# CSC 121_M5HW3_EmployeeClass
# 04/18/2018
# uses pickle to write data to a file to access later

import pickle 
import Employee

FILENAME = 'employees.dat'

def main():

    output_file = open(FILENAME, 'wb')

    user = int(input("How many employees would you like to enter? "))

    x = 0

    for x in range(0,user):

        name = input("\nEnter employee name: ")
        IDnumber= input("Enter ID number: ")
        department = input("Enter department: ")
        jobTitle = input("Enter job title: ")
        
        employee = Employee.Employee(name, IDnumber, department, jobTitle)

        pickle.dump(employee, output_file)

main()
