#03/19/2018
#Gabriela Canjura
#csv files

import csv

# READS FILES
with open('names.csv','r')as csv_file:

    #csv_reader = csv.reader(csv_file) # reads the file 
    csv_reader = csv.DictReader(csv_file) # reads file as dictionary

    #print(csv_reader) # tells you that it is reading the file

    #next(csv_reader)#erases the first line when displaying

    #CREATES NEW FILE TO ADD CONTENTS AND USES - TO SEPERATE

    with open('new_names.csv','w')as new_file: # writes new file

         csv_writer = csv.writer(new_file,delimiter="-")

         for line in csv_reader:
             print(line['Email']) ## prints lines as is
             csv_writer.writerow(line)


            #print(line[0]) ## prints line at index which is email address(3rd col)
            # remember index starts at 0
            


      
    
