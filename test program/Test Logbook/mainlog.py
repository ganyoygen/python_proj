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
                frameWin = Frame(self.parent, bg="#666")
                frameWin.pack(fill=X,side=TOP)
                WindowDraggable(frameWin)
                Label(frameWin, text='PETUGAS',bg="#666",fg="white").pack(side=LEFT,padx=20)
                # buttonx = Button(frameWin, text="X",fg="white", bg="#FA8072", width=6, height=2,bd=0,\
                #                  activebackground="#FB8072",activeforeground="white", command=self.keluar, relief=FLAT)
                # Menghilangkan Frame windows
                # self.parent.overrideredirect(1) 
                # buttonx.pack(side=RIGHT)
                #
                mainFrame = Frame(self.parent)
                mainFrame.pack(side=TOP,fill=X)
                btnFrame = Frame(self.parent)
                btnFrame.pack(side=TOP, fill=X)
                tabelFrame = Frame(self.parent)
                tabelFrame.pack(expand=YES, side=TOP,fill=Y)

                Label(mainFrame, text=' ').grid(row=0, column=0)
                Label(btnFrame, text=' ').grid(row=1, column=0)

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
                Label(mainFrame, text="Tanggal Selesai").grid(row=3, column=3, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=3, column=4, sticky=W,pady=5,padx=10)
                tgldone = Frame(mainFrame)
                tgldone.grid(row=3,column=5,sticky=W)
                self.entTgldone = Entry(tgldone, width=15)
                self.entTgldone.grid(row=1, column=0,sticky=W)
                Label(tgldone, text='(dd/mm/yyyy)').grid(row=1, column=3, sticky=E,padx=5)

                Label(mainFrame, text="Jam Selesai").grid(row=4, column=3, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=4, column=4, sticky=W,pady=5,padx=10)             
                self.entJamdone = Entry(mainFrame, width=10)
                self.entJamdone.grid(row=4, column=5,sticky=W)

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

                # open table 
                self.onClear()

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
                        sql = "SELECT no_wo, no_ifca, date_create, unit, work_req, staff, date_done, time_done, work_act, time_create FROM logbook WHERE no_ifca = %s"
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
                                self.entJamdone.insert(END, data[7])
                                self.entWorkAct.insert(END, data[8])
                        except:
                                self.btnReceived.config(state="disable") #tidak dapat receive karena wo belum done
                                pass

                        

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
                
                #panel kanan
                cWorkAct = self.entWorkAct.get('1.0', 'end')
                jamdone = self.entJamdone.get()
                getTglDone = self.checktgl(self.entTgldone.get()) #check tgl dulu
                #eksekusi sql
                sql = "UPDATE logbook SET no_wo=%s,no_ifca=%s,date_create=%s,work_req=%s,staff=%s,date_done=%s,time_done=%s,work_act=%s WHERE no_ifca =%s"
                cur.execute(sql,(cWo,cIfca,getTglBuat,cWorkReq,cStaff,getTglDone,jamdone,cWorkAct,cIfca))
                messagebox.showinfo(title="Informasi", \
                        message="Data sudah di terupdate.")
                cur.close()
                con.close()
                self.onSearch()


def main():
    os.system("cls")
    Petugas(root)
    root.mainloop()
main()
                                                           
                                                                                           
