# opens file reads name and displays it
# 02/05/2018
# CSC121-0001 AW1T2 - Name Output
# Gabriela Canjura

def main():

    nameFile = open('E:/2018 SP CSC121/my_name.txt', 'r')

    line = nameFile.readline()

    nameFile.close()

    print(line)

main()
