# Gabriela Canjura
# CSC 121_M5HW3_EmployeeClass
# 04/18/2018
# displays data in objects

import Employee

def main():

    employees = []

    employee1 = Employee.Employee("Susan Meyers", 47899, "Accounting",
                                  "Vice President")
    employee2 = Employee.Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee.Employee("Joy Rogers", 81774, "Manufacturing",
                                  "Engineer")

    employees.append(employee1)
    employees.append(employee2)
    employees.append(employee3)
    
    spacing = '{:<15}{:<10}{:<15}{:<15}'
    intro = spacing.format("Employee Name", "ID Number",
                           "Department", "Job Title")

    print(intro)
    print("-"*55)
    
    for item in employees:
        text = spacing.format(item.get_name(),item.get_IDnumber(),
                              item.get_department(),item.get_jobTitle())            
        print(text)

main()
