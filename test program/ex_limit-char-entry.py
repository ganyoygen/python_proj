from tkinter import *

def callback(sv):
    c = sv.get()[0:9] # max 9 char
    print ("c=" , c)
    sv.set(c)
root = Tk()
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()

if __name__ == '__main__':
    pass