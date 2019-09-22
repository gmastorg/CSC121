# Gabriela Canjura
# CSC 121_M4A2_FileAnalysis
# 04/06/2018
# Compares words in two files using sets

def main():

    set1 = set ()

    set2 = set()

    set3 = set()

    firstList = []

    secondList = []
    
    filesList = []
    
    with open ('first_file.txt','r') as firstfile:
        for line in firstfile:
            line = line.lower()
            line = line.replace(".", "").replace(",","")
            word = line.split(' ')
            firstList = word
            set1 = set(firstList)
            
    with open('second_file.txt', 'r') as secondfile:
        for line in secondfile:
            line = line.lower()
            line = line.replace(".", "").replace(",","")
            word = line.split(' ')
            secondList = word
            set2 = set(secondList)
            
    set3 = set1|set2 #combines both sets

    print ("Unique words in both files: ",set3)

    set3 = set1.intersection(set2) #shows items that are in both files

    print ("\nWords that are in both files: ",set3)

    set3 = set1.difference(set2) #shows items that are not found in both sets

    print("\nWords in first file but not in second: ",set3)

    set3 = set2.difference(set1)

    print("\nWords in second file but not in first: ",set3)

    set3 = set1.symmetric_difference(set2) #shows items unique to both sets

    print("\nWords in either first or second file but not in both: ",set3)

    
main()

    
        
