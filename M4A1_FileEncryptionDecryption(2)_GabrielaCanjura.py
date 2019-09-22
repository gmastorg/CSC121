#Gabriela Canjura
#CSC 121 - M4A1_FileEncryptionDecryption
#04/02/2018
#File Encryption and Decryption

def main():

    keepGoing = "Y"

    while keepGoing == "Y":

        menu()

        keepGoing = input("\nWould you like to do something else? (Y/N)")
        keepGoing = keepGoing.upper()
    
def menu():

    print("\n1. Encrypt File")
    print("2. Decrypt File")
    print("3. View Cyphir")
  
     
    decision = int(input("\nWould you like to do? "))

    if decision == 1:
        encrypt()
    elif decision == 2:
        decrypt()
    elif decision == 3:
        cypher()
    else:
        print ("Invalid option, try again.\n")
        temp=menu()
            
def encrypt():

    outfile = open('encrypted.txt','w')

    code = generateRandomCharacter()

    i = 0

    with open('original.txt','r') as infile:
        for  line in infile:
            for letter in  line:
                if letter in code:
                    encrypted = code[letter]
                    outfile.write(encrypted)
               
    outfile.close()

def decrypt():

    outfile = open('decrypted.txt', 'w')

    with open('decodeKey.txt', 'r') as inf:
        code = eval(inf.read())

    

    with open('encrypted.txt', 'r') as infile:
        for line in infile:
            for letter in line:
                for key,value in code.items():
                    if value == letter:
                        outfile.write(key)
    outfile.close()
                        
def cypher():

    with open('decodeKey.txt', 'r') as inf:
        code = eval(inf.read())

        print("\n"+str(code))

def generateRandomCharacter():

    import string
    import random

    file = open('decodeKey.txt','w')
    
    code = {}

    key = []

    value = []

    key = [i for i in string.printable]

    key.remove('\r')
    
    value = random.sample(key, len(key))

    code = dict(zip(key,value))

    file.write(str(code))

    file.close()

    return code

main()
