#import the tkinter module
import tkinter as tk

#import the ttk module from the tkinter module
from tkinter import ttk

#import file dialog
from tkinter import filedialog
from tkinter import *

import FileEncryptionDecryption as file

import webbrowser

##How to create an empty root window
root = tk.Tk()
root.title("File Encryption Decryption")
root.geometry("300x125")

#how to create a frame and add it to the root window
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

#savedName = '' #saved name variable
#openName = '' #open name variable


def encrypt():
        
    outfile = open(savedName,'w')

    code = generateRandomCharacter()

    i = 0

    with open(openName,'r') as infile:
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
   
def click_saveFileBtn():
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Save As",filetypes = (("text files","*.txt"),
                                                                                               ("all files","*.*")))
    #global savedName   
    savedName=root.filename

    root3 = tk.Tk()
    root3.title("Hey")
    root3.geometry("400x100")
    frame3 = ttk.Frame(root3, padding="10 10 10 10")
    frame3.pack(fill=tk.BOTH, expand=True)
    
    selectBtn = ttk.Button(frame3, text="Select File to Encrypt", command=click_selectFileBtn)
    selectBtn.pack()
   
def click_selectFileBtn():
    savedName.get()
    root.openname =  filedialog.askopenfilename(initialdir = "/",title = "Select file to encrypt",
                                              filetypes = (("text files","*.txt"),("all files","*.*")))
    #global openName
    openName = root.openname

    encrypt()
    
    root4 = tk.Tk()
    root4.title("Open File")
    root4.geometry("400x100")
    frame4 = ttk.Frame(root4, padding="10 10 10 10")
    frame4.pack(fill=tk.BOTH, expand=True)
    ttk.Label(frame4,text= "Your file has been encrypted. Click open to view.", wraplength = 300).pack()
    openFileBtn = ttk.Button(frame3, text="Open File", command=click_openFileBtn).pack()
    

def click_openFileBtn():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    filename=root.filename
    webbrowser.open(filename)
    

def click_encryptBtn():
    root2 = tk.Tk()
    root2.title("Encrypt")
    root2.geometry("400x100")
    frame2 = ttk.Frame(root2, padding="10 10 10 10")
    frame2.pack(fill=tk.BOTH, expand=True)
    saveFileBtn = ttk.Button(frame2, text="Save As", command=click_saveFileBtn).pack()
   
encryptBtn = ttk.Button(frame, text="Encrypt", command=click_encryptBtn).pack()
decryptBtn = ttk.Button(frame, text="Decrypt", command=click_decryptBtn).pack()
cypherBtn = ttk.Button(frame, text="Cypher", command=click_cypherBtn).pack()
exitBtn = ttk.Button(frame, text="Exit", command=click_exitBtn).pack()    



