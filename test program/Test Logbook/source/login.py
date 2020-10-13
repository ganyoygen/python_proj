import mysql.connector
import tkinter
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk # make sure to pip install ttkthemes


root = ThemedTk(theme='blue')

class Login:
    def __init__(self,parent,title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
        lebar=250
        tinggi=100
        setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
        setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.aturKomponen()
        
    def aturKomponen(self):
        frameUtama = ttk.Frame(root)
        frameUtama.pack(side=TOP,fill=BOTH)

        ttk.Label(frameUtama, text="Username").grid(row=1, column=1, sticky=W,padx=6)
        ttk.Label(frameUtama, text="Password").grid(row=2, column=1, sticky=W,padx=6)

        self.entryUsername = ttk.Entry(frameUtama,width=17)
        self.entryUsername.grid(row=1, column=2,sticky=W)
        self.entryUsername.bind('<Return>', self.letEntryPass)

        self.entryPassword = ttk.Entry(frameUtama,show='+',width=17)
        self.entryPassword.grid(row=2, column=2,sticky=W)
        self.entryPassword.bind('<Return>', self.proses)

        self.buttonLogin = ttk.Button(frameUtama, text="Login", command=self.proses,\
                             width=10)
        self.buttonLogin.grid(row=3, column=2)

        self.entryUsername.focus_set()

    def keluar(self,event=None):
        self.parent.destroy()

    def letEntryPass(self,event=None):
        self.entryPassword.focus_set()

    #proses cek user dan pass
    def proses(self,event=None):
        user = str("admin")
        password = str("admin")
    
        if (str(self.entryUsername.get()) == user) and (str(self.entryPassword.get()) == password):
            root.destroy()
            # import main
            from main import start
            start(user)
        elif (user==""):
            self.entryUsername.focus_set()
        elif (password==""):
            self.entryPassword.focus_set()
        else:
            self.entryUsername.delete(0, END)
            self.entryPassword.delete(0, END)
            self.entryUsername.focus_set()

def main():
    Login(root, "Login Program")
    root.mainloop()
main()

