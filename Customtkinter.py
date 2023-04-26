from tkinter import *
from tkinter import ttk

import Customtkinter

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry
win.geometry("700x250")

# Define a function to return the Input data
def get_data():
    textvar = Customtkinter.entry.get()
    print(textvar)
   #label.config(text= entry.get(), font= ('Helvetica 13'))


#Create an Entry Widget
entry = Entry(win, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)

#Inititalize a Label widget
label= Label(win, text="", font=('Helvetica 13'))
label.pack()

#Create a Button to get the input data
ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

win.mainloop()