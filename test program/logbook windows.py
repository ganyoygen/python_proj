import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = inputwo.get()
	return userInput

def getInputBoxValue():
	userInput = inputifca.get()
	return userInput

def getInputBoxValue():
	userInput = inputtgl.get()
	return userInput

def getInputBoxValue():
	userInput = inputunit.get()
	return userInput

def getInputBoxValue():
	userInput = inputworkreq.get()
	return userInput

def getInputBoxValue():
	userInput = inputstaff.get()
	return userInput

def getInputBoxValue():
	userInput = inputworkact.get()
	return userInput

def getInputBoxValue():
	userInput = inputdatedone.get()
	return userInput

def getInputBoxValue():
	userInput = inputtimedone.get()
	return userInput

#this is the function called when the button is clicked
def writeBtnClk():
	print('clicked')

def updatebtnclk():
	print('clicked')

def receivedbtnclk():
	print('clicked')


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = cbVariable.get()
	return checkedOrNot
# this is a function which returns the selected spin box value
def getSelectedSpinBoxValue():
	return spinBoxTwo.get()


root = Tk()
#this is the declaration of the variable associated with the checkbox
cbVariable = tk.IntVar()


# This is the section of code which creates the main window
root.geometry('860x560')
root.configure(background='#F0F8FF')
root.title('Hello, I\'m the main window')


# This is the section of code which creates the a label
Label(root, text='No.WO', bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=46, y=17)

Label(root, text='No.IFCA', bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=46, y=47)

Label(root, text='Tanggal', bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=46, y=77)

Label(root, text='Unit', bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=46, y=107)

Label(root, text='Work Request', bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=46, y=137)

Label(root, text='Staff', bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=46, y=207)

Label(root, text='Work Action', bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=446, y=17)

Label(root, text='Date Done', bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=446, y=77)

Label(root, text='Time Done', bg='#F0F8FF', font=('arial', 12, 'bold')).place(x=446, y=107)


# This is the section of code which creates a text input box
inputwo=Entry(root)
inputwo.place(x=176, y=17)

inputifca=Entry(root)
inputifca.place(x=176, y=47)

inputtgl=Entry(root)
inputtgl.place(x=176, y=77)

inputunit=Entry(root)
inputunit.place(x=176, y=107)

inputworkreq=Entry(root)
inputworkreq.place(x=176, y=137)

inputstaff=Entry(root)
inputstaff.place(x=176, y=207)

inputworkact=Entry(root)
inputworkact.place(x=556, y=17)

inputdatedone=Entry(root)
inputdatedone.place(x=556, y=77)

inputtimedone=Entry(root)
inputtimedone.place(x=556, y=107)


# This is the section of code which creates a button
Button(root, text='Write', bg='#C1CDCD', font=('arial', 12, 'bold'), command=writeBtnClk).place(x=176, y=237)

Button(root, text='Update', bg='#C1CDCD', font=('arial', 12, 'bold'), command=updatebtnclk).place(x=456, y=237)

Button(root, text='Received', bg='#C1CDCD', font=('arial', 12, 'bold'), command=receivedbtnclk).place(x=716, y=237)


# This is the section of code which creates a checkbox
CheckBoxOne=Checkbutton(root, text='Check me, I\'m a box!', variable=cbVariable, bg='#F0F8FF', font=('arial', 12, 'bold'))
CheckBoxOne.place(x=16, y=297)


# This is the section of code which creates a spin box
spinBoxTwo= Spinbox(root, from_=1, to=50, font=('arial', 12, 'bold'), bg = '#EEDFCC', width=10)
spinBoxTwo.place(x=136, y=367)


root.mainloop()
