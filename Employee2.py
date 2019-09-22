# Gabriela Canjura
# CSC 121 CarClass
# 04/23/2018
# Creates a class

class Employee:

    def __init__(self, name, IDnumber):

        self.__name = name
        self.__IDnumber = IDnumber
            
    def set_name(self, name):
        self.__name = name

    def set_IDnumber(self, IDnumber):
        self.__IDnumber = IDnumber

    def get_name(self):
        return self.__name

    def get_IDnumber(self):
        return self.__IDnumber

class ProductionWorker(Employee):

    def __init__(self, name, IDnumber, shiftNumber, payRate):

        Employee.__init__(self, name, IDnumber)

        self.__shiftNumber = shiftNumber
        self.__payRate = payRate

    def set_shiftNumber (self, shiftNumber):
        self.__shiftNumber = shiftNumber

    def set_payRate(self, payRate):
        self.__payRate = payRate

    def get_shiftNumber(self):
        return self.__shiftNumber

    def get_payRate(self):
        return self.__payRate

    def get_shift(self):

        if self.__shiftNumber == 1:
            self.__shiftNumber = "Day"
        else:
            self.__shiftNumber = "Night"

        return self.__shiftNumber

class ShiftSupervisor(Employee):

    def __init__(self, name, IDnumber, annualSalary, annualBonus):

        Employee.__init__(self, name, IDnumber)

        self.__annualSalary = annualSalary
        self.__annualBonus = annualBonus

    def set_annualSalary (self, annualSalary):
        self.__annualSalary = annualSalary

    def set_annualBonus(self, annualBonus):
        self.__annualBonus = annualBonus

    def get_annualSalary(self):
        return self.__annualSalary

    def get_annualBonus(self):
        return self.__annualBonus
