# Gabriela Canjura
# CSC 121_M5HW1_PetClass
# 04/16/2018
# receives object displays object does calculations with object

import Car

def main():

    car_year_model = 0
    car_make = ""
    car_speed = 0

    car_year_model = input("Enter year model: ")
    car_make = input("Enter the make of car: ")
    car_speed = int(input("Enter the speed: "))

    car = Car.Car(car_year_model, car_make, car_speed)

    x = 0
    current_speed = 0

    print("\nYear Model: ", car.get_year_model())
    print("Make: ", car.get_make())
    
    for x in range(0,4):
        current_speed += car.accelerate(car_speed)
        x+=1
        print("Current Speed: ", current_speed)
        
    x = 0
    
    for x in range(0,4):        
        current_speed -= car.brake(car_speed)
        x+=1
        print("Current Speed: ", current_speed)

main()
