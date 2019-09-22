# Gabriela Canjura
# CSC 121 CarClass
# 04/18/2018
# Creates a class

class Employee:

    def __init__(self, name, IDnumber, department, jobTitle):

        self.__name = name
        self.__IDnumber = IDnumber
        self.__department = department
        self.__jobTitle = jobTitle
            
    def set_name(self, name):
        self.__name = name

    def set_IDnumber(self, IDnumber):
        self.__IDnumber = IDnumber

    def set_department(self, department):
        self.__department = department

    def set_jobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

    def get_name(self):
        return self.__name

    def get_IDnumber(self):
        return self.__IDnumber

    def get_department(self):
        return self.__department

    def get_jobTitle(self):
        return self.__jobTitle


   
