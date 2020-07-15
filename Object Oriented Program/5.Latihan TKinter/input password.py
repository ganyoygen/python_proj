# Accept password from tkinter entry

from tkinter import *


win = Tk()
win.geometry("300x300") #ukuran windows
text = StringVar() # variable to keep track of input in entry widget

def foo(): # function called on btn-click
    print(text.get()) # print value of text var

# pass a show **** argument
entry = Entry(win, show="*",textvariable = text)
button = Button(win, text = "OK", command = foo)

entry.pack()
button.pack()

win.mainloop()