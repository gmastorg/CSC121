# writes name to a file
# 02/05/2018
# CSC121-0001 AW1T1 - Name Input
# Gabriela Canjura

def main():
    name = input("Enter your name: ")

    nameFile = open('E:/2018 SP CSC121/my_name.txt', 'w')

    nameFile.write(name)

    nameFile.close()

main()
