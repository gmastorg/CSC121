#Gabriela Canjura
#CSC 121 - M4A1_FileEncryptionDecryption
#04/02/2018
#File Encryption and Decryption

def encrypt(filename):
        
    outfile = open('encrypted.txt','w')

    code = generateRandomCharacter()

    i = 0

    with open(filename,'r') as infile:
        for  line in infile:
            for letter in  line:
                if letter in code:
                    encrypted = code[letter]
                    outfile.write(encrypted)
                    
    outfile.close()
    

def decrypt(filename):

    outfile = open('decrypted.txt', 'w')

    with open('decodeKey.txt', 'r') as inf:
        code = eval(inf.read())

    with open(filename, 'r') as infile:
        for line in infile:
            for letter in line:
                for key,value in code.items():
                    if value == letter:
                        outfile.write(key)
    outfile.close()
                        
def cypher():

    with open('decodeKey.txt', 'r') as inf:
        code = eval(inf.read())

        #print("\n"+str(code))

    return code

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

