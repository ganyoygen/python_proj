import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from configparser import ConfigParser
import mysql.connector
import datetime
import time
import os
# import mainlog
from mainlog import aturKomponen

root = Tk()
kolomPending = ("WO","IFCA","Tanggal","UNIT","Work Request")

class Pending:
    def __init__(self, parent):
        self.parent = parent

    def pendingTab(self):
        # tab pending
        topFrame = Frame(self.tabPending)
        topFrame.pack(side=TOP,fill=X)
        midFrame = Frame(self.tabPending)
        midFrame.pack(side=TOP, fill=X)
        botFrame = Frame(self.tabPending)
        botFrame.pack(expand=YES, side=TOP,fill=Y)

        Label(topFrame, text='').grid(row=0, column=0)
        Label(midFrame, text='').grid(row=1, column=0)

        entOne = Frame(topFrame)
        entOne.grid(row=1,column=1,sticky=W)
        self.pendWo = Entry(entOne, width=10)
        self.pendWo.grid(row=1, column=0,sticky=W)
        Label(entOne, text=' ').grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.pendIfca = Entry(entOne, width=15)
        self.pendIfca.grid(row=1, column=2,sticky=W)               
        Label(entOne, text=' ').grid(row=1, column=3, sticky=W,pady=5,padx=10)
        self.pendUnit = Entry(entOne, width=10)
        self.pendUnit.grid(row=1, column=4,sticky=W)

        entTwo = Frame(topFrame)
        entTwo.grid(row=2,column=1,sticky=W)
        self.pendTgl = Entry(entTwo, width=12)
        self.pendTgl.grid(row=2, column=0,sticky=W)
        # Label(entTwo, text=' ').grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.pendJam = Entry(entTwo, width=7)
        self.pendJam.grid(row=2, column=1,sticky=W)               
        Label(entTwo, text=' ').grid(row=2, column=2, sticky=W,pady=5,padx=10)
        self.pendStaff = Entry(entTwo, width=12)
        self.pendStaff.grid(row=2, column=3,sticky=W)

        self.pendWorkReq = ScrolledText(topFrame,height=8,width=40)
        self.pendWorkReq.grid(row=3, column=1,sticky=W)

        entLeft = Frame(topFrame)
        entLeft.grid(row=2,column=5,sticky=W)
        Label(entLeft, text='By :').grid(row=2, column=0, sticky=W,pady=5,padx=10)
        self.accpStaff = Entry(entLeft, width=20)
        self.accpStaff.grid(row=2, column=1,sticky=W) 
        self.btnAccept = Button(entLeft, text='Accept',\
                                command="", width=10,\
                                relief=RAISED, bd=2, bg="#FC6042", fg="white",activebackground="#444",activeforeground="white" )
        self.btnAccept.grid(row=2, column=2,pady=10,padx=5)

        Label(topFrame, text='                  ').grid(row=2, column=2, sticky=W,pady=5,padx=10)
        self.pendWorkAct = ScrolledText(topFrame,height=8,width=40)
        self.pendWorkAct.grid(row=3, column=5,sticky=W)

        #tabel
        self.pend_data = Frame(botFrame, bd=10)
        self.pend_data.pack(fill=BOTH, expand=YES)
        self.tabelPend = ttk.Treeview(self.pend_data, columns=kolomPending,show='headings')
        self.tabelPend.bind("<Double-1>", "self.OnDoubleClick")
        sbVer = Scrollbar(self.pend_data, orient='vertical',command=self.tabelPend.yview)
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor = Scrollbar(self.pend_data, orient='horizontal',command=self.tabelPend.xview)
        sbHor.pack(side=BOTTOM, fill=X)

        self.tabelPend.pack(side=TOP, fill=BOTH)
        self.tabelPend.configure(yscrollcommand=sbVer.set)
        self.tabelPend.configure(xscrollcommand=sbHor.set)


def main():
    Pending(root)
    root.mainloop()


