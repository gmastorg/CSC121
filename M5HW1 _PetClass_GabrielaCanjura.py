# Gabriela Canjura
# CSC 121_M5HW1_PetClass
# 04/16/2018
# receives input creates object and displays object 

import Pet

def main():

    petName = ""
    petType = ""
    petAge = 0

    petName = input("Enter your pet's name: ")
    petType = input("Enter your pet type: ")
    petAge = int(input("Enter your pets age: "))

    pet =Pet.Pet(petName, petType, petAge)

    print("\nYour pet's info: ")
    print("Name: ", pet.get_name())
    print("Type: ",pet.get_animal_type())
    print("Age: ",pet.get_age())

main()
