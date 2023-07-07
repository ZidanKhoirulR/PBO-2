import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Gerbong import *
class FrmGerbong:
    
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
        Label(mainFrame, text='ID_GERBONG:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUMLAH_KURSI:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtId_gerbong = Entry(mainFrame) 
        self.txtId_gerbong.grid(row=0, column=1, padx=5, pady=5)
        self.txtId_gerbong.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtJumlah_kursi = Entry(mainFrame) 
        self.txtJumlah_kursi.grid(row=1, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','id_gerbong','jumlah_kursi')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('id_gerbong', text='ID Gerbong')
        self.tree.column('id_gerbong', width="80")
        self.tree.heading('jumlah_kursi', text='Jumlah Kursi')
        self.tree.column('jumlah_kursi', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtId_gerbong.delete(0,END)
        self.txtId_gerbong.insert(END,"")
        self.txtJumlah_kursi.delete(0,END)
        self.txtJumlah_kursi.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data gerbong
        obj = Gerbong()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["id_gerbong"],d["jumlah_kursi"]))
    def onCari(self, event=None):
        id_gerbong = self.txtId_gerbong.get()
        obj = Gerbong()
        a = obj.get_by_id_gerbong(id_gerbong)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        id_gerbong = self.txtId_gerbong.get()
        obj = Gerbong()
        res = obj.get_by_id_gerbong(id_gerbong)
        self.txtId_gerbong.delete(0,END)
        self.txtId_gerbong.insert(END,obj.id_gerbong)
        self.txtJumlah_kursi.delete(0,END)
        self.txtJumlah_kursi.insert(END,obj.jumlah_kursi)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        id_gerbong = self.txtId_gerbong.get()
        jumlah_kursi = self.txtJumlah_kursi.get()
        # create new Object
        obj = Gerbong()
        obj.id_gerbong = id_gerbong
        obj.jumlah_kursi = jumlah_kursi
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_id_gerbong(id_gerbong)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        id_gerbong = self.txtId_gerbong.get()
        obj = Gerbong()
        obj.id_gerbong = id_gerbong
        if(self.ditemukan==True):
            res = obj.delete_by_id_gerbong(id_gerbong)
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
    aplikasi = FrmGerbong(root2, "Aplikasi Data Gerbong")
    root2.mainloop()
