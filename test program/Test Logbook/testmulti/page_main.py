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

judul_kolom = ("WO","IFCA","Tanggal","UNIT","Work Request","Staff","Work Action","Tanggal Done","Jam Done","Received")

class PageMain(tk.Frame):
    def __init__(self,parent,btnselect):
        tk.Frame.__init__(self,parent)
        self.btnselect = btnselect

        # label = tk.Label(self, text="This is page 2")
        # label.pack(fill ="both", expand=True, padx=20, pady=10)
        self.komponenMain()

    def komponenMain(self):
        mainFrame = Frame(self) 
        mainFrame.pack(side=TOP,fill=X)
        btnFrame = Frame(self)
        btnFrame.pack(side=TOP, fill=X)
        tabelFrame = Frame(self)
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

        self.rbtnTN = Radiobutton(radiobtn, text="TN", variable=self.btnselect, value="TN", command=self.auto_ifca,anchor = W)
        self.rbtnTN.grid(row=0, column=0,sticky=W)
        self.rbtnBM = Radiobutton(radiobtn, text="BM", variable=self.btnselect, value="BM", command=self.auto_ifca,anchor = W)
        Label(radiobtn, text="/").grid(row=0,column=1,sticky=E)
        self.rbtnBM.grid(row=0, column=2,sticky=W)

        #tglbuat
        Label(mainFrame, text="Tanggal - Jam").grid(row=3, column=0, sticky=W,padx=20)
        Label(mainFrame, text=':').grid(row=3, column=1, sticky=W,pady=5,padx=10)
        tglbuat = Frame(mainFrame)
        tglbuat.grid(row=3,column=2,sticky=W)
        self.entTglbuat = CustomDateEntry(tglbuat, width=10, locale='en_UK')
        self.entTglbuat.grid(row=1, column=0,sticky=W)
        vcmd = (self.register(self.onValidate), '%d', '%s', '%S')
        self.entJambuat = Entry(tglbuat, validate="key", validatecommand=vcmd, width=7, justify=tk.CENTER)
        self.entJambuat.bind("<KeyRelease>", self.hour_24)
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

        self.opsiStatus = ttk.Combobox(mainFrame, \
            values = ["","DONE","CANCEL","PENDING"],\
            state="readonly", width=10)
        self.opsiStatus.current(0)
        self.opsiStatus.grid(row=3, column=5,sticky=W)

        Label(mainFrame, text="Tanggal - Jam").grid(row=4, column=3, sticky=W,padx=20)
        Label(mainFrame, text=':').grid(row=4, column=4, sticky=W,pady=5,padx=10)             
        tgldone = Frame(mainFrame)
        tgldone.grid(row=4,column=5,sticky=W)
        self.entTgldone = CustomDateEntry(tgldone, width=10, locale='en_UK')
        self.entTgldone.grid(row=1, column=0,sticky=W)
        self.entJamdone = Entry(tgldone, width=7)
        self.entJamdone.grid(row=1, column=1,sticky=W)
        # Label(tgldone, text='(dd/mm/yyyy)').grid(row=1, column=3, sticky=E,padx=5)

        Label(mainFrame, text="Work Action").grid(row=5, column=3, sticky=NW,padx=20)
        Label(mainFrame, text=':').grid(row=5, column=4, sticky=NW,padx=10,pady=6)
        self.entWorkAct = ScrolledText(mainFrame,height=4,width=35)
        self.entWorkAct.grid(row=5, column=5,sticky=W)
                
        Label(mainFrame, text="Received").grid(row=6, column=3, sticky=W,padx=20)
        Label(mainFrame, text=':').grid(row=6, column=4, sticky=W,pady=5,padx=10)
        recentry = Frame(mainFrame)
        recentry.grid(row=6,column=5,sticky=W)
        self.entRecDate = Entry(recentry, width=20)
        self.entRecDate.grid(row=0, column=0,sticky=W)
        self.entRecBy = Entry(recentry, width=25)
        self.entRecBy.grid(row=0, column=1,sticky=W)

        #panel button
        self.btnSave = Button(btnFrame, text='Save',\
            command=self.onSave, width=10,\
            relief=RAISED, bd=2, bg="#666", fg="white",\
            activebackground="#444",activeforeground="white" )
        self.btnSave.grid(row=0, column=1,pady=10,padx=5)

        self.btnUpdate = Button(btnFrame, text='Update',\
            command=self.onUpdate,state="disable", width=10,\
            relief=RAISED, bd=2, bg="#666", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnUpdate.grid(row=0,column=2,pady=10,padx=5)
                
        self.btnClear = Button(btnFrame, text='Clear',\
            command=self.onClear, width=10,\
            relief=RAISED, bd=2, bg="#666", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnClear.grid(row=0,column=3,pady=10,padx=5)

        self.btnDelete = Button(btnFrame, text='Delete',\
            command=self.onDelete,state="disable", width=10,\
            relief=RAISED, bd=2, bg="#FC6042", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnDelete.grid(row=0,column=4,pady=10,padx=5)

        self.btnReceived = Button(btnFrame, text='Received',\
            command=self.onReceived,state="disable", width=10,\
            relief=RAISED, bd=2, bg="#667", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnReceived.grid(row=0,column=5,pady=10,padx=5)

        # Label(btnFrame, text="Search :").grid(row=1, column=1, sticky=E,padx=20)
        self.opsicari = ttk.Combobox(btnFrame, \
            values = ["IFCA","Tanggal", "Unit", "Work Req."], \
            state="readonly", width=10)
        self.opsicari.current(1)
        self.opsicari.grid(row=1, column=1,sticky=W)

        self.entCari = Entry(btnFrame, width=20)
        self.entCari.grid(row=1, column=2,sticky=W)
        # self.entCari.bind('<KeyRelease>',self.onSearch) #cari saat input apapun
        
        self.btnSearch = Button(btnFrame, text='Search',\
            command=self.onSearch,\
            state="normal", width=10,\
            relief=RAISED, bd=2, bg="#667", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnSearch.grid(row=1,column=3,pady=10,padx=5)

        self.btnMainExp = Button(btnFrame, text='Export',\
            command=self.onMainExport,\
            state="normal", width=10,\
            relief=RAISED, bd=2, \
            bg="#558", fg="white", \
            activebackground="#444",activeforeground="white")
        self.btnMainExp.grid(row=1,column=4,pady=10,padx=5)

        #tabel
        self.fr_data = Frame(tabelFrame, bd=10)
        self.fr_data.pack(fill=BOTH, expand=YES)
        self.trvTabel = ttk.Treeview(self.fr_data, columns=judul_kolom,show='headings')
        self.trvTabel.bind("<Double-1>", self.mainlog_detail)
        sbVer = Scrollbar(self.fr_data, orient='vertical',command=self.trvTabel.yview)
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor = Scrollbar(self.fr_data, orient='horizontal',command=self.trvTabel.xview)
        sbHor.pack(side=BOTTOM, fill=X)

        self.trvTabel.pack(side=TOP, fill=BOTH)
        self.trvTabel.configure(yscrollcommand=sbVer.set)
        self.trvTabel.configure(xscrollcommand=sbHor.set)

        self.onClear()

    def onValidate(self, d, s, S):
        # if it's deleting return True
        if d == "0":
            return True
        # Allow only digit, ":" and check the length of the string
        if ((S == ":" and len(s) != 2) or (not S.isdigit() and
                S != ":") or (len(s) == 3 and int(S) > 5) or len(s) > 4):
            self.bell()
            return False
         
        return True
 
    def hour_24(self, event):
        """
        Check and build the correct format hour: hh:mm in 24 format
        it keep in mind the 0x, 1x and 2x hours and the max minutes can be 59
        """
 
        # get the object that triggered the event
        s = event.widget
        # if delete a char do return ok or delete the char ":" and the previous number
        if len(s.get()) == 2 and event.keysym=="BackSpace":
            s.delete(len(s.get())-1, tk.END)
        if event.keysym=="BackSpace":
            return
         
        # check the hour format and add : between hours and minutes
        if len(s.get()) == 1 and int(s.get()) > 2:
            s.insert(0, "0")
            s.insert("end", ":")
        elif len(s.get()) == 2 and int(s.get()) < 24:
            s.insert(2, ":")
        elif len(s.get()) >= 2 and s.get()[2:3] != ":":
            self.bell()
            s.delete(1, tk.END)

    def entrySet(self,opsi):
        # 1 on doubleclick main entry, normal
        if opsi == "mainclear":
            self.entWo.config(state="normal")
            self.entIfca.config(state="normal")
            self.entTglbuat.config(state="normal")
            self.entJambuat.config(state="normal")
            self.entUnit.config(state="normal")
            self.entRecBy.config(state="normal")
            self.entRecDate.config(state="normal")
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
            self.entRecBy.delete(0, END)
            self.entRecDate.delete(0, END)
            self.btnSave.config(state="disable")
            self.btnUpdate.config(state="normal")
            self.btnDelete.config(state="normal")
            self.btnReceived.config(state="normal")
            self.rbtnBM.config(state="disable")
            self.rbtnTN.config(state="disable")
        # mainentry readonly panel kiri kecuali work req dan staff
        if opsi == "mainreadifca":
            self.entWo.config(state="readonly")
            self.entIfca.config(state="readonly")
            self.entTglbuat.config(state="disable")
            self.entJambuat.config(state="readonly")
            self.entUnit.config(state="readonly")
            self.entRecBy.config(state="readonly")
            self.entRecDate.config(state="readonly")
        # 1 #

    def checkwo(self,data):
        try:
            db_config = read_db_config()
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
            cur.close()
            con.close()
        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err))

    def checkifca(self,data):
        try:
            db_config = read_db_config()
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
        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err))

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
            db_config = read_db_config()
            con = mysql.connector.connect(**db_config)
            cur = con.cursor()
            cur.execute(opsi, data)
            results = cur.fetchall()
            print('---',cur.rowcount,'ditemukan ---')
            cur.close()
            con.close()
            self.showtable(results)
        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err)) 

    def onSearch(self):
        opsi = self.opsicari.get()
        cari = self.entCari.get()
        if opsi == "Tanggal":
                cari = self.checktgl(cari)
                sql = "SELECT * FROM logbook WHERE date_create LIKE %s ORDER BY date_create DESC"
                val = ("%{}%".format(cari),)
                self.search_data(sql,val)
        elif opsi == "IFCA":
                sql = "SELECT * FROM logbook WHERE no_ifca LIKE %s ORDER BY no_ifca DESC"
                val = ("%{}%".format(cari),)
                self.search_data(sql,val)
        elif opsi == "Unit":
                sql = "SELECT * FROM logbook WHERE unit LIKE %s ORDER BY date_create DESC"
                val = ("%{}%".format(cari),)
                self.search_data(sql,val)
        elif opsi == "Work Req.":
                sql = "SELECT * FROM logbook WHERE work_req LIKE %s ORDER BY date_create DESC"
                val = ("%{}%".format(cari),)
                self.search_data(sql,val)

    def auto_wo(self):
        try:
            db_config = read_db_config()
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
        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err))

    def auto_ifca(self):
        try:
            tipe = str(self.btnselect.get())
            db_config = read_db_config()
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
        self.trvTabel.tag_configure("ganjil", background="gainsboro")
        self.trvTabel.tag_configure("genap", background="floral white")                              

    def onMainExport(self):
        opsi = self.opsicari.get()
        cari = self.entCari.get()
        if opsi == "Tanggal":
                cari = self.checktgl(cari)
                sql = "SELECT * FROM logbook WHERE date_create LIKE %s"
                val = ("%{}%".format(cari),)
        elif opsi == "IFCA":
                sql = "SELECT * FROM logbook WHERE no_ifca LIKE %s"
                val = ("%{}%".format(cari),)
        elif opsi == "Unit":
                sql = "SELECT * FROM logbook WHERE unit LIKE %s"
                val = ("%{}%".format(cari),)
        elif opsi == "Work Req.":
                sql = "SELECT * FROM logbook WHERE work_req LIKE %s"
                val = ("%{}%".format(cari),)
                
        try:
            db_config = read_db_config()
            con = mysql.connector.connect(**db_config)
            cur = con.cursor()
            cur.execute(sql,val)
            results = cur.fetchall()
            if len(results) <= 0:
                    cur.close()
                    con.close()
                    return # stop aja karena kosong
        
            directory = filedialog.asksaveasfilename(initialdir = os.getcwd(), \
                initialfile = cari, \
                defaultextension='.csv', \
                title="Save file Export", \
                filetypes=[("Excel CSV", "*.csv"),("All", "*.*")])
            try:
                filename=open(directory,'w',newline='')
            except:
                print("export aborted by user")
                return 
            cWrite=csv.writer(filename)
            cWrite.writerow(["Index","No WO","No IFCA","Tanggal Buat","Unit",\
                    "Work Request","Staff","Work Action","Tanggal Selesai",\
                    "Jam Selesai","Diterima","Penerima","Tanggal Diterima",\
                    "Jam Buat","Status WO"])
            i=0
            for dat in results:
                cWrite.writerow(dat)
                i+=1
            cWrite.writerow(["Save to",directory,str(i),"record(s)"])
            filename.close()
            cur.close()
            con.close()
            messagebox.showinfo(title="Export File", \
                    message="Sudah tersimpan di: {}".format(directory))

        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err))

    def onReceived(self):
        cIfca = self.entIfca.get()
        if len(cIfca.strip()) == 0:
            messagebox.showwarning(title="Peringatan",message="No IFCA Kosong.")
            self.entIfca.focus_set()
        else:
            try:
                db_config = read_db_config()
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
                con.commit()
                cur.close()
                con.close()
            except mysql.connector.Error as err:
                messagebox.showerror(title="Error", \
                    message="SQL Log: {}".format(err))          

    def mainlog_detail(self, event):
        try:
            curItem = self.trvTabel.item(self.trvTabel.focus())
            ifca_value = curItem['values'][1]  
            self.entrySet("mainclear")
            db_config = read_db_config()
            con = mysql.connector.connect(**db_config)
            cur = con.cursor()
            # sql = "SELECT no_wo, no_ifca, date_create, unit, work_req, staff, date_done, time_done, work_act, time_create, status_ifca FROM logbook WHERE no_ifca = %s"
            sql = "SELECT * FROM logbook WHERE no_ifca = %s"
            cur.execute(sql,(ifca_value,))
            data = cur.fetchone()
            self.entIfca.insert(END, ifca_value)
            self.entWo.insert(END, data[1])
            #TGL buat
            self.entTglbuat.insert(END, data[3])
            getTgl = self.entTglbuat.get() #dari mysql YYYY-MM-DD
            #balikin menjadi DD-MM-YYYY
            showtgl = str(getTgl)[8:] +'-'+ str(getTgl)[5:7] +'-'+ str(getTgl)[:4]
            self.entTglbuat.delete(0, END)
            self.entTglbuat.insert(END, showtgl)
            # self.entJambuat.insert(END, data[13])
            self.entJambuat.insert(END, str(data[13])[:2]+str(data[13])[3:])
            self.entUnit.insert(END, data[4])
            self.entWorkReq.insert(END, data[5])
            self.entStaff.insert(END, data[6])
            #TGL done
            try: 
                    self.entTgldone.insert(END, data[8])
                    getTgldone = self.entTgldone.get() #dari mysql YYYY-MM-DD
                    #balikin menjadi DD-MM-YYYY
                    showtgldone = str(getTgldone)[8:] + '-' + str(getTgldone)[5:7] +'-' + str(getTgldone)[:4]
                    self.entTgldone.delete(0, END)
                    self.entTgldone.insert(END, showtgldone)
            except:
                    pass
            self.entJamdone.insert(END, data[9])
            self.entWorkAct.insert(END, data[7])
            try: self.entRecDate.insert(END, data[12])
            except: pass
            self.entRecBy.insert(END, data[11])
            if data[14] == "DONE":
                    self.opsiStatus.current(1)
                    # ngapain diUpdate lagi wo sudah DONE
                    self.btnUpdate.config(state="disable")
            elif data[14] == "CANCEL":
                    self.opsiStatus.current(2)
            elif data[14] == "PENDING":
                    self.opsiStatus.current(3)
                    self.btnReceived.config(state="disable") #tidak dapat receive karena wo belum done
                    self.btnUpdate.config(state="disable") #tidak dapat update karena wo sudah di list pending
            elif data[14] == "ONPROGRESS":
                    self.opsiStatus.current(0)
                    self.btnReceived.config(state="disable") #tidak dapat receive karena wo sedang on progress
                    self.btnUpdate.config(state="disable") #tidak dapat update karena wo sedang on progress
            else:
                    self.opsiStatus.current(0)
                    self.btnReceived.config(state="disable") #tidak dapat receive karena wo belum done
            if data[10] == True and ifca_value[:2] == "TN":
                    # tidak dapat receive wo TN karena sudah direceive
                    self.btnReceived.config(state="disable")
                    # ngapain diUpdate lagi wo TN sudah di CS
                    self.btnUpdate.config(state="disable")
            
            # read only setelah entry terisi
            self.entrySet("mainreadifca")
            cur.close()
            con.close()
        except:
            print('Tidak ada data di tabel')

    def onDelete(self):
        try:
            db_config = read_db_config()
            con = mysql.connector.connect(**db_config)
            cur = con.cursor()
            self.entWo.config(state="normal")
            cIfca = self.entIfca.get()
            sql = "DELETE FROM logbook WHERE no_ifca =%s"
            cur.execute(sql,(cIfca,))
            self.onClear()
            messagebox.showinfo(title="Informasi", \
                                message="Data sudah di hapus.")
            
            con.commit()
            cur.close()
            con.close()
        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err))

    def onClear(self):
        self.entrySet("mainclear")
        self.btnSave.config(state="normal")
        self.btnUpdate.config(state="disable")
        self.btnDelete.config(state="disable")
        self.btnReceived.config(state="disable")
        self.rbtnBM.config(state="normal")
        self.rbtnTN.config(state="normal")
        self.entRecBy.config(state="readonly")
        self.entRecDate.config(state="readonly")
        self.trvTabel.delete(*self.trvTabel.get_children())
        self.entCari.delete(0, END)
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
        try:
            db_config = read_db_config()
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
            elif len(cIfca.strip()) == 0:
                    messagebox.showwarning(title="Peringatan",message="No IFCA Kosong.")
                    self.entIfca.focus_set()
            elif self.checktgl(cTglBuat) == None: #check tgl jika kosong, batalkan save
                    messagebox.showerror(title="Error",message="Format tanggal salah")    
            elif len(cJamBuat.strip()) == 0:
                    messagebox.showwarning(title="Peringatan",message="Jam buat harus diisi.")
                    self.entJambuat.focus_set()
            elif len(cUnit.strip()) == 0:
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
                    cur.execute(sql,(cWo,cIfca.upper(),self.checktgl(cTglBuat),cJamBuat,cUnit.upper(),cWorkReq,cStaff.upper()))
                    messagebox.showinfo(title="Informasi", \
                                        message="Data sudah di tersimpan.")
                    con.commit()
                    cur.close()
                    con.close()
                    self.onClear()
        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err))

    def onUpdate(self):
        try:
            db_config = read_db_config()
            con = mysql.connector.connect(**db_config)
            cur = con.cursor()
            #panel kiri
            cWo = self.entWo.get()
            cIfca = self.entIfca.get()
            getTglBuat = self.checktgl(self.entTglbuat.get()) #check tgl dulu
            cWorkReq = self.entWorkReq.get('1.0', 'end')
            cStaff = self.entStaff.get()
            cStatus = self.opsiStatus.get()
            from datetime import datetime
            getTimeAcc = datetime.now()
            
            #panel kanan
            cWorkAct = self.entWorkAct.get('1.0', 'end')
            jamdone = self.entJamdone.get()
            getTglDone = self.checktgl(self.entTgldone.get()) #check tgl dulu
            #eksekusi sql
            # 2 update commit for pending
            if cStatus == "PENDING":
                    if len(cWorkAct.strip()) <= 0: 
                            messagebox.showwarning(title="Peringatan",message="Work Action harus diisi.")
                            self.entWorkAct.focus_set()
                            return # stop aja karena cWorkAct tidak diisi
                    elif len(cStaff.strip()) <= 0: 
                            messagebox.showwarning(title="Peringatan",message="Staff ENG harus diisi.")
                            self.entStaff.focus_set()
                            return # stop aja karena cStaff tidak diisi
                    else: ### jgn eksekusi sekarang mungkin?
                            sql1 = "INSERT INTO onprogress (no_ifca,date_update,commit_update,auth_by,auth_login)"+\
                            "VALUES(%s,%s,%s,%s,%s)"
                            cur.execute(sql1,(cIfca,getTimeAcc,cWorkAct,cStaff.upper(),""))
            # 2 #
            sql = "UPDATE logbook SET no_wo=%s,no_ifca=%s,date_create=%s,work_req=%s,staff=%s,status_ifca=%s,date_done=%s,time_done=%s,work_act=%s WHERE no_ifca =%s"
            cur.execute(sql,(cWo,cIfca,getTglBuat,cWorkReq,cStaff.upper(),cStatus,getTglDone,jamdone,cWorkAct,cIfca))
            messagebox.showinfo(title="Informasi", \
                    message="Data sudah di terupdate.")
            con.commit()
            cur.close()
            con.close()
            self.onSearch()
        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err))
