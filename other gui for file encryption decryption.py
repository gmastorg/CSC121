    
def click_decryptBtn():
    filename = selectFile()
    root4 = tk.Tk()
    root4.title("Decrypt")
    root4.geometry("400x150")
    frame4 = ttk.Frame(root4, padding="10 10 10 10")
    frame4.pack(fill=tk.BOTH, expand=True)
    file.decrypt(filename)
    ttk.Label(frame4,text="\nYour file has been decrypted and saved as decrypted.txt.\n"+
              "To view your decrypted file click open file: \n").pack()
    openFileBtn = ttk.Button(frame3, text="Open File", command=click_openFileBtn).pack()
    
def click_cypherBtn():
    root4 = tk.Tk()
    root4.title("Cypher")
    root4.geometry("500x225")
    frame4 = ttk.Frame(root4, padding="10 10 10 10")
    frame4.pack(fill=tk.BOTH, expand=True)
    cypher = file.cypher()
    ttk.Label(frame4,text= str(cypher), wraplength = 300).pack()
       
def click_exitBtn():
    root.destroy()  

def click_openFileBtn():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    filename=root.filename
    webbrowser.open(filename)
           
encryptBtn = ttk.Button(frame, text="Encrypt", command=click_encryptBtn).pack()
decryptBtn = ttk.Button(frame, text="Decrypt", command=click_decryptBtn).pack()
cypherBtn = ttk.Button(frame, text="Cypher", command=click_cypherBtn).pack()
exitBtn = ttk.Button(frame, text="Exit", command=click_exitBtn).pack()

    file.encrypt(filename)
    ttk.Label(frame3,text="\nYour file has been encrypted and saved as encrypted.txt.\n"+
              "To view your encrypted file click open file: \n").pack()
    openFileBtn = ttk.Button(frame3, text="Open File", command=click_openFileBtn)
    openFileBtn.pack()

def saveFile():
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Save As",filetypes = (("text files","*.txt"),
                                                                                                  ("all files","*.*")))
    saved=root.filename
    return save

 file.encrypt(filename)
    ttk.Label(frame3,text="\nYour file has been encrypted and saved as encrypted.txt.\n"+
              "To view your encrypted file click open file: \n").pack()
    openFileBtn = ttk.Button(frame3, text="Open File", command=click_openFileBtn)
    openFileBtn.pack()

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

#
def click_selectFileBtn(savedName):
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file to encrypt or decrypt",
                                                filetypes = (("text files","*.txt"),("all files","*.*")))
    openName = root.filename

    root3 = tk.Tk()
    root3.title("Encrypt")
    root3.geometry("400x100")
    frame3 = ttk.Frame(root3, padding="10 10 10 10")
    frame3.pack(fill=tk.BOTH, expand=True)
    saveFileBtn = ttk.Button(frame3, text="Save As", command=click_saveFileBtn(openName)).pack()
    
    
def click_saveFileBtn(openName):
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Save As",filetypes = (("text files","*.txt"),
                                                                                                  ("all files","*.*")))
    savedName=root.filename

    root3 = tk.Tk()
    root3.title("Encrypt")
    root3.geometry("400x100")
    frame3 = ttk.Frame(root3, padding="10 10 10 10")
    frame3.pack(fill=tk.BOTH, expand=True)
    saveFileBtn = ttk.Button(frame3, text="Save As", command=click_saveFileBtn(savedName)).pack()
    
    return openName, savedName   

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
