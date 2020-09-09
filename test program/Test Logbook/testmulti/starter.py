import os
import tkinter
from tkinter import *
from tkinter import ttk
from page_main import PageMain
from page_pending import Pending
from page_progress import PageProg
from ttkthemes import ThemedTk # make sure to pip install ttkthemes

# root = Tk()
root = ThemedTk(theme='clearlooks')
btnselect = StringVar(value="TN")
statwosel = StringVar(value="PEND")
class WindowDraggable():
    def __init__(self, label):
            self.label = label
            label.bind('<ButtonPress-1>', self.StartMove)
            label.bind('<ButtonRelease-1>', self.StopMove)
            label.bind('<B1-Motion>', self.OnMotion)

    def StartMove(self, event):
            self.x = event.x
            self.y = event.y

    def StopMove(self, event):
            self.x = None
            self.y = None

    def OnMotion(self,event):
            x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
            y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
            root.geometry("+%s+%s" % (x, y))

class MainLog:
    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
        lebar=950
        tinggi=600
        setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
        setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        
        self.aturKomponen()
    
    def aturKomponen(self):
        frameWin = Frame(self.parent, bg="#898")
        frameWin.pack(fill=X,side=TOP)
        WindowDraggable(frameWin)
        Label(frameWin, text='Work Order Logbook Record',bg="#898",fg="white").pack(side=LEFT,padx=20)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        page1 = PageMain(self.notebook,btnselect) # untuk radiobutton tambah positional di __init__() Class PageMain
        page2 = Pending(self.notebook)
        page3 = PageProg(self.notebook,statwosel)
        self.notebook.add(page1, text="Main")
        self.notebook.add(page2, text="Pending")
        self.notebook.add(page3, text="Progress")

    def keluar(self,event=None):
        self.parent.destroy()

def main():
    os.system("cls")
    root.title("Project Logbook by GanyoyGen")
    root.iconbitmap(str(os.getcwd()+"\\"+"mainicon.ico"))
    MainLog(root)
    root.mainloop()
main()