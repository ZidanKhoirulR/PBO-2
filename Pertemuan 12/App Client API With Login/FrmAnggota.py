import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import *
class FrmAnggota:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_ANGGOTA:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_ANGGOTA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JENIS_KELAMIN:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PRODI:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NO_TLP:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtkode_anggota = Entry(mainFrame) 
        self.txtkode_anggota.grid(row=0, column=1, padx=5, pady=5)
        self.txtkode_anggota.bind('<Return>', self.onCari)
        # Textbox
        self.txtNama_anggota = Entry(mainFrame) 
        self.txtNama_anggota.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJenis_kelamin = StringVar()
        Cbo_jenis_kelamin = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJenis_kelamin) 
        Cbo_jenis_kelamin.grid(row=2, column=1, padx=5, pady=5)
        # Adding jenis_kelamin combobox drop down list
        Cbo_jenis_kelamin['values'] = ('P','L')
        Cbo_jenis_kelamin.current()
        # Textbox
        self.txtProdi = Entry(mainFrame) 
        self.txtProdi.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtNo_tlp = Entry(mainFrame) 
        self.txtNo_tlp.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_anggota','kode_anggota','nama_anggota','jenis_kelamin','prodi','no_tlp','alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_anggota', text='ID_ANGGOTA')
        self.tree.column('id_anggota', width="30")
        self.tree.heading('kode_anggota', text='KODE_ANGGOTA')
        self.tree.column('kode_anggota', width="30")
        self.tree.heading('nama_anggota', text='NAMA_ANGGOTA')
        self.tree.column('nama_anggota', width="30")
        self.tree.heading('jenis_kelamin', text='JENIS_KELAMIN')
        self.tree.column('jenis_kelamin', width="30")
        self.tree.heading('prodi', text='PRODI')
        self.tree.column('prodi', width="30")
        self.tree.heading('no_tlp', text='NO_TLP')
        self.tree.column('no_tlp', width="30")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtkode_anggota.delete(0,END)
        self.txtkode_anggota.insert(END,"")
        self.txtNama_anggota.delete(0,END)
        self.txtNama_anggota.insert(END,"")
        self.txtJenis_kelamin.set("")
        self.txtProdi.delete(0,END)
        self.txtProdi.insert(END,"")
        self.txtNo_tlp.delete(0,END)
        self.txtNo_tlp.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_anggota"],d["kode_anggota"],d["nama_anggota"],d["jenis_kelamin"],d["prodi"],d["no_tlp"],d["alamat"]))
    def onCari(self, event=None):
        kode_anggota = self.txtkode_anggota.get()
        obj = Anggota()
        a = obj.get_by_kode_anggota(kode_anggota)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_anggota = self.txtkode_anggota.get()
        obj = Anggota()
        res = obj.get_by_kode_anggota(kode_anggota)
        self.txtkode_anggota.delete(0,END)
        self.txtkode_anggota.insert(END,obj.kode_anggota)
        self.txtNama_anggota.delete(0,END)
        self.txtNama_anggota.insert(END,obj.nama_anggota)
        self.txtJenis_kelamin.set(obj.jenis_kelamin)
        self.txtProdi.delete(0,END)
        self.txtProdi.insert(END,obj.prodi)
        self.txtNo_tlp.delete(0,END)
        self.txtNo_tlp.insert(END,obj.no_tlp)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_anggota = self.txtkode_anggota.get()
        nama_anggota = self.txtNama_anggota.get()
        jenis_kelamin = self.txtJenis_kelamin.get()
        prodi = self.txtProdi.get()
        no_tlp = self.txtNo_tlp.get()
        alamat = self.txtAlamat.get()
        # create new Object
        obj = Anggota()
        obj.kode_anggota = kode_anggota
        obj.nama_anggota = nama_anggota
        obj.jenis_kelamin = jenis_kelamin
        obj.prodi = prodi
        obj.no_tlp = no_tlp
        obj.alamat = alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_anggota(kode_anggota)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_anggota = self.txtkode_anggota.get()
        obj = Anggota()
        obj.kode_anggota = kode_anggota
        if(self.ditemukan==True):
            res = obj.delete_by_kode_anggota(kode_anggota)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()
