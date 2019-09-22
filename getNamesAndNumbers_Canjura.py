def main():

    import random 

    file = open('namesAndNumbers.txt','w')

    for i in range (1,20):

        name = input("Enter a Name: (last,first) \n")

        studentID = random.randint(0000000,9999999)

        space = int(20-len(name))
        info = name+" "*space

        file.write(info)
        file.write(str(studentID)+"\n")

    file.close()

main()
    
