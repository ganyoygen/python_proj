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
# import tabpending
# from tabpending import pendingTab




root = Tk()
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

btnselect = StringVar(value="TN")
judul_kolom = ("WO","IFCA","Tanggal","UNIT","Work Request","Staff","Work Action","Tanggal Done","Jam Done","Received")
kolomPending = ("WO","IFCA","Tanggal","UNIT","Work Request")
kolomProgIfca = ("WO","IFCA","UNIT")

class Petugas:
        def __init__(self, parent):
                self.parent = parent
                self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
                lebar=950
                tinggi=600
                setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
                setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
                self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
                
                self.aturKomponen()

        def keluar(self,event=None):
                self.parent.destroy()

        def aturKomponen(self):
                # Note: padx(horizontal), pady(vertical)
                frameWin = Frame(self.parent, bg="#898")
                frameWin.pack(fill=X,side=TOP)
                WindowDraggable(frameWin)
                Label(frameWin, text='PETUGAS',bg="#898",fg="white").pack(side=LEFT,padx=20)
                # buttonx = Button(frameWin, text="X",fg="white", bg="#FA8072", width=6, height=2,bd=0,\
                #                  activebackground="#FB8072",activeforeground="white", command=self.keluar, relief=FLAT)
                # # Menghilangkan Frame windows
                # self.parent.overrideredirect(1) 
                # buttonx.pack(side=RIGHT)

                tabControl = ttk.Notebook(root)
                self.tabMain = ttk.Frame(tabControl)
                tabControl.add(self.tabMain, text ='Main')
                self.tabPending = ttk.Frame(tabControl)
                tabControl.add(self.tabPending, text ='Pending')
                self.tabProgress = ttk.Frame(tabControl)
                tabControl.add(self.tabProgress, text ='Progress')            
                tabControl.pack(expand = 1, fill ="both")
                
                self.mainTab()
                self.pendingTab()
                self.onClear()

        def mainTab(self):
                mainFrame = Frame(self.tabMain)
                # mainFrame = Frame(self.parent)
                mainFrame.pack(side=TOP,fill=X)
                btnFrame = Frame(self.tabMain)
                # btnFrame = Frame(self.parent)
                btnFrame.pack(side=TOP, fill=X)
                tabelFrame = Frame(self.tabMain)
                # tabelFrame = Frame(self.parent)
                tabelFrame.pack(expand=YES, side=TOP,fill=Y)

                Label(mainFrame, text='').grid(row=0, column=0)
                Label(btnFrame, text='').grid(row=1, column=0)

                #samping kiri
                Label(mainFrame, text='No WO').grid(row=1, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=1, column=1, sticky=W,pady=5,padx=10)
                self.entWo = Entry(mainFrame, width=20)
                self.entWo.grid(row=1, column=2,sticky=W)

                Label(mainFrame, text="IFCA").grid(row=2, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=2, column=1, sticky=W,pady=5,padx=10)
                self.entIfca = Entry(mainFrame, width=20)
                self.entIfca.grid(row=2, column=2,sticky=W)
                radiobtn = Frame(mainFrame)
                radiobtn.grid(row=2,column=2)
                
                self.rbtnTN = Radiobutton(radiobtn, text="TN", variable=btnselect, value="TN", command=self.auto_ifca,anchor = W)
                self.rbtnTN.grid(row=0, column=0,sticky=W)
                self.rbtnBM = Radiobutton(radiobtn, text="BM", variable=btnselect, value="BM", command=self.auto_ifca,anchor = W)
                Label(radiobtn, text="/").grid(row=0,column=1,sticky=E)
                self.rbtnBM.grid(row=0, column=2,sticky=W)

                #tglbuat
                Label(mainFrame, text="Tanggal - Jam").grid(row=3, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=3, column=1, sticky=W,pady=5,padx=10)
                tglbuat = Frame(mainFrame)
                tglbuat.grid(row=3,column=2,sticky=W)
                self.entTglbuat = Entry(tglbuat, width=12)
                self.entTglbuat.grid(row=1, column=0,sticky=W)
                self.entJambuat = Entry(tglbuat, width=7)
                self.entJambuat.grid(row=1, column=1,sticky=W)
                # self.entBulan = Entry(tglbuat, width=5)
                # self.entBulan.grid(row=1, column=1,sticky=W,padx=2)
                # self.entTahun = Entry(tglbuat, width=10)
                # self.entTahun.grid(row=1, column=2,sticky=W,padx=2)
                # Label(tglbuat, text='(dd/mm/yyyy)').grid(row=1, column=3, sticky=E,padx=5)
                
                Label(mainFrame, text="Unit").grid(row=4, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=4, column=1, sticky=W,pady=5,padx=10)             
                self.entUnit = Entry(mainFrame, width=15)
                self.entUnit.grid(row=4, column=2,sticky=W)

                Label(mainFrame, text="Work Request").grid(row=5, column=0, sticky=NW,padx=20)
                Label(mainFrame, text=':').grid(row=5, column=1, sticky=NW,padx=10,pady=6)
                self.entWorkReq = ScrolledText(mainFrame,height=4,width=35)
                self.entWorkReq.grid(row=5, column=2,sticky=W)

                Label(mainFrame, text="Staff").grid(row=6, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=6, column=1, sticky=W,pady=5,padx=10)
                self.entStaff = Entry(mainFrame, width=20)
                self.entStaff.grid(row=6, column=2,sticky=W)

                #samping kanan
                #tgldone
                Label(mainFrame, text="Status").grid(row=3, column=3, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=3, column=4, sticky=W,pady=5,padx=10)
                # self.statusIfca = Entry(mainFrame, width=15)
                # self.statusIfca.grid(row=3, column=5,sticky=W)

                self.opsiStatus = ttk.Combobox(mainFrame, values = ["","DONE","CANCEL","PENDING"],\
                                                state="readonly", width=10)
                self.opsiStatus.current(0)
                self.opsiStatus.grid(row=3, column=5,sticky=W)
                
                Label(mainFrame, text="Tanggal - Jam").grid(row=4, column=3, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=4, column=4, sticky=W,pady=5,padx=10)             
                tgldone = Frame(mainFrame)
                tgldone.grid(row=4,column=5,sticky=W)
                self.entTgldone = Entry(tgldone, width=12)
                self.entTgldone.grid(row=1, column=0,sticky=W)
                self.entJamdone = Entry(tgldone, width=7)
                self.entJamdone.grid(row=1, column=1,sticky=W)
                # Label(tgldone, text='(dd/mm/yyyy)').grid(row=1, column=3, sticky=E,padx=5)

                Label(mainFrame, text="Work Action").grid(row=5, column=3, sticky=NW,padx=20)
                Label(mainFrame, text=':').grid(row=5, column=4, sticky=NW,padx=10,pady=6)
                self.entWorkAct = ScrolledText(mainFrame,height=4,width=35)
                self.entWorkAct.grid(row=5, column=5,sticky=W)

                #panel button
                self.btnSave = Button(btnFrame, text='Save',\
                                        command=self.onSave, width=10,\
                                        relief=RAISED, bd=2, bg="#666", fg="white",activebackground="#444",activeforeground="white" )
                self.btnSave.grid(row=0, column=1,pady=10,padx=5)

                self.btnUpdate = Button(btnFrame, text='Update',\
                                        command=self.onUpdate,state="disable", width=10,\
                                        relief=RAISED, bd=2, bg="#666", fg="white",activebackground="#444",activeforeground="white")
                self.btnUpdate.grid(row=0,column=2,pady=10,padx=5)
                
                self.btnClear = Button(btnFrame, text='Clear',\
                                        command=self.onClear, width=10,\
                                       relief=RAISED, bd=2, bg="#666", fg="white",activebackground="#444",activeforeground="white")
                self.btnClear.grid(row=0,column=3,pady=10,padx=5)

                self.btnDelete = Button(btnFrame, text='Delete',\
                                        command=self.onDelete,state="disable", width=10,\
                                        relief=RAISED, bd=2, bg="#FC6042", fg="white",activebackground="#444",activeforeground="white")
                self.btnDelete.grid(row=0,column=4,pady=10,padx=5)

                self.btnReceived = Button(btnFrame, text='Received',\
                                        command=self.onReceived,state="disable", width=10,\
                                       relief=RAISED, bd=2, bg="#667", fg="white",activebackground="#444",activeforeground="white")
                self.btnReceived.grid(row=0,column=5,pady=10,padx=5)

                # Label(btnFrame, text="Search :").grid(row=1, column=1, sticky=E,padx=20)
                self.opsicari = ttk.Combobox(btnFrame, values = ["IFCA","Tanggal", "Unit", "Work Req."],\
                                                state="readonly", width=10)
                self.opsicari.current(1)
                self.opsicari.grid(row=1, column=1,sticky=W)
                self.entCari = Entry(btnFrame, width=20)
                self.entCari.grid(row=1, column=2,sticky=W)
                # self.entCari.bind('<KeyRelease>',self.onSearch) #cari saat input apapun
                self.btnSearch = Button(btnFrame, text='Search',\
                                        command=self.onSearch,\
                                        state="normal", width=10,\
                                       relief=RAISED, bd=2, bg="#667", fg="white",activebackground="#444",activeforeground="white")
                self.btnSearch.grid(row=1,column=3,pady=10,padx=5)

                #tabel
                self.fr_data = Frame(tabelFrame, bd=10)
                self.fr_data.pack(fill=BOTH, expand=YES)
                self.trvTabel = ttk.Treeview(self.fr_data, columns=judul_kolom,show='headings')
                self.trvTabel.bind("<Double-1>", self.OnDoubleClick)
                sbVer = Scrollbar(self.fr_data, orient='vertical',command=self.trvTabel.yview)
                sbVer.pack(side=RIGHT, fill=Y)
                sbHor = Scrollbar(self.fr_data, orient='horizontal',command=self.trvTabel.xview)
                sbHor.pack(side=BOTTOM, fill=X)

                self.trvTabel.pack(side=TOP, fill=BOTH)
                self.trvTabel.configure(yscrollcommand=sbVer.set)
                self.trvTabel.configure(xscrollcommand=sbHor.set)

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
                # Label(entOne, text=' ').grid(row=1, column=1, sticky=W,pady=5,padx=10)
                self.pendIfca = Entry(entOne, width=15)
                self.pendIfca.grid(row=1, column=2,sticky=W)               
                Label(entOne, text=' ').grid(row=1, column=3, sticky=W,pady=5,padx=10)
                self.pendUnit = Entry(entOne, width=12)
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
                                        command=self.onAccPending, width=10,\
                                        relief=RAISED, bd=2, bg="#FC6042", fg="white",activebackground="#444",activeforeground="white" )
                self.btnAccept.grid(row=2, column=2,pady=10,padx=5)

                Label(topFrame, text='                  ').grid(row=2, column=2, sticky=W,pady=5,padx=10)
                self.pendWorkAct = ScrolledText(topFrame,height=8,width=40)
                self.pendWorkAct.grid(row=3, column=5,sticky=W)

                self.btnRefresh = Button(midFrame, text='Refresh',\
                                        command=self.pending_refresh, width=10,\
                                        relief=RAISED, bd=2, bg="#667", fg="white",activebackground="#444",activeforeground="white" )
                self.btnRefresh.grid(row=1, column=0,pady=10,padx=5)

                #tabel
                self.pend_data = Frame(botFrame, bd=10)
                self.pend_data.pack(fill=BOTH, expand=YES)
                self.tabelPend = ttk.Treeview(self.pend_data, columns=kolomPending,show='headings')
                self.tabelPend.bind("<Double-1>",self.pending_detail)
                sbVer = Scrollbar(self.pend_data, orient='vertical',command=self.tabelPend.yview)
                sbVer.pack(side=RIGHT, fill=Y)
                sbHor = Scrollbar(self.pend_data, orient='horizontal',command=self.tabelPend.xview)
                sbHor.pack(side=BOTTOM, fill=X)

                self.tabelPend.pack(side=TOP, fill=BOTH)
                self.tabelPend.configure(yscrollcommand=sbVer.set)
                self.tabelPend.configure(xscrollcommand=sbHor.set)

                #showtable
                self.pending_refresh()

        def progressTab(self):
                # tab progress
                topFrame = Frame(self.tabProgress)
                topFrame.pack(side=TOP,fill=X)
                midFrame = Frame(self.tabProgress)
                midFrame.pack(side=TOP, fill=X)
                botFrame = Frame(self.tabProgress)
                botFrame.pack(expand=YES, side=TOP,fill=Y)

                Label(topFrame, text='').grid(row=0, column=0)
                Label(midFrame, text='').grid(row=1, column=0)
                
                listProg = Frame(botFrame)
                listProg.grid(row=1,column=0,sticky=W)
                listPend = Frame(botFrame)
                listPend.grid(row=1,column=1,sticky=W)

                #listPend
                self.prog_data = Frame(listProg, bd=10)
                self.prog_data.pack(fill=BOTH, expand=YES)
                self.tabelProg = ttk.Treeview(self.prog_data, columns=kolomProgIfca,show='headings')
                self.tabelProg.bind("<Double-1>","self.pending_detail")
                sbVer = Scrollbar(self.prog_data, orient='vertical',command=self.tabelProg.yview)
                sbVer.pack(side=RIGHT, fill=Y)
                sbHor = Scrollbar(self.prog_data, orient='horizontal',command=self.tabelProg.xview)
                sbHor.pack(side=BOTTOM, fill=X)

                self.tabelProg.pack(side=TOP, fill=BOTH)
                self.tabelProg.configure(yscrollcommand=sbVer.set)
                self.tabelProg.configure(xscrollcommand=sbHor.set)

        def read_db_config(self,filename='C:\\config.ini', section='mysql'):
                """ Read database configuration file and return a dictionary object
                :param filename: name of the configuration file
                :param section: section of database configuration
                :return: a dictionary of database parameters
                """
                # create parser and read ini configuration file
                parser = ConfigParser()
                parser.read(filename)

                # get section, default to mysql
                db = {}
                if parser.has_section(section):
                    items = parser.items(section)
                    for item in items:
                        db[item[0]] = item[1]
                else:
                    raise Exception('{0} not found in the {1} file'.format(section, filename))
            
                return db

        def checkwo(self,data):
                db_config = self.read_db_config()
                con = mysql.connector.connect(**db_config)
                cur = con.cursor()
                sql = ("SELECT * FROM logbook where no_wo LIKE %s")
                cur.execute(sql,(data,))
                hasil = cur.fetchone()
                if cur.rowcount < 0:
                        pass
                else:
                        if len(data) < 1: # Jika wo kosong
                                return "terima" 
                        if (data == hasil[1]):
                                return "tolak"
                print(len(data))
                cur.close()
                con.close()

        def checkifca(self,data):
                db_config = self.read_db_config()
                con = mysql.connector.connect(**db_config)
                cur = con.cursor()
                sql = ("SELECT * FROM logbook where no_ifca LIKE %s")
                cur.execute(sql,(data,))
                hasil = cur.fetchone()
                if cur.rowcount < 0:
                        pass
                else:
                        if (data.upper() == hasil[2].upper()):
                                return "tolak"
                cur.close()
                con.close()

        def checktgl(self,data):
                if len(str(data)) == 10:
                        cHari = str(data)[0:2]
                        cBulan = str(data)[3:5]
                        cTahun = str(data)[6:]
                        return datetime.date(int(cTahun),int(cBulan),int(cHari))
                else:
                        return None

        def search_data(self,opsi,data):
                try:
                    db_config = self.read_db_config()
                    con = mysql.connector.connect(**db_config)
                    cur = con.cursor()
                    cur.execute(opsi, data)
                    results = cur.fetchall()
                    print('---',cur.rowcount,'ditemukan ---')
                    cur.close()
                    con.close() 
                    self.showtable(results)

                except mysql.connector.Error as err:
                    print("SQL Log: {}".format(err))

        def onSearch(self):
                opsi = self.opsicari.get()
                cari = self.entCari.get()
                if opsi == "Tanggal":
                        cari = self.checktgl(cari)
                        sql = "SELECT * FROM logbook WHERE date_create LIKE %s"
                        val = ("%{}%".format(cari),)
                        self.search_data(sql,val)
                elif opsi == "IFCA":
                        sql = "SELECT * FROM logbook WHERE no_ifca LIKE %s"
                        val = ("%{}%".format(cari),)
                        self.search_data(sql,val)
                elif opsi == "Unit":
                        sql = "SELECT * FROM logbook WHERE unit LIKE %s"
                        val = ("%{}%".format(cari),)
                        self.search_data(sql,val)
                elif opsi == "Work Req.":
                        sql = "SELECT * FROM logbook WHERE work_req LIKE %s"
                        val = ("%{}%".format(cari),)
                        self.search_data(sql,val)

        def auto_wo(self):
                db_config = self.read_db_config()
                con = mysql.connector.connect(**db_config)
                cur = con.cursor()
                sql = "SELECT no_wo FROM logbook"
                cur.execute(sql)
                hasil = cur.fetchall() # buat dulu daftar wo

                if len(hasil) <= 0: # prevent error jika belum ada data
                        hasil = "0"

                lastwo = hasil[len(hasil)-1] # Max num wo terakhir
                print("Jumlah Wo:",len(hasil)) # Jumlah wo didapat
                newWoNum = (int(max(lastwo))+1) # cari wo, + 1
                getNewWo = str(newWoNum) # Wo baru siap dipakai
                print("Get new Wo:",getNewWo) 
                self.entWo.delete(0, END)
        
                if len(str(getNewWo)) <= 6:
                    self.entWo.insert(0, getNewWo)
                    self.entIfca.focus_set()
                else:
                    messagebox.showwarning(title="Peringatan", \
                            message="maaf lebar data untuk no WO hanya sampai 6 digit")

                self.entWo.config(state="normal")
                cur.close()
                con.close()

        def auto_ifca(self):
                tipe = str(btnselect.get())
                db_config = self.read_db_config()
                con = mysql.connector.connect(**db_config)
                cur = con.cursor()
                sql = "SELECT no_ifca FROM logbook WHERE no_ifca LIKE %s"
                val = ("%{}%".format(tipe),)
                cur.execute(sql, val)
                hasil = cur.fetchall()

                # for get in hasil:  
                        # ifcalist = [get] # buat dulu daftar ifca
                lastifca = max(hasil) # Max num ifca terakhir
                print("Jumlah IFCA:",len(hasil)) # Jumlah ifca didapat
                newIfcaNum = (int(max(lastifca)[2:])+1) # cari lastifca, hapus tipe(BM/TN) + 1
                getNewIfca = tipe+str(newIfcaNum) # Ifca baru siap dipakai
                print("Get new ifca:",getNewIfca) 
                self.entIfca.delete(0, END)
                self.entIfca.insert(0,getNewIfca)
                self.entIfca.config(state="normal")
                cur.close()
                con.close()

        def pending_table(self):
                try:
                    db_config = self.read_db_config()
                    con = mysql.connector.connect(**db_config)
                    cur = con.cursor()
                    sql = "SELECT * FROM logbook WHERE status_ifca LIKE %s"
                    data = "PENDING"
                    val = ("%{}%".format(data),)
                #     data = "%PENDING%"
                    cur.execute(sql, val)
                    results = cur.fetchall()

                    self.tabelPend.delete(*self.tabelPend.get_children()) #refresh, hapus dulu tabel lama
                    for kolom in kolomPending:
                        self.tabelPend.heading(kolom,text=kolom)

                    # self.tabelPend.column("No", width=10,anchor="w")
                    self.tabelPend.column("WO", width=50,anchor="w")
                    self.tabelPend.column("IFCA", width=80,anchor="w")
                    self.tabelPend.column("Tanggal", width=80,anchor="w")
                    self.tabelPend.column("UNIT", width=80,anchor="w")
                    self.tabelPend.column("Work Request", width=200,anchor="w")
            
                    i=0
                    for dat in results: 
                        if(i%2):
                            baris="genap"
                        else:
                            baris="ganjil"
                        #hilangkan nomor mulai dari kolom wo dat[1:]
                        self.tabelPend.insert('', 'end', values=dat[1:], tags=baris)
                        i+=1

                    self.tabelPend.tag_configure("ganjil", background="#FFFFFF")
                    self.tabelPend.tag_configure("genap", background="whitesmoke")

                    cur.close()
                    con.close()
                
                except mysql.connector.Error as err:
                    messagebox.showerror(title="Error", \
                        message="SQL Log: {}".format(err))                           

        def showtable(self,data):
                self.trvTabel.delete(*self.trvTabel.get_children()) #refresh, hapus dulu tabel lama
                for kolom in judul_kolom:
                    self.trvTabel.heading(kolom,text=kolom)

                # self.trvTabel.column("No", width=10,anchor="w")
                self.trvTabel.column("WO", width=50,anchor="w")
                self.trvTabel.column("IFCA", width=80,anchor="w")
                self.trvTabel.column("Tanggal", width=80,anchor="w")
                self.trvTabel.column("UNIT", width=80,anchor="w")
                self.trvTabel.column("Work Request", width=120,anchor="w")
                self.trvTabel.column("Staff", width=70,anchor="w")
                self.trvTabel.column("Work Action", width=120,anchor="w")
                self.trvTabel.column("Tanggal Done", width=80,anchor="w")
                self.trvTabel.column("Jam Done", width=40,anchor="w")
                self.trvTabel.column("Received", width=40,anchor="w")
            
                i=0
                for dat in data: 
                    if(i%2):
                        baris="genap"
                    else:
                        baris="ganjil"
                    #hilangkan nomor mulai dari kolom wo dat[1:]
                    self.trvTabel.insert('', 'end', values=dat[1:], tags=baris)
                    i+=1

                self.trvTabel.tag_configure("ganjil", background="#FFFFFF")
                self.trvTabel.tag_configure("genap", background="whitesmoke")                              

        def onReceived(self):
                cIfca = self.entIfca.get()
                if len(cIfca) == 0:
                        messagebox.showwarning(title="Peringatan",message="No IFCA Kosong.")
                        self.entIfca.focus_set()
                else:
                        db_config = self.read_db_config()
                        con = mysql.connector.connect(**db_config)
                        cur = con.cursor()
                        setreceived = True
                        from datetime import datetime
                        tsekarang = datetime.now()
                        sql = "UPDATE logbook SET date_received=%s,received=%s WHERE no_ifca =%s"
                        cur.execute(sql,(tsekarang,setreceived,cIfca))
                        self.onSearch() #update received sesuai tabel yg dicari
                        messagebox.showinfo(title="Informasi", \
                                    message="Wo {} sudah diterima.".format(cIfca))
                        cur.close()
                        con.close()               

        def pending_detail(self, event):
                try:
                        curItem = self.tabelPend.item(self.tabelPend.focus())
                        ifca_value = curItem['values'][1]  

                        self.pendWo.config(state="normal")
                        self.pendIfca.config(state="normal")
                        self.pendUnit.config(state="normal")
                        self.pendTgl.config(state="normal")
                        self.pendJam.config(state="normal")
                        self.pendStaff.config(state="normal")
                        self.pendWorkReq.config(state="normal")
                        self.pendWorkAct.config(state="normal")
                        self.pendWo.delete(0, END)
                        self.pendIfca.delete(0, END)
                        self.pendUnit.delete(0, END)
                        self.pendTgl.delete(0, END)
                        self.pendJam.delete(0, END)
                        self.pendStaff.delete(0, END)
                        self.pendWorkAct.delete('1.0', 'end')
                        self.pendWorkReq.delete('1.0', 'end')

                        self.pendIfca.insert(END, ifca_value)

                        cIfca = self.pendIfca.get()
                        db_config = self.read_db_config()
                        con = mysql.connector.connect(**db_config)
                        cur = con.cursor()
                        # sql = "SELECT no_wo, no_ifca, date_create, time_create, unit, work_req, staff, work_act, FROM logbook WHERE no_ifca = %s"
                        sql = "SELECT no_wo, no_ifca, date_create, unit, work_req, staff, work_act, time_create FROM logbook WHERE no_ifca = %s"
                        cur.execute(sql,(cIfca,))
                        data = cur.fetchone()
                        self.pendWo.insert(END, data[0])
                        #TGL buat
                        self.pendTgl.insert(END, data[2])
                        getTgl = self.pendTgl.get() #dari mysql YYYY-MM-DD
                        #balikin menjadi DD-MM-YYYY
                        showtgl = str(getTgl)[8:] + '-' + str(getTgl)[5:7] +'-' + str(getTgl)[:4]
                        self.pendTgl.delete(0, END)
                        self.pendTgl.insert(END, showtgl)
                        self.pendJam.insert(END, data[7])
                        self.pendUnit.insert(END, data[3])
                        self.pendWorkReq.insert(END, data[4])
                        self.pendStaff.insert(END, data[5])
                        self.pendWorkAct.insert(END, data[6])

                        self.pendWo.config(state="readonly")
                        self.pendIfca.config(state="readonly")
                        self.pendUnit.config(state="readonly")
                        self.pendTgl.config(state="readonly")
                        self.pendJam.config(state="readonly")
                        self.pendStaff.config(state="readonly")
                        self.pendWorkReq.config(state="disable")
                        self.pendWorkAct.config(state="disable")
                        self.btnAccept.config(state="normal")
                        cur.close()
                        con.close()
                        # self.pending_table()
                except:
                        print('Tidak ada data di tabel')

        def OnDoubleClick(self, event):
                try:
                        curItem = self.trvTabel.item(self.trvTabel.focus())
                        ifca_value = curItem['values'][1]  

                        self.entWo.config(state="normal")
                        self.entIfca.config(state="normal")
                        self.entTglbuat.config(state="normal")
                        self.entJambuat.config(state="normal")
                        self.entUnit.config(state="normal")
                        self.entWo.delete(0, END)
                        self.entIfca.delete(0, END)
                        self.entTglbuat.delete(0, END)
                        self.entJambuat.delete(0, END)
                        self.entUnit.delete(0, END)
                        self.entWorkReq.delete('1.0', 'end')
                        self.entStaff.delete(0, END)
                        self.entTgldone.delete(0, END)
                        self.entJamdone.delete(0, END)
                        self.entWorkAct.delete('1.0', 'end')

                        self.btnSave.config(state="disable")
                        self.btnUpdate.config(state="normal")
                        self.btnDelete.config(state="normal")
                        self.btnReceived.config(state="normal")
                        self.rbtnBM.config(state="disable")
                        self.rbtnTN.config(state="disable")

                        self.entIfca.insert(END, ifca_value)

                        cIfca = self.entIfca.get()
                        db_config = self.read_db_config()
                        con = mysql.connector.connect(**db_config)
                        cur = con.cursor()
                        sql = "SELECT no_wo, no_ifca, date_create, unit, work_req, staff, date_done, time_done, work_act, time_create, status_ifca FROM logbook WHERE no_ifca = %s"
                        cur.execute(sql,(cIfca,))
                        data = cur.fetchone()

                        self.entWo.insert(END, data[0])
                        #TGL buat
                        self.entTglbuat.insert(END, data[2])
                        getTgl = self.entTglbuat.get() #dari mysql YYYY-MM-DD
                        #balikin menjadi DD-MM-YYYY
                        showtgl = str(getTgl)[8:] + '-' + str(getTgl)[5:7] +'-' + str(getTgl)[:4]
                        self.entTglbuat.delete(0, END)
                        self.entTglbuat.insert(END, showtgl)
                        self.entJambuat.insert(END, data[9])
                        
                        if data[10] == "DONE":
                                self.opsiStatus.current(1)
                        elif data[10] == "CANCEL":
                                self.opsiStatus.current(2)
                                self.btnReceived.config(state="disable") #tidak dapat receive karena wo belum done
                        elif data[10] == "PENDING":
                                self.opsiStatus.current(3)
                                self.btnReceived.config(state="disable") #tidak dapat receive karena wo belum done
                        else:
                                self.opsiStatus.current(0)
                                self.btnReceived.config(state="disable") #tidak dapat receive karena wo belum done

                        self.entUnit.insert(END, data[3])
                        self.entWorkReq.insert(END, data[4])
                        self.entStaff.insert(END, data[5])

                        #TGL done
                        try: 
                                self.entTgldone.insert(END, data[6])
                                getTgldone = self.entTgldone.get() #dari mysql YYYY-MM-DD
                                #balikin menjadi DD-MM-YYYY
                                showtgldone = str(getTgldone)[8:] + '-' + str(getTgldone)[5:7] +'-' + str(getTgldone)[:4]
                                self.entTgldone.delete(0, END)
                                self.entTgldone.insert(END, showtgldone)
                        except:
                                pass

                        self.entJamdone.insert(END, data[7])
                        self.entWorkAct.insert(END, data[8])
                        # jangan update ifca, tgl, unit
                        self.entWo.config(state="readonly")
                        self.entIfca.config(state="readonly")
                        self.entTglbuat.config(state="readonly")
                        self.entJambuat.config(state="readonly")
                        self.entUnit.config(state="readonly")
                        cur.close()
                        con.close()
                except:
                        print('Tidak ada data di tabel')

        def onDelete(self):
                db_config = self.read_db_config()
                con = mysql.connector.connect(**db_config)
                cur = con.cursor()
                self.entWo.config(state="normal")
                cIfca = self.entIfca.get()
                sql = "DELETE FROM logbook WHERE no_ifca =%s"
                cur.execute(sql,(cIfca,))
                self.onClear()
                messagebox.showinfo(title="Informasi", \
                                    message="Data sudah di hapus.")
                
                cur.close()
                con.close()

        def pending_refresh(self):
                # refresh juga tab Pending
                self.btnAccept.config(state="disable")
                self.pendWo.config(state="normal")
                self.pendIfca.config(state="normal")
                self.pendUnit.config(state="normal")
                self.pendTgl.config(state="normal")
                self.pendJam.config(state="normal")
                self.pendStaff.config(state="normal")
                self.pendWorkReq.config(state="normal")
                self.pendWorkAct.config(state="normal")
                self.pendWo.delete(0, END)
                self.pendIfca.delete(0, END)
                self.pendUnit.delete(0, END)
                self.pendTgl.delete(0, END)
                self.pendJam.delete(0, END)
                self.pendStaff.delete(0, END)
                self.pendWorkAct.delete('1.0', 'end')
                self.pendWorkReq.delete('1.0', 'end')
                self.pending_table()
                #########

        def onClear(self):
                self.btnSave.config(state="normal")
                self.btnUpdate.config(state="disable")
                self.btnDelete.config(state="disable")
                self.btnReceived.config(state="disable")
                self.rbtnBM.config(state="normal")
                self.rbtnTN.config(state="normal")
                self.entWo.config(state="normal")
                self.entIfca.config(state="normal")
                self.entTglbuat.config(state="normal")
                self.entJambuat.config(state="normal")
                self.entUnit.config(state="normal")
                self.entWo.delete(0, END)
                self.entIfca.delete(0, END)
                self.entTglbuat.delete(0, END)
                self.entJambuat.delete(0, END)
                self.entUnit.delete(0, END)
                self.entWorkReq.delete('1.0', 'end')
                self.entStaff.delete(0, END)
                self.entTgldone.delete(0, END)
                self.entJamdone.delete(0, END)
                self.entWorkAct.delete('1.0', 'end')
                self.entCari.delete(0, END)
                self.trvTabel.delete(*self.trvTabel.get_children())

                self.opsiStatus.current(0)

                # list wo hari ini
                self.opsicari.current(1)
                from datetime import date
                today = date.today()
                self.entCari.insert(END,today.strftime("%d-%m-%Y"))
                self.onSearch()
                # self.fr_data.after(0, self.search_data("no_ifca",""))

                # tanggal otomatis hari ini
                self.entTglbuat.insert(END,today.strftime("%d-%m-%Y"))

                self.auto_wo()
                self.entUnit.focus_set()
                os.system("cls")

        def onSave(self):
                db_config = self.read_db_config()
                con = mysql.connector.connect(**db_config)
 
                cWo = self.entWo.get()
                cIfca = self.entIfca.get()
                cTglBuat = self.entTglbuat.get()
                cJamBuat = self.entJambuat.get()
                cUnit = self.entUnit.get()
                cWorkReq = self.entWorkReq.get('1.0', 'end')
                cStaff = self.entStaff.get()
                cIfca = self.entIfca.get()
                if self.checkwo(cWo) == "tolak": #check WO
                        messagebox.showerror(title="Error", \
                        message="Wo {} sudah terdaftar.".format(cWo))
                elif len(cIfca) == 0:
                        messagebox.showwarning(title="Peringatan",message="No IFCA Kosong.")
                        self.entIfca.focus_set()
                elif self.checktgl(cTglBuat) == None: #check tgl jika kosong, batalkan save
                        messagebox.showerror(title="Error",message="Format tanggal salah")    
                elif len(cJamBuat) == 0:
                        messagebox.showwarning(title="Peringatan",message="Jam buat harus diisi.")
                        self.entJambuat.focus_set()
                elif len(cUnit) == 0:
                        messagebox.showwarning(title="Peringatan",message="Unit harus diisi.")
                        self.entUnit.focus_set()
                elif self.checkifca(cIfca) == "tolak": #check IFCA
                        messagebox.showerror(title="Error", \
                        message="{} sudah terdaftar.".format(cIfca))
                        self.entIfca.focus_set()
                else:
                        cur = con.cursor()
                        sql = "INSERT INTO logbook (no_wo, no_ifca, date_create, time_create, unit, work_req, staff)"+\
                              "VALUES(%s,%s,%s,%s,%s,%s,%s)"
                        cur.execute(sql,(cWo,cIfca.upper(),self.checktgl(cTglBuat),cJamBuat,cUnit.upper(),cWorkReq,cStaff))
                        messagebox.showinfo(title="Informasi", \
                                            message="Data sudah di tersimpan.")
                        cur.close()
                        con.close()
                        self.onClear()

        def onUpdate(self):
                db_config = self.read_db_config()
                con = mysql.connector.connect(**db_config)
                cur = con.cursor()
                #panel kiri
                cWo = self.entWo.get()
                cIfca = self.entIfca.get()
                getTglBuat = self.checktgl(self.entTglbuat.get()) #check tgl dulu
                cWorkReq = self.entWorkReq.get('1.0', 'end')
                cStaff = self.entStaff.get()
                cStatus = self.opsiStatus.get()
                
                #panel kanan
                cWorkAct = self.entWorkAct.get('1.0', 'end')
                jamdone = self.entJamdone.get()
                getTglDone = self.checktgl(self.entTgldone.get()) #check tgl dulu
                #eksekusi sql
                sql = "UPDATE logbook SET no_wo=%s,no_ifca=%s,date_create=%s,work_req=%s,staff=%s,status_ifca=%s,date_done=%s,time_done=%s,work_act=%s WHERE no_ifca =%s"
                cur.execute(sql,(cWo,cIfca,getTglBuat,cWorkReq,cStaff,cStatus,getTglDone,jamdone,cWorkAct,cIfca))
                messagebox.showinfo(title="Informasi", \
                        message="Data sudah di terupdate.")
                cur.close()
                con.close()
                self.onSearch()

        def onAccPending(self):
                db_config = self.read_db_config()
                con = mysql.connector.connect(**db_config)
                cur = con.cursor()
                getIfca = self.pendIfca.get()
                getAccBy = self.accpStaff.get()
                getCauses = self.pendWorkAct.get('1.0', 'end')
                from datetime import datetime
                getTimeAcc = datetime.now()
                firstcom = "WO Sudah diterima oleh"

                if len(getAccBy) == 0:
                        messagebox.showwarning(title="Peringatan",message="Siapa yang menerima WO?")
                        self.accpStaff.focus_set()
                else:
                        sql1 = "INSERT INTO onprogress (no_ifca,date_update,commit_update,auth_by,auth_login)"+\
                        "VALUES(%s,%s,%s,%s,%s)"
                        cur.execute(sql1,(getIfca,getTimeAcc,getCauses,getAccBy.upper(),""))

                        sql2 = "INSERT INTO onprogress (no_ifca,date_update,commit_update,auth_by,auth_login)"+\
                        "VALUES(%s,%s,%s,%s,%s)"
                        cur.execute(sql2,(getIfca,getTimeAcc,firstcom,getAccBy.upper(),""))

                        cur.close()
                        con.close()
                        messagebox.showinfo(title="Informasi",message="WO sudah diterima oleh {}.".format(getAccBy))
                        self.pending_refresh()
                        



def main():
    os.system("cls")
    Petugas(root)
    root.mainloop()
main()
                                                           
                                                                                           
