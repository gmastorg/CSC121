#03/21/2018
#Gabriela Canjura
#File Encryption and Decryption

#import encoding_Dictionary

def main():

    code = {'u': '/', 'J': 'F', "'": '=', '-': '-', '{': '!', 'O': ',', '`': 'D', 'C': 'X', 'K': '0', 'L': '|', '7': 'f',
            'E': 'q', '!': 'G', '%': 'g', '9': "'", ')': 'I', '3': ']', '|': '9', 'z': '@', 't': '}','Q': 'A', ':': '^',
            '&': '$', 'n': '`', 'V': 'S', '/': 'Q', 'W': '&', '?': '>', 'Z': 'B', 'b': 'T', 'U': 'L', '>': 'J', '5': 'Z',
            'x': '"', '_': 'H', 'f': '%', '0': 'm', '6': 'n', '(': '5', 'I': '(', ']': 'h', ',': '<', '~': '7', 'l': 'k',
            '<': 'b', 'H': 'V', 'a': ')', 'D': 'y', '"': '?', 'R': 'N', 'g': 'C', 'S': 'o', '=': 'l', '1': 'O', '$': '.',
            'v': 'R', '\\': '~', 'i': '4', 'k': '6', 'T': 's', 'y': '{', 'h': 'c', 'o': '\\', '2': '2', 'X': '3', ' ': '_',
            '8': '1', '*': 'x', 'm': 'K', '[': 'U', 'F': '#', '^': 'd', 's': ' ', '4': 'p', 'p': 'W', 'M': 'r', ';': ':',
            'q': '*', 'P': 'M', 'j': ';', 'r': 'u', 'B': '8', '.': '[', '+': 'i', 'd': 't', 'N': '+', 'e': 'E', 'c': 'j',
            'G': 'Y', '}': 'e', '@': 'a', 'w': 'z', '#': 'v', 'A': 'P', 'Y': 'w'}
    
    infile = open('text.txt','r')

    outfile = open('encrypted.txt','w')

    i = 0

    for line in infile:
        while i < len(line):
            ch = line[i]
            i += 1
            #print(ch)
            if ch in code:
                value = code.get(ch)
            #print(value)
                outfile.write(value)
    
             
    infile.close()
    outfile.close()


main()
