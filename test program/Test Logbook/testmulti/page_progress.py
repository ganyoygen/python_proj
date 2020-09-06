import tkinter as tk
import mysql.connector
import os
import csv # untuk write ke Excel
import time
import datetime

from mysqlcon import read_db_config
from entryDate import CustomDateEntry # input tgl pake kalender
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText

kolomProgIfca = ("WO","IFCA","UNIT")
kolomCommIfca = ("TANGGAL","UPDATE","OLEH","DEPT")

class PageProg(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # label = tk.Label(self, text="This is page 2")
        # label.pack(fill ="both", expand=True, padx=20, pady=10)
        self.komponenProgress()

    def komponenProgress(self):
        # tab progress
        topFrame = Frame(self.tabProgress)
        topFrame.pack(side=TOP,fill=X)
        midFrame = Frame(self.tabProgress)
        midFrame.pack(side=TOP, fill=X)
        botFrame = Frame(self.tabProgress)
        botFrame.pack(expand=YES, side=TOP,fill=Y)
        
        Label(topFrame, text='').grid(row=0, column=0)
        Label(midFrame, text='').grid(row=0, column=0)
        
        entOne = Frame(topFrame)
        entOne.grid(row=1,column=1,sticky=W)
        self.progWo = Entry(entOne, width=10)
        self.progWo.grid(row=1, column=0,sticky=W)
        # Label(entOne, text=' ').grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.progIfca = Entry(entOne, width=15)
        self.progIfca.grid(row=1, column=2,sticky=W)               
        Label(entOne, text=' ').grid(row=1, column=3, sticky=W,pady=5,padx=10)
        self.progUnit = Entry(entOne, width=12)
        self.progUnit.grid(row=1, column=4,sticky=W)

        entTwo = Frame(topFrame)
        entTwo.grid(row=2,column=1,sticky=W)
        self.progTgl = Entry(entTwo, width=15)
        self.progTgl.grid(row=2, column=0,sticky=W)
        # Label(entTwo, text=' ').grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.progJam = Entry(entTwo, width=10)
        self.progJam.grid(row=2, column=1,sticky=W)               
        Label(entTwo, text=' ').grid(row=2, column=2, sticky=W,pady=5,padx=10)
        self.progStaff = Entry(entTwo, width=12)
        self.progStaff.grid(row=2, column=3,sticky=W)
        self.progWorkReq = ScrolledText(topFrame,height=8,width=40)
        self.progWorkReq.grid(row=3, column=1,sticky=W)
            
        entLeft = Frame(topFrame)
        entLeft.grid(row=2,column=5,sticky=W)
        self.commitdate = Entry(entLeft, width=25)
        self.commitdate.grid(row=1, column=0,sticky=W)
        Label(entLeft, text='By :').grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.commitby = Entry(entLeft, width=20)
        self.commitby.grid(row=1, column=2,sticky=W) 
        
        Label(topFrame, text='                  ').grid(row=2,column=2,sticky=W,pady=5,padx=10)
        self.commitDetail = ScrolledText(topFrame,height=8,width=40)
        self.commitDetail.grid(row=3, column=5,sticky=W)
                
        entBtnRight = Frame(topFrame)
        entBtnRight.grid(row=3,column=6,sticky=W)
        self.btnCommUpdate = Button(entBtnRight, text='Update',\
                                command=self.onProgCommUpd, width=10,\
                                relief=RAISED, bd=2, bg="#FC6042", fg="white",activebackground="#444",activeforeground="white" )
        self.btnCommUpdate.grid(row=0,column=0,sticky=N,pady=5,padx=5)
        self.btnCommReturn = Button(entBtnRight, text='Return',\
                                command='self.onProgCommUpd', width=10,\
                                relief=RAISED, bd=2, bg="#FC6042", fg="white",activebackground="#444",activeforeground="white" )
        self.btnCommReturn.grid(row=1,column=0,sticky=N,pady=5,padx=5)
        self.btnCommTake = Button(entBtnRight, text='Take',\
                                command='self.onProgCommUpd', width=10,\
                                relief=RAISED, bd=2, bg="#FC6042", fg="white",activebackground="#444",activeforeground="white" )
        self.btnCommTake.grid(row=2,column=0,sticky=N,pady=5,padx=5)
        self.btnCommDone = Button(entBtnRight, text='Done',\
                                command='self.onProgCommUpd', width=10,\
                                relief=RAISED, bd=2, bg="#FC6042", fg="white",#
                                activebackground="#444",activeforeground="white" )
        self.btnCommDone.grid(row=3,column=0,sticky=N,pady=5,padx=5)
        self.btnRefProg = Button(midFrame, text='Refresh',\
                                command=self.progress_refresh, width=10,\
                                relief=RAISED, bd=2, bg="#667", fg="white",#
                                activebackground="#444",activeforeground="white" )
        self.btnRefProg.grid(row=1,column=0,pady=10,padx=5)
                
        listprog = Frame(botFrame)
        listprog.grid(row=1,column=0,sticky=W)
        listcomm = Frame(botFrame)
        listcomm.grid(row=1,column=1,sticky=W)

        #listprogress
        self.prog_data = Frame(listprog, bd=10)
        self.prog_data.pack(fill=BOTH, expand=YES)
        self.tabelProg = ttk.Treeview(self.prog_data, columns=kolomProgIfca,show='headings')
        self.tabelProg.bind("<Double-1>",self.progress_detail)
        sbVer = Scrollbar(self.prog_data, orient='vertical',command=self.tabelProg.yview)
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor = Scrollbar(self.prog_data, orient='horizontal',command=self.tabelProg.xview)
        sbHor.pack(side=BOTTOM, fill=X)

        self.tabelProg.pack(side=TOP, fill=BOTH)
        self.tabelProg.configure(yscrollcommand=sbVer.set)
        self.tabelProg.configure(xscrollcommand=sbHor.set)

        #listcommited
        self.comm_data = Frame(listcomm, bd=10)
        self.comm_data.pack(fill=BOTH, expand=YES)
        self.tabelcomm = ttk.Treeview(self.comm_data, columns=kolomCommIfca,show='headings')
        self.tabelcomm.bind("<Double-1>",self.prog_comm_detail)
        sbVer = Scrollbar(self.comm_data, orient='vertical',command=self.tabelcomm.yview)
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor = Scrollbar(self.comm_data, orient='horizontal',command=self.tabelcomm.xview)
        sbHor.pack(side=BOTTOM, fill=X)

        self.tabelcomm.pack(side=TOP, fill=BOTH)
        self.tabelcomm.configure(yscrollcommand=sbVer.set)
        self.tabelcomm.configure(xscrollcommand=sbHor.set)
        
        self.progress_refresh()