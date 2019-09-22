# 02/26/2018
# CSC-121 classwork
# Gabriela Canjura

def main():

    reportFile = open('tdsc01.txt' , 'r') # opens and reads file

    file = open('productSalesReport.txt','w') # creates a filt to write into

    file.write("Product Sales Report\n\n"+"Item"+" "*7+"Customer"+" "*12+"Item\t\tPrice Per\n"
    +"Number"+" "*5+"Name"+" "*16+"Description\tUnit\n"+"-"*57+"\n\n") # writes intro to file

    #below prints intro to shell
    print ("Product Sales Report\n\n")
    print("Item"+" "*7+"Customer"+" "*12+"Item\t\tPrice Per")
    print("Number"+" "*5+"Name"+" "*16+"Description\tUnit")
    print("-"*65,"\n")

    count = float(0)
    priceTotal = float(0)
    priceAve = float(0)
    
    for line in reportFile:
        
        itemNum = line[7:10]+"-"+line[10:13]+" "*4 #obtains data from file and formats it
        
        name = line[13:33]

        itemDesc = line[33:48]+"\t"

        price = "$"+line[len(line)-4:len(line)-3]+"."+line[len(line)-3:len(line)]

        priceNum = float(line[len(line)-4:len(line)])/100#converts string to float
        
        priceTotal += priceNum # gets total

        count +=1 # keeps count of number of 

        priceAve = (priceTotal)/count
        
        row = itemNum+name+itemDesc+price.rstrip()+"\n" # creates a variable with out put for file
            
        print (itemNum+name+itemDesc+price.rstrip()) # prints output to shell

        file.write(row) # prints output to file

    print("-"*57+"\n"+"Average Price of an Item: "+"$",format(priceAve,',.2f')) 
    print("Total Cost of Items: "+"$",format(priceTotal,',.2f'))

    ave = "-"*57+"\n"+"Average Price of an Item: "+"$"+format(priceAve,',.2f')+"\n"
    total = "Total Cost of Items: "+"$"+format(priceTotal,',.2f')
    
    file.write(ave+total)
    
    reportFile.close() 
    file.close()
    
main()

    
   
