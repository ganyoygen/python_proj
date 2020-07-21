import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import mysql.connector
import datetime
import time



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
                
judul_kolom = ("No WO","No IFCA","Tanggal","UNIT","Work Request","Staff","Work Action","Tanggal Done","Jam Done","Received")
class Petugas:
        def __init__(self, parent):
                self.parent = parent
                self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
                lebar=950
                tinggi=700
                setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
                setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
                self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
                self.aturKomponen()
                self.auto()
                
        def keluar(self,event=None):
                self.parent.destroy()
                
        def OnDoubleClick(self, event):

                self.entWo.config(state="normal")
                self.entWo.delete(0, END)
                self.entIfca.delete(0, END)
                self.entHari.delete(0, END)
                self.entUnit.delete(0, END)
                self.entWorkReq.delete('1.0', 'end')
                self.entStaff.delete(0, END)
            
                it = self.trvTabel.selection()[0]
                ck = str(self.trvTabel.item(it,"values"))[2:8]
                    
                self.entWo.insert(END, ck)
                
                cKode = self.entWo.get()
                con = mysql.connector.connect(db="proj_pares", user="root", passwd="", host="192.168.10.5", port=3306,autocommit=True)
                cur = con.cursor()
                sql = "SELECT no_wo, no_ifca, date_creat, unit, work_req, staff FROM logbook WHERE no_wo = %s"
                cur.execute(sql,(cKode,))
                data = cur.fetchone()
                
        
                self.entIfca.insert(END, data[1])
                
                #TGL Lahir
                self.entHari.insert(END, data[2])
                cTglLahir = self.entHari.get()
                
                pecahTahun = str(cTglLahir[0]+cTglLahir[1]+cTglLahir[2]+cTglLahir[3])
                pecahBulan = str(cTglLahir[5]+cTglLahir[6])
                pecahHari = str(cTglLahir[8]+cTglLahir[9])
        
                self.entHari.delete(0, END)
                self.entBulan.delete(0, END)
                self.entTahun.delete(0, END)
                self.entHari.insert(END, pecahHari)
                self.entBulan.insert(END, pecahBulan)
                self.entTahun.insert(END, pecahTahun)
                
                self.entUnit.insert(END, data[3])
                self.entWorkReq.insert(END, data[4])
                self.entStaff.insert(END, data[5])
                self.entWo.config(state="disable")
                self.btnSave.config(state="disable")
                self.btnUpdate.config(state="normal")
                self.btnDelete.config(state="normal")
                
        def aturKomponen(self):
                frameWin = Frame(self.parent, bg="#666")
                frameWin.pack(fill=X,side=TOP)
                WindowDraggable(frameWin)
                Label(frameWin, text='PETUGAS',bg="#666",fg="white").pack(side=LEFT,padx=20)
                buttonx = Button(frameWin, text="X",fg="white", bg="#FA8072", width=6, height=2,bd=0,\
                                 activebackground="#FB8072",activeforeground="white", command=self.onClose, relief=FLAT)
                # Menghilangkan Frame windows
                # self.parent.overrideredirect(1) 
                # buttonx.pack(side=RIGHT)
                #
                mainFrame = Frame(self.parent)
                mainFrame.pack(side=TOP,fill=X)
                btnFrame = Frame(self.parent)
                btnFrame.pack(side=TOP, fill=X)
                tabelFrame = Frame(self.parent)
                tabelFrame.pack( expand=YES, side=TOP,fill=Y)
       
                Label(mainFrame, text='  ').grid(row=0, column=0)
                Label(btnFrame, text='  ').grid(row=1, column=0)

                Label(mainFrame, text='No WO').grid(row=1, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=1, column=1, sticky=W,pady=5,padx=10)
                self.entWo = Entry(mainFrame, width=20)
                self.entWo.grid(row=1, column=2,sticky=W)

                Label(mainFrame, text="No IFCA").grid(row=2, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=2, column=1, sticky=W,pady=5,padx=10)
                self.entIfca = Entry(mainFrame, width=20)
                self.entIfca.grid(row=2, column=2,sticky=W)

                Label(mainFrame, text="Tanggal").grid(row=3, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=3, column=1, sticky=W,pady=5,padx=10)

                #tgl
                tgl = Frame(mainFrame)
                tgl.grid(row=3,column=2,sticky=W)
                self.entHari = Entry(tgl, width=5)
                self.entHari.grid(row=1, column=0,sticky=W)
                self.entBulan = Entry(tgl, width=5)
                self.entBulan.grid(row=1, column=1,sticky=W,padx=2)
                self.entTahun = Entry(tgl, width=10)
                self.entTahun.grid(row=1, column=2,sticky=W,padx=2)
                Label(tgl, text='(dd/mm/yyyy)').grid(row=1, column=3, sticky=E,padx=5)
                
                Label(mainFrame, text="Unit").grid(row=4, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=4, column=1, sticky=W,pady=5,padx=10)             
                self.entUnit = Entry(mainFrame, width=20)
                self.entUnit.grid(row=4, column=2,sticky=W)

                Label(mainFrame, text="Work Request").grid(row=5, column=0, sticky=NW,padx=20)
                Label(mainFrame, text=':').grid(row=5, column=1, sticky=NW,padx=10,pady=6)
                self.entWorkReq = ScrolledText(mainFrame,height=4,width=35)
                self.entWorkReq.grid(row=5, column=2,sticky=W)

                Label(mainFrame, text="Staff").grid(row=6, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=6, column=1, sticky=W,pady=5,padx=10)
                self.entStaff = Entry(mainFrame, width=20)
                self.entStaff.grid(row=6, column=2,sticky=W)


                self.btnSave = Button(btnFrame, text='Save',\
                                        command=self.onSave, width=10,\
                                        relief=FLAT, bd=2, bg="#666", fg="white",activebackground="#444",activeforeground="white" )
                self.btnSave.grid(row=0, column=1,padx=5)

                self.btnUpdate = Button(btnFrame, text='Update',\
                                        command=self.onUpdate,state="disable", width=10,\
                                        relief=FLAT, bd=2, bg="#666", fg="white",activebackground="#444",activeforeground="white")
                self.btnUpdate.grid(row=0,column=2,pady=10, padx=5)
                
                self.btnClear = Button(btnFrame, text='Clear',\
                                        command=self.onClear, width=10,\
                                       relief=FLAT, bd=2, bg="#666", fg="white",activebackground="#444",activeforeground="white")
                self.btnClear.grid(row=0,column=3,pady=10, padx=5)

                self.btnDelete = Button(btnFrame, text='Delete',\
                                        command=self.onDelete,state="disable", width=10,\
                                        relief=FLAT, bd=2, bg="#FC6042", fg="white",activebackground="#444",activeforeground="white")
                self.btnDelete.grid(row=0,column=4,pady=10, padx=5)


                self.fr_data = Frame(tabelFrame, bd=10)
                self.fr_data.pack(fill=BOTH, expand=YES)
                self.trvTabel = ttk.Treeview(self.fr_data, columns=judul_kolom,show='headings')
                self.trvTabel.bind("<Double-1>", self.OnDoubleClick)
                sbVer = Scrollbar(self.fr_data, orient='vertical',command=self.trvTabel.yview)
                sbVer.pack(side=RIGHT, fill=Y)
                sbVer = Scrollbar(self.fr_data, orient='horizontal',command=self.trvTabel.xview)
                sbVer.pack(side=BOTTOM, fill=X)

                self.trvTabel.pack(side=TOP, fill=BOTH)
                self.trvTabel.configure(yscrollcommand=sbVer.set)
                self.trvTabel.configure(xscrollcommand=sbVer.set)
                self.table()
                
        def table(self):

        
                con = mysql.connector.connect(db="proj_pares", user="root", passwd="", host="192.168.10.5", port=3306,autocommit=True)
                cur = con.cursor()
                cur.execute("SELECT * FROM logbook")
                data_table = cur.fetchall()

                for kolom in judul_kolom:
                    self.trvTabel.heading(kolom,text=kolom)

                self.trvTabel.column("No WO", width=80,anchor="w")
                self.trvTabel.column("No IFCA", width=80,anchor="w")
                self.trvTabel.column("Tanggal", width=80,anchor="w")
                self.trvTabel.column("UNIT", width=80,anchor="w")
                self.trvTabel.column("Work Request", width=120,anchor="w")
                self.trvTabel.column("Staff", width=80,anchor="w")
                self.trvTabel.column("Work Action", width=120,anchor="w")
                self.trvTabel.column("Tanggal Done", width=80,anchor="w")
                self.trvTabel.column("Jam Done", width=40,anchor="w")
                self.trvTabel.column("Received", width=40,anchor="w")
            

                i=0
                for dat in data_table:
                    if(i%2):
                        baris="genap"
                    else:
                        baris="ganjil"
                    self.trvTabel.insert('', 'end', values=dat, tags=baris)
                    i+=1

                self.trvTabel.tag_configure("ganjil", background="#FFFFFF")
                self.trvTabel.tag_configure("genap", background="whitesmoke")
                cur.close()
                con.close()                              

        def auto(self):
                con = mysql.connector.connect(db='proj_pares', user='root', passwd='', host='192.168.10.5', port=3306,autocommit=True)
                cur = con.cursor()
                cuv = con.cursor()
                sqlkode = "SELECT max(no_wo) FROM logbook"
                sql = "SELECT no_wo FROM logbook"
                cur.execute(sqlkode)
                # cuv.execute(sql)
                maxkode = cur.fetchone()
                
                if cur.rowcount > 0:      
                    autohit = int(maxkode[0])+1
                    hits = "00000"+str(autohit)
                    if len(hits) == 6:
                        self.entWo.insert(0, hits)
                        self.entIfca.focus_set()
                    elif len(hits) == 7:
                        hit = "0000"+str(autohit)
                        self.entWo.insert(0, hit)
                        self.entIfca.focus_set()
                    elif len(hits) == 8:
                        hit = "000"+str(autohit)
                        self.entWo.insert(0, hit)
                        self.entIfca.focus_set()
                    elif len(hits) == 9:
                        hit = "00"+str(autohit)
                        self.entWo.insert(0, hit)
                        self.entIfca.focus_set()
                    elif len(hits) == 10:
                        hit = "0"+str(autohit)
                        self.entWo.insert(0, hit)
                        self.entIfca.focus_set()
                    elif len(hits) == 11:
                        hit = ""+str(autohit)
                        self.entWo.insert(0, hit)
                        self.entIfca.focus_set()
                    
                    else:
                        messagebox.showwarning(title="Peringatan", \
                                    message="maaf lebar data hanya sampai 6 digit")
                        
                else:
                    hit = "000001"
                    self.entWo.insert(0, hit)
                    self.entIfca.focus_set()
                    
                self.entWo.config(state="readonly")
        
        def onClose(self, event=None):
                self.parent.destroy()

        def onDelete(self):
                con = mysql.connector.connect(db='proj_pares', user='root', passwd='', host='192.168.10.5', port=3306,autocommit=True)
                cur = con.cursor()
                self.entWo.config(state="normal")
                cKode = self.entWo.get()
                sql = "DELETE FROM logbook WHERE no_wo =%s"
                cur.execute(sql,(cKode,))
                self.onClear()
                messagebox.showinfo(title="Informasi", \
                                    message="Data sudah di hapus.")
                
                cur.close()
                con.close()

        def onClear(self):
                self.btnSave.config(state="normal")
                self.btnUpdate.config(state="disable")
                self.btnDelete.config(state="disable")
                self.entWo.config(state="normal")
                self.entWo.delete(0, END)
                self.entIfca.delete(0, END)
                self.entHari.delete(0, END)
                self.entBulan.delete(0, END)
                self.entTahun.delete(0, END)
                self.entUnit.delete(0, END)
                self.entWorkReq.delete('1.0', 'end')
                self.entStaff.delete(0, END)
                self.trvTabel.delete(*self.trvTabel.get_children())
                self.fr_data.after(0, self.table())
        
                self.auto()
                self.entWo.focus_set()
                        
        def onSave(self):
        
                con = mysql.connector.connect(db='proj_pares', user='root', passwd='', host='192.168.10.5', port=3306,autocommit=True)
 
                cKode = self.entWo.get()
                cIfca = self.entIfca.get()

                ####
                cHari = self.entHari.get()
                cBulan = self.entBulan.get()
                cTahun = self.entTahun.get()
                dCreate = datetime.date(int(cTahun),int(cBulan),int(cHari))
                cUnit = self.entUnit.get()
                cWorkReq = self.entWorkReq.get('1.0', 'end')
                cStaff = self.entStaff.get()
                if len(cHari) == 0 and len(cBulan) == 0 and len(cTahun):
                        messagebox.showwarning(title="Peringatan",message="Tanggal Tidak boleh kosong")    
                else:
                        
                        cur = con.cursor()
                        sql = "INSERT INTO logbook (no_wo, no_ifca, date_creat, unit, work_req, staff)"+\
                              "VALUES(%s,%s,%s,%s,%s,%s)"
                        cur.execute(sql,(cKode,cIfca,dCreate,cUnit,cWorkReq,cStaff))
                        self.onClear()
                        messagebox.showinfo(title="Informasi", \
                                            message="Data sudah di tersimpan.")
                        
                        cur.close()
                        con.close()
                
        def onUpdate(self):
                cKode = self.entWo.get()
                
                if len(cKode) == 0:
                        messagebox.showwarning(title="Peringatan",message="Kode kosong.")
                        self.entWo.focus_set()

                else:
                        con = mysql.connector.connect(db='proj_pares', user='root', passwd='', host="192.168.10.5",\
                                      port=3306, autocommit=True)
                        cur = con.cursor()
                        cKode = self.entWo.get()
                        cIfca = self.entIfca.get()

                        ####
                        cHari = self.entHari.get()
                        cBulan = self.entBulan.get()
                        cTahun = self.entTahun.get()
                        dLahir = datetime.date(int(cTahun),int(cBulan),int(cHari))
                        cWorkReq = self.entWorkReq.get('1.0', 'end')
                        cStaff = self.entStaff.get()
                        
                        sql = "UPDATE logbook SET no_ifca=%s, date_creat=%s, work_req=%s,staff=%s WHERE no_wo =%s"
                        cur.execute(sql,(cIfca,dLahir,cWorkReq,cStaff,cKode))
                        self.onClear()
                        messagebox.showinfo(title="Informasi", \
                                    message="Data sudah di terupdate.")

                        cur.close()
                        con.close()   
                     

def main():
    Petugas(root)
    root.mainloop()
main()
                                                           
                                                                                           
