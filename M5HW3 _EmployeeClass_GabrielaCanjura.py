# Gabriela Canjura
# CSC 121_M5HW3_EmployeeClass
# 04/18/2018
# creates a list that holds objects with employee info then displays held info

import Employee

def main():

    employees = makeList()

    spacing = '{:<15}{:<10}{:<15}{:<15}'
    intro = spacing.format("Employee Name", "ID Number",
                           "Department", "Job Title")

    print(intro)
    print("-"*55)

    displayList(spacing, employees)

def makeList():

    employee_list = []

    user = int(input("How many employees would you like to enter? "))

    x = 0

    for x in range(0,user):

        name = input("\nEnter employee name: ")
        IDnumber= input("Enter ID number: ")
        department = input("Enter department: ")
        jobTitle = input("Enter job title: ")
        
        employee = Employee.Employee(name, IDnumber, department, jobTitle)

        employee_list.append(employee)

    return employee_list

def displayList(spacing, employee_list): 

    for item in employee_list:

        text = spacing.format(item.get_name(),item.get_IDnumber(),
                              item.get_department(),item.get_jobTitle()) 
        print(text)

main()
