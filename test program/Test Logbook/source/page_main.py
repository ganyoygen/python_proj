import tkinter as tk
import mysql.connector
import os
import csv # untuk write ke Excel
import time
import datetime

from mysqlcon import read_db_config
from popup_date import PopupDateTime # popup set tgl jam
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText

judul_kolom = ("WO","IFCA","Tanggal","UNIT","Work Request","Staff","Work Action","Tanggal Done","Jam Done","Received")

class PageMain(tk.Frame):
    def __init__(self,parent,dept):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.dept = dept
        imgdateset = tk.PhotoImage(file = str(os.getcwd()+"\\"+"icon-icons.com_date.png"))
        self.imgdateget = imgdateset.subsample(2, 2) # Resizing image by.subsample to fit on button
        self.btnselect = StringVar(parent,value="TN")

        self.komponenMain()
        self.komponenAtas()
        self.komponenTengah()
        self.komponenBawah()

    def komponenMain(self):
        self.topFrame = ttk.Frame(self)
        self.topFrame.pack(side=TOP,fill=X)
        self.midFrame = ttk.Frame(self)
        self.midFrame.pack(side=TOP, fill=X)
        self.botFrame = ttk.Frame(self)
        self.botFrame.pack(side=TOP, fill=X)
        footer = ttk.Frame(self)
        footer.pack(side=TOP, fill=X)
        
        ttk.Label(self.topFrame, text='').grid(row=0, column=0)
        ttk.Label(self.midFrame, text='').grid(row=0, column=0)
        ttk.Label(self.botFrame, text='').grid(row=0, column=0)
        ttk.Label(footer, text='').grid(row=0, column=0)

    def komponenAtas(self):
        #samping kiri
        topleft = ttk.Frame(self.topFrame)
        topleft.grid(row=1,column=1,sticky=W)
        ttk.Label(topleft, text='No WO').grid(row=0, column=0, sticky=W,padx=20)
        ttk.Label(topleft, text=':').grid(row=0, column=1, sticky=W,pady=5,padx=10)
        self.entWo = ttk.Entry(topleft, width=20)
        self.entWo.grid(row=0, column=2,sticky=W)

        ttk.Label(topleft, text="IFCA").grid(row=1, column=0, sticky=W,padx=20)
        ttk.Label(topleft, text=':').grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.entIfca = ttk.Entry(topleft, width=15)
        self.entIfca.grid(row=1, column=2,sticky=W)
        radiobtn = ttk.Frame(topleft)
        radiobtn.grid(row=1,column=2)

        self.rbtnTN = ttk.Radiobutton(radiobtn, text="TN", variable=self.btnselect, value="TN", command=self.auto_ifca)
        self.rbtnTN.grid(row=0, column=0,sticky=W)
        self.rbtnBM = ttk.Radiobutton(radiobtn, text="BM", variable=self.btnselect, value="BM", command=self.auto_ifca)
        ttk.Label(radiobtn, text="  /  ").grid(row=0,column=1,sticky=E)
        self.rbtnBM.grid(row=0, column=2,sticky=W)

        #tglbuat
        ttk.Label(topleft, text="Tanggal - Jam").grid(row=2, column=0, sticky=W,padx=20)
        ttk.Label(topleft, text=':').grid(row=2, column=1, sticky=W,pady=5,padx=10)
        tglbuat = ttk.Frame(topleft)
        tglbuat.grid(row=2,column=2,sticky=W)
        self.entTglbuat = ttk.Entry(tglbuat, width=10)
        self.entTglbuat.grid(row=1, column=0,sticky=W)
        self.entJambuat = ttk.Entry(tglbuat,width=7)
        self.entJambuat.grid(row=1, column=1,sticky=W)
        self.btnDateCreate = Button(tglbuat,image=self.imgdateget,command=self.onDateCreate)
        self.btnDateCreate.grid(row=1, column=2,pady=10,padx=5)

        ttk.Label(topleft, text="Unit").grid(row=3, column=0, sticky=W,padx=20)
        ttk.Label(topleft, text=':').grid(row=3, column=1, sticky=W,pady=5,padx=10)             
        self.entUnit = ttk.Entry(topleft, width=15)
        self.entUnit.grid(row=3, column=2,sticky=W)

        ttk.Label(topleft, text="Work Request").grid(row=4, column=0, sticky=NW,padx=20)
        ttk.Label(topleft, text=':').grid(row=4, column=1, sticky=NW,padx=10,pady=6)
        self.entWorkReq = ScrolledText(topleft,height=4,width=35)
        self.entWorkReq.grid(row=4, column=2,sticky=W)

        ttk.Label(topleft, text="Staff").grid(row=5, column=0, sticky=W,padx=20)
        ttk.Label(topleft, text=':').grid(row=5, column=1, sticky=W,pady=5,padx=10)
        self.entStaff = ttk.Entry(topleft, width=20)
        self.entStaff.grid(row=5, column=2,sticky=W)

        #samping kanan
        topright = ttk.Frame(self.topFrame)
        topright.grid(row=1,column=2,sticky=W)
        ttk.Label(topright, text="").grid(row=0, column=0, sticky=W,pady=5,padx=20)
        ttk.Label(topright, text="").grid(row=1, column=0, sticky=W,pady=5,padx=20)
        ttk.Label(topright, text="Status").grid(row=2, column=0, sticky=W,pady=5,padx=20)
        ttk.Label(topright, text=':').grid(row=2, column=1, sticky=W,pady=5,padx=10)

        self.opsiStatus = ttk.Combobox(topright, \
            values = ["","DONE","CANCEL","PENDING"],\
            state="readonly", width=10)
        self.opsiStatus.current(0)
        self.opsiStatus.grid(row=2, column=2,sticky=W)

        ttk.Label(topright, text="Tanggal - Jam").grid(row=3, column=0, sticky=W,padx=20)
        ttk.Label(topright, text=':').grid(row=3, column=1, sticky=W,pady=5,padx=10)             
        tgldone = ttk.Frame(topright)
        tgldone.grid(row=3,column=2,sticky=W)
        self.entTgldone = ttk.Entry(tgldone, width=10)
        self.entTgldone.grid(row=0, column=0,sticky=W)
        self.entJamdone = ttk.Entry(tgldone, width=7)
        self.entJamdone.grid(row=0, column=1,sticky=W)
        self.btnDateDone = Button(tgldone,image=self.imgdateget,command=self.onDateDone)
        self.btnDateDone.grid(row=0, column=2,pady=10,padx=5)

        ttk.Label(topright, text="Work Action").grid(row=4, column=0, sticky=NW,padx=20)
        ttk.Label(topright, text=':').grid(row=4, column=1, sticky=NW,padx=10,pady=6)
        self.entWorkAct = ScrolledText(topright,height=4,width=35)
        self.entWorkAct.grid(row=4, column=2,sticky=W)
                
        ttk.Label(topright, text="Received").grid(row=5, column=0, sticky=W,padx=20)
        ttk.Label(topright, text=':').grid(row=5, column=1, sticky=W,pady=5,padx=10)
        recentry = ttk.Frame(topright)
        recentry.grid(row=5,column=2,sticky=W)
        self.entRecDate = ttk.Entry(recentry, width=20)
        self.entRecDate.grid(row=0, column=0,sticky=W)
        self.entRecBy = ttk.Entry(recentry, width=25)
        self.entRecBy.grid(row=0, column=1,sticky=W)

    def komponenTengah(self):
        #panel button
        self.btnClear = Button(self.midFrame, text='New',\
            command=self.onClear, width=10,\
            relief=RAISED, bd=2, bg="#666", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnClear.grid(row=1, column=1,pady=10,padx=5)

        self.btnSave = Button(self.midFrame, text='Save',\
            command=self.onSave, width=10,\
            relief=RAISED, bd=2, bg="#666", fg="white",\
            activebackground="#444",activeforeground="white" )
        self.btnSave.grid(row=1,column=2,pady=10,padx=5)

        self.btnUpdate = Button(self.midFrame, text='Update',\
            command=self.onUpdate,state="disable", width=10,\
            relief=RAISED, bd=2, bg="#666", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnUpdate.grid(row=1,column=3,pady=10,padx=5)

        self.btnDelete = Button(self.midFrame, text='Delete',\
            command=self.onDelete,state="disable", width=10,\
            relief=RAISED, bd=2, bg="#FC6042", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnDelete.grid(row=1,column=4,pady=10,padx=5)

        self.btnReceived = Button(self.midFrame, text='Received',\
            command=self.onReceived,state="disable", width=10,\
            relief=RAISED, bd=2, bg="#667", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnReceived.grid(row=1,column=5,pady=10,padx=5)

        # Label(self.midFrame, text="Search :").grid(row=1, column=1, sticky=E,padx=20)
        self.opsicari = ttk.Combobox(self.midFrame, \
            values = ["IFCA","Tanggal", "Unit", "Work Req."], \
            state="readonly", width=10)
        self.opsicari.current(1)
        self.opsicari.grid(row=2, column=1,sticky=W)

        self.entCari = ttk.Entry(self.midFrame, width=20)
        self.entCari.grid(row=2, column=2,sticky=W)
        # self.entCari.bind('<KeyRelease>',self.onSearch) #cari saat input apapun
        
        self.btnSearch = Button(self.midFrame, text='Search',\
            command=self.onSearch,\
            state="normal", width=10,\
            relief=RAISED, bd=2, bg="#667", fg="white",\
            activebackground="#444",activeforeground="white")
        self.btnSearch.grid(row=2,column=3,pady=10,padx=5)

        self.btnMainExp = Button(self.midFrame, text='Export',\
            command=self.onMainExport,\
            state="normal", width=10,\
            relief=RAISED, bd=2, \
            bg="#558", fg="white", \
            activebackground="#444",activeforeground="white")
        self.btnMainExp.grid(row=2,column=4,pady=10,padx=5)

    def komponenBawah(self):
        #tabel
        listifca = ttk.Frame(self.botFrame)
        listifca.grid(row=1,column=1)
        self.tabelIfca = ttk.Treeview(listifca, columns=judul_kolom,show='headings')
        self.tabelIfca.bind("<Double-1>", self.mainlog_detail)
        sbVer = ttk.Scrollbar(listifca, orient='vertical',command=self.tabelIfca.yview)
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor = ttk.Scrollbar(listifca, orient='horizontal',command=self.tabelIfca.xview)
        sbHor.pack(side=BOTTOM, fill=X)

        self.tabelIfca.pack(side=TOP, fill=BOTH)
        self.tabelIfca.configure(yscrollcommand=sbVer.set)
        self.tabelIfca.configure(xscrollcommand=sbHor.set)

        self.onClear()

    def entrySet(self,opsi):
        # 1 on doubleclick main entry, normal
        if opsi == "mainclear":
            self.entWo.config(state="normal")
            self.entIfca.config(state="normal")
            self.entTglbuat.config(state="normal")
            self.entJambuat.config(state="normal")
            self.entUnit.config(state="normal")
            self.entTgldone.config(state="normal")
            self.entJamdone.config(state="normal")
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
            self.entRecBy.config(state="normal")
            self.entRecDate.config(state="normal")
            self.btnDelete.config(state="disable")
            self.btnReceived.config(state="disable")

            # A. readonly aja, input pake popup
            self.entTglbuat.config(state="readonly")
            self.entJambuat.config(state="readonly")
            self.entTgldone.config(state="readonly")
            self.entJamdone.config(state="readonly")
            # A #
        # mainentry readonly panel kiri kecuali work req dan staff
        elif opsi == "disablebtn":
            self.btnDateCreate.config(state="disable")
            self.btnDateDone.config(state="disable")
            self.btnSave.config(state="disable")
            self.btnUpdate.config(state="disable")
            self.rbtnBM.config(state="disable")
            self.rbtnTN.config(state="disable")
        elif opsi == "mainreadifca":
            self.entWo.config(state="readonly")
            self.entIfca.config(state="readonly")
            self.entTglbuat.config(state="readonly")
            self.entJambuat.config(state="readonly")
            self.entUnit.config(state="readonly")
            self.entTgldone.config(state="readonly")
            self.entJamdone.config(state="readonly")
            self.entRecBy.config(state="readonly")
            self.entRecDate.config(state="readonly")
        # 1 #
        else : pass

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
        self.entrySet("mainclear")
        self.opsiStatus.current(0)
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
            try: # prevent error, ketika IFCA terakhir tanpa no. WO (blank)
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
            except: pass
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
        self.tabelIfca.delete(*self.tabelIfca.get_children()) #refresh, hapus dulu tabel lama
        for kolom in judul_kolom:
            self.tabelIfca.heading(kolom,text=kolom)
        # self.tabelIfca.column("No", width=10,anchor="w")
        self.tabelIfca.column("WO", width=50,anchor="w")
        self.tabelIfca.column("IFCA", width=80,anchor="w")
        self.tabelIfca.column("Tanggal", width=80,anchor="w")
        self.tabelIfca.column("UNIT", width=80,anchor="w")
        self.tabelIfca.column("Work Request", width=150,anchor="w")
        self.tabelIfca.column("Staff", width=70,anchor="w")
        self.tabelIfca.column("Work Action", width=150,anchor="w")
        self.tabelIfca.column("Tanggal Done", width=80,anchor="w")
        self.tabelIfca.column("Jam Done", width=40,anchor="w")
        self.tabelIfca.column("Received", width=40,anchor="w")
    
        i=0
        for dat in data: 
            if(i%2):
                baris="genap"
            else:
                baris="ganjil"
            #hilangkan nomor mulai dari kolom wo dat[1:]
            self.tabelIfca.insert('', 'end', values=dat[1:], tags=baris)
            i+=1
        self.tabelIfca.tag_configure("ganjil", background="gainsboro")
        self.tabelIfca.tag_configure("genap", background="floral white")                              

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
                cur.close()
                con.close()
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
            curItem = self.tabelIfca.item(self.tabelIfca.focus())
            ifca_value = curItem['values'][1]  
            self.entrySet("mainclear")
            self.entrySet("disablebtn")
            if self.dept == "ROOT": self.btnDelete.config(state="normal")
            self.entTglbuat.config(state="normal")
            self.entJambuat.config(state="normal")
            self.entTgldone.config(state="normal")
            self.entJamdone.config(state="normal")
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
            self.entJambuat.insert(END, data[13])
            # self.entJambuat.insert(END, str(data[13])[:2]+str(data[13])[3:])
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
            except: pass
            self.entJamdone.insert(END, data[9])
            self.entWorkAct.insert(END, data[7])
            try: 
                showdate = str(data[12])[8:10] + '-' + str(data[12])[5:7] +'-' + str(data[12])[:4]+' '+str(data[12])[11:]
                self.entRecDate.insert(END, showdate)
            except: pass
            self.entRecBy.insert(END, data[11])
            if data[14] == "DONE":
                self.opsiStatus.current(1)
                self.btnReceived.config(state="normal")
                # ngapain diUpdate lagi wo sudah DONE
            elif data[14] == "CANCEL": 
                self.opsiStatus.current(2)
                self.btnReceived.config(state="normal")
            elif data[14] == "PENDING":
                self.opsiStatus.current(3)
            elif data[14] == "ONPROGRESS" or data[14] == "RETURNEDCS" or data[14] == "TAKENBYENG":
                self.opsiStatus.current(0)
            else:
                self.btnUpdate.config(state="normal")
                self.btnDateDone.config(state="normal")
                self.opsiStatus.current(0)
            if data[10] == True and ifca_value[:2] == "TN":
                # tidak dapat receive wo TN karena sudah direceive
                self.btnReceived.config(state="disable")
            
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
            if messagebox.askokcancel('Delete Data','WO dengan no {} akan dihapus?'.format(cIfca)) == True:
                sqlmain = "DELETE FROM logbook WHERE no_ifca =%s"
                cur.execute(sqlmain,(cIfca,))
                sqlprog = "DELETE FROM onprogress WHERE no_ifca =%s"
                cur.execute(sqlprog,(cIfca,))
                self.onSearch() #update received sesuai tabel yg dicari
                messagebox.showinfo(title="Delete {}".format(cIfca), \
                                    message="Data sudah di hapus.")
            else: pass
            con.commit()
            cur.close()
            con.close()
        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err))

    def onClear(self):
        self.entrySet("mainclear")
        self.entrySet("disablebtn")
        self.btnDateCreate.config(state="normal")
        self.btnDateDone.config(state="normal")
        self.btnSave.config(state="normal")
        self.rbtnBM.config(state="normal")
        self.rbtnTN.config(state="normal")
        self.tabelIfca.delete(*self.tabelIfca.get_children())
        self.entCari.delete(0, END)
        self.opsiStatus.current(0)
        # list wo hari ini
        self.opsicari.current(1)
        from datetime import date
        today = date.today()
        self.entCari.insert(END,today.strftime("%d-%m-%Y"))
        self.onSearch()
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
                    self.entIfca.delete(0, END)
            elif self.checktgl(cTglBuat) == None or len(cJamBuat.strip()) == 0: #check tgl jika kosong, batalkan save
                    messagebox.showerror(title="Error",message="Format tanggal salah")
            elif len(cUnit.strip()) == 0:
                    messagebox.showwarning(title="Peringatan",message="Unit harus diisi.")
                    self.entUnit.focus_set()
                    self.entUnit.delete(0, END)
            elif self.checkifca(cIfca) == "tolak": #check IFCA
                    messagebox.showerror(title="Error", \
                    message="{} sudah terdaftar.".format(cIfca))
                    self.entIfca.focus_set()
            else:
                    cur = con.cursor()
                    sql = "INSERT INTO logbook (no_wo, no_ifca, date_create, time_create, unit, work_req, staff)"+\
                          "VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(sql,(cWo,cIfca.upper(),self.checktgl(cTglBuat),cJamBuat,cUnit.upper(),cWorkReq.strip(),cStaff.upper()))
                    messagebox.showinfo(title="Informasi", \
                                        message="Data sudah di tersimpan.")
                    cur.close()
                    self.onClear()
            con.commit()
            con.close()
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
            if cStatus == "DONE":
                if len(cStaff.strip()) <= 0: 
                    messagebox.showwarning(title="Peringatan",message="Staff ENG harus diisi.")
                    self.entStaff.focus_set()
                    self.entStaff.delete(0, END)
                    return # stop aja karena cStaff tidak diisi
                elif len(cWorkAct.strip()) <= 0:
                    messagebox.showwarning(title="Peringatan",message="Work Action harus diisi.")
                    self.entWorkAct.focus_set()
                    self.entWorkAct.delete('1.0', 'end')
                    return # stop aja karena cWorkAct tidak diisi
                elif getTglDone == None or len(jamdone.strip()) == 0:
                    messagebox.showwarning(title="Peringatan",message="Tanggal harus diisi.")
                    return # stop aja karena tanggal tidak diisi
                else : pass
            elif cStatus == "PENDING":
                getTglDone = None
                jamdone = None
                if len(cStaff.strip()) <= 0: 
                    messagebox.showwarning(title="Peringatan",message="Staff ENG harus diisi.")
                    self.entStaff.focus_set()
                    self.entStaff.delete(0, END)
                    return # stop aja karena cStaff tidak diisi
                elif len(cWorkAct.strip()) <= 0: 
                    messagebox.showwarning(title="Peringatan",message="Work Action harus diisi.")
                    self.entWorkAct.focus_set()
                    self.entWorkAct.delete('1.0', 'end')
                    return # stop aja karena cWorkAct tidak diisi
                else: ### jgn eksekusi sekarang mungkin?
                    sql1 = "INSERT INTO onprogress (no_ifca,date_update,commit_update,auth_by,auth_login)"+\
                    "VALUES(%s,%s,%s,%s,%s)"
                    cur.execute(sql1,(cIfca,getTimeAcc,cWorkAct.strip(),cStaff.upper(),""))
            # 2 #
            elif cStatus == "CANCEL":
                if len(cWorkAct.strip()) <= 0: 
                    messagebox.showwarning(title="Peringatan",message="Work Action harus diisi.")
                    self.entWorkAct.focus_set()
                    self.entWorkAct.delete('1.0', 'end')
                    return # stop aja karena cWorkAct tidak diisi
            else : # UPDATE / CANCEL tidak perlu tanggal
                getTglDone = None
                jamdone = None
            sql = "UPDATE logbook SET no_wo=%s,no_ifca=%s,date_create=%s,work_req=%s,staff=%s,status_ifca=%s,date_done=%s,time_done=%s,work_act=%s WHERE no_ifca =%s"
            cur.execute(sql,(cWo,cIfca,getTglBuat,cWorkReq.strip(),cStaff.upper(),cStatus,getTglDone,jamdone,cWorkAct.strip(),cIfca))
            messagebox.showinfo(title="Informasi", \
                    message="Data sudah di terupdate.")
            con.commit()
            cur.close()
            con.close()
            self.onSearch()
        except mysql.connector.Error as err:
            messagebox.showerror(title="Error", \
                message="SQL Log: {}".format(err))

    def onDateCreate(self):
        setdate = PopupDateTime(self.parent)
        setdate.parent.wait_window(setdate.top)
        if len(setdate.value.strip()) > 0: 
            # output <tanggal> <jam>, lanjutkan perintah
            getdate, gettime = setdate.value.split() #pisah tanggal dan jam
            self.entTglbuat.config(state="normal")
            self.entJambuat.config(state="normal")
            self.entTglbuat.delete(0, END)
            self.entJambuat.delete(0, END)
            self.entTglbuat.insert(END, getdate)
            self.entJambuat.insert(END, gettime)
            self.entTglbuat.config(state="readonly")
            self.entJambuat.config(state="readonly")
            self.entUnit.focus_set()
        else: 
            # output kosong, batalkan perintah
            pass

    def onDateDone(self):
        setdate = PopupDateTime(self.parent)
        setdate.parent.wait_window(setdate.top)
        if len(setdate.value.strip()) > 0: 
            # output <tanggal> <jam>, lanjutkan perintah
            getdate, gettime = setdate.value.split() #pisah tanggal dan jam
            self.entTgldone.config(state="normal")
            self.entJamdone.config(state="normal")
            self.entTgldone.delete(0, END)
            self.entJamdone.delete(0, END)
            self.entTgldone.insert(END, getdate)
            self.entJamdone.insert(END, gettime)
            self.entTgldone.config(state="readonly")
            self.entJamdone.config(state="readonly")
        else: 
            # output kosong, batalkan perintah
            pass