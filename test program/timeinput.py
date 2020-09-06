from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        sv = StringVar()
        endHourEntry = Entry(self, textvariable=sv)
        sv.trace("w", lambda name, index, mode, sv=sv: 
                             entryUpdateEndHour(endHourEntry))
        endHourEntry.pack()

def entryUpdateEndHour(entry):
    text = entry.get()
    if len(text) in (2,):
        entry.insert(END,':')
        entry.icursor(len(text)+1)
    # elif len(text) not in (3,6):
    if not text[-1].isdigit():
        entry.delete(0,END)
        entry.insert(0,text[:-1])
    if len(text) > 5:
        entry.delete(0,END)
        entry.insert(0,text[:5])


root = Tk() 
app = Application(master=root) 
app.mainloop()