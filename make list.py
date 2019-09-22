def main():
    import random
        
    infile = open('characters.txt', 'r')

    characters = infile.readlines()

    ch = []
    
    infile.close()

    symbols = {} 

    index = 0
    
    while index < len(characters):
        characters[index] = characters[index].rstrip("\n") #creates a list from file
        ch = random.sample(characters, len(characters))
        index+=1
    symbols = dict(zip(characters, ch))
    print(symbols)
main()

