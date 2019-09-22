# Gabriela Canjura
# CSC 121 CarClass
# 04/23/2018
# adds employee information and displays it 

import Employee2 as Emp

def main():

    employees = makeList()

    spacing = '{:<15}{:<15}{:<10}{:<15}'
    intro = spacing.format("\nEmployee Name", "ID Number",
                           "Shift", "Pay Rate")

    print(intro)
    print("-"*55)    

    displayList(spacing, employees)
    
def makeList():

    employee_list = []

    user = int(input("How many employees would you like to enter? "))

    x = 0

    name = ''
    IDnumber = 0
    shiftNumber = 0
    payRate = 0.0

    for x in range(0,user):

        name = input("\nEnter employee name: ")
        IDnumber = int(input("Enter employee number: "))
        shiftNumber = int(input("Enter 1 for day shift or 2 for night shift: "))
        payRate = float(input("Enter pay rate: "))

        employee = Emp.ProductionWorker(name, IDnumber, shiftNumber, payRate)

        employee_list.append(employee)

    return employee_list

def displayList(spacing, employee_list):

    for item in employee_list:

        text = spacing.format(item.get_name(),item.get_IDnumber(),
                              item.get_shift(),
                              format(item.get_payRate(),',.2f')) 
        print(text)

main()


    
