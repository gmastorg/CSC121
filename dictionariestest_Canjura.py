def main():

    addressbook = {}
    infoFile = open('namesAndNumbers.txt','r')

    file = open('usernamesAndEmails.txt','w')

    #spacing = '{:<20}{:<10}{:<15}{:<20}'
    #intro = spacing.format("Student Name","Datatel#","Username","Email")
    #dashes = "-"*80

    #file.write(intro+"\n"+dashes+"\n")

    #print(intro+"\n"+dashes)

    for line in sorted(infoFile):

        name = line[0:20]
                
        name_list = name.split(",")
        lastName =  name_list[0].strip()
        firstName = name_list[1].strip()
        
        datatel = line[20:27]

        user = lastName[0:6]+firstName[0]+line[23:27]
                
        email = user+"@student.faytechcc.edu"

        name2 = lastName+", "+firstName

        #output = spacing.format(name2,datatel,user.lower(),email.lower())
        
        #print(output)

        #file.write (output+"\n")

        addressbook[name]= email, datatel
        print (name, addressbook[name]) 
    
 
    infoFile.close()
    
    file.close()
    
main()
