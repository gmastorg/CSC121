# Gabriela Canjura
# CSC 121 CarClass
# 04/23/2018
# adds employee information and displays it 

import Employee2 as Emp

def main():

    employees = makeList()

    spacing = '{:<15}{:<10}{:<15}{:<15}'
    intro = spacing.format("\nEmployee Name", "ID Number",
                           "Annual Salary", "Annual Bonus")

    print(intro)
    print("-"*55)    

    displayList(spacing, employees)
    
def makeList():

    employee_list = []

    user = int(input("How many employees would you like to enter? "))

    x = 0

    name = ''
    IDnumber = 0
    annualSalary = 0
    annualBonus = 0

    for x in range(0,user):

        name = input("\nEnter employee name: ")
        IDnumber = int(input("Enter employee number: "))
        annualSalary = int(input("Enter annual salary: "))
        annualBonus = int(input("Enter annual bonus: "))
    
        employee = Emp.ShiftSupervisor(name, IDnumber, annualSalary, annualBonus)

        employee_list.append(employee)

    return employee_list

def displayList(spacing, employee_list):

    for item in employee_list:

        text = spacing.format(item.get_name(),item.get_IDnumber(),
                              item.get_annualSalary(),item.get_annualBonus()) 
        print(text)

main()
