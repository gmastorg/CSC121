def getDictionary():
    
    import random
        
    infile = open('characters.txt', 'r')

    characters = []
    ch = []

    file = open('decodeKey.txt','w') 

    symbols = {} 

    index = 0
    
    for line in infile:
        characters.append(line.rstrip("\n"))
    ch = random.sample(characters, len(characters))
    #print(characters)
    #print(ch)
    symbols = dict(zip(characters,ch))
    
    #print(symbols)

    file.write(str(symbols))

    file.close()


 
