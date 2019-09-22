# 02/26/2018
# CSC-121 classwork
# Gabriela Canjura

def main():

    reportFile = open('tdsc01.txt' , 'r') # opens and reads file

    file = open('productSalesReport.txt','w') # creates a file to write into

    spacing = '{:<15}{:<20}{:<20}{:<15}'

    title = "Product Sales Report\n"
    intro1 = spacing.format("Item","Customer","Item","Price Per")
    intro2 = spacing.format("Number","Name","Description","Unit")
    dashes = "-"*70
    
    #below prints intro to shell
    print (title.center(70))
    print (intro1)
    print (intro2)
    print (dashes)

    file.write(title.center(70)+"\n"+intro1+"\n"+intro2+"\n"+dashes+"\n") # writes intro to file

    getReport(reportFile, file, spacing, dashes)
   
    reportFile.close() 
    file.close()
    
def getReport(reportFile, file, spacing, dashes):

        count = float(0)
        priceTotal = float(0)
        priceAve = float(0)
    
        for line in reportFile:
            
            itemNum = line[7:10]+"-"+line[10:13] #obtains data from file and formats it
        
            name = line[13:33]

            itemDesc = line[33:48]

            price = "$"+line[len(line)-4:len(line)-3]+"."+line[len(line)-3:len(line)]

            priceNum = float(line[len(line)-4:len(line)])/100 #converts string to float
        
            priceTotal += priceNum # gets total

            count +=1 # keeps count of number of 

            priceAve = (priceTotal)/count
        
            row = spacing.format(itemNum,name,itemDesc,price.rstrip()) # creates a variable with out put for file
            
            print (row) # prints output to shell

            file.write(row+"\n") # prints output to file

        displayAveAndTotal(reportFile, file, priceAve, priceTotal, dashes)

def displayAveAndTotal(reportFile, file, priceAve, priceTotal, dashes):

        total = "Total Cost of Items: "+"$"+format(priceTotal,',.2f')
        ave = dashes+"\n"+"Average Price of an Item: "+"$"+format(priceAve,',.2f')

        print(ave) 
        print(total)
        
        file.write(ave+"\n"+total)
    
main()    
   
