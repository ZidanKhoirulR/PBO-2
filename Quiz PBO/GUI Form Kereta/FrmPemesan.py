import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pemesan import *
class FrmPemesan:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("550x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='ID_PEMESAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_PEMESAN:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KELAMIN:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT_PEMESAN:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NOTLP:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtId_pemesan = Entry(mainFrame) 
        self.txtId_pemesan.grid(row=0, column=1, padx=5, pady=5)
        self.txtId_pemesan.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama_pemesan = Entry(mainFrame) 
        self.txtNama_pemesan.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtKelamin = StringVar()
        Cbo_kelamin = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtKelamin) 
        Cbo_kelamin.grid(row=2, column=1, padx=5, pady=5)
        # Adding kelamin combobox drop down list
        Cbo_kelamin['values'] = ('Pria','Wanita')
        Cbo_kelamin.current()
        # Textbox
        self.txtAlamat_pemesan = Entry(mainFrame) 
        self.txtAlamat_pemesan.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtNoTlp = Entry(mainFrame) 
        self.txtNoTlp.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','id_pemesan','nama_pemesan','kelamin','alamat_pemesan','NoTlp')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="25")
        self.tree.heading('id_pemesan', text='ID Pemesan')
        self.tree.column('id_pemesan', width="100")
        self.tree.heading('nama_pemesan', text='Nama Penumpang')
        self.tree.column('nama_pemesan', width="130")
        self.tree.heading('kelamin', text='Kelamin')
        self.tree.column('kelamin', width="70")
        self.tree.heading('alamat_pemesan', text='Alamat')
        self.tree.column('alamat_pemesan', width="120")
        self.tree.heading('NoTlp', text='No Telepon')
        self.tree.column('NoTlp', width="80")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtId_pemesan.delete(0,END)
        self.txtId_pemesan.insert(END,"")
        self.txtNama_pemesan.delete(0,END)
        self.txtNama_pemesan.insert(END,"")
        self.txtKelamin.set("")
        self.txtAlamat_pemesan.delete(0,END)
        self.txtAlamat_pemesan.insert(END,"")
        self.txtNoTlp.delete(0,END)
        self.txtNoTlp.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pemesan
        obj = Pemesan()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["id_pemesan"],d["nama_pemesan"],d["kelamin"],d["alamat_pemesan"],d["NoTlp"]))
    def onCari(self, event=None):
        id_pemesan = self.txtId_pemesan.get()
        obj = Pemesan()
        a = obj.get_by_id_pemesan(id_pemesan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        id_pemesan = self.txtId_pemesan.get()
        obj = Pemesan()
        res = obj.get_by_id_pemesan(id_pemesan)
        self.txtId_pemesan.delete(0,END)
        self.txtId_pemesan.insert(END,obj.id_pemesan)
        self.txtNama_pemesan.delete(0,END)
        self.txtNama_pemesan.insert(END,obj.nama_pemesan)
        self.txtKelamin.set(obj.kelamin)
        self.txtAlamat_pemesan.delete(0,END)
        self.txtAlamat_pemesan.insert(END,obj.alamat_pemesan)
        self.txtNoTlp.delete(0,END)
        self.txtNoTlp.insert(END,obj.NoTlp)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        id_pemesan = self.txtId_pemesan.get()
        nama_pemesan = self.txtNama_pemesan.get()
        kelamin = self.txtKelamin.get()
        alamat_pemesan = self.txtAlamat_pemesan.get()
        NoTlp = self.txtNoTlp.get()
        # create new Object
        obj = Pemesan()
        obj.id_pemesan = id_pemesan
        obj.nama_pemesan = nama_pemesan
        obj.kelamin = kelamin
        obj.alamat_pemesan = alamat_pemesan
        obj.NoTlp = NoTlp
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_id_pemesan(id_pemesan)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        id_pemesan = self.txtId_pemesan.get()
        obj = Pemesan()
        obj.id_pemesan = id_pemesan
        if(self.ditemukan==True):
            res = obj.delete_by_id_pemesan(id_pemesan)
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
    aplikasi = FrmPemesan(root2, "Aplikasi Data Pemesan")
    root2.mainloop()
