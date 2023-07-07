import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Kereta import *
class FrmKereta:
    
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
        Label(mainFrame, text='ID_KERETA:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TUJUAN:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_GERBONG:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtId_kereta = Entry(mainFrame) 
        self.txtId_kereta.grid(row=0, column=1, padx=5, pady=5)
        self.txtId_kereta.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtTujuan = Entry(mainFrame) 
        self.txtTujuan.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_gerbong = Entry(mainFrame) 
        self.txtId_gerbong.grid(row=2, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','id_kereta','tujuan','id_gerbong')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('id_kereta', text='ID Kereta')
        self.tree.column('id_kereta', width="90")
        self.tree.heading('tujuan', text='Tujuan')
        self.tree.column('tujuan', width="80")
        self.tree.heading('id_gerbong', text='ID Gerbong')
        self.tree.column('id_gerbong', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtId_kereta.delete(0,END)
        self.txtId_kereta.insert(END,"")
        self.txtTujuan.delete(0,END)
        self.txtTujuan.insert(END,"")
        self.txtId_gerbong.delete(0,END)
        self.txtId_gerbong.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data kereta
        obj = Kereta()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["id_kereta"],d["tujuan"],d["id_gerbong"]))
    def onCari(self, event=None):
        id_kereta = self.txtId_kereta.get()
        obj = Kereta()
        a = obj.get_by_id_kereta(id_kereta)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        id_kereta = self.txtId_kereta.get()
        obj = Kereta()
        res = obj.get_by_id_kereta(id_kereta)
        self.txtId_kereta.delete(0,END)
        self.txtId_kereta.insert(END,obj.id_kereta)
        self.txtTujuan.delete(0,END)
        self.txtTujuan.insert(END,obj.tujuan)
        self.txtId_gerbong.delete(0,END)
        self.txtId_gerbong.insert(END,obj.id_gerbong)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        id_kereta = self.txtId_kereta.get()
        tujuan = self.txtTujuan.get()
        id_gerbong = self.txtId_gerbong.get()
        # create new Object
        obj = Kereta()
        obj.id_kereta = id_kereta
        obj.tujuan = tujuan
        obj.id_gerbong = id_gerbong
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_id_kereta(id_kereta)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        id_kereta = self.txtId_kereta.get()
        obj = Kereta()
        obj.id_kereta = id_kereta
        if(self.ditemukan==True):
            res = obj.delete_by_id_kereta(id_kereta)
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
    aplikasi = FrmKereta(root2, "Aplikasi Data Kereta")
    root2.mainloop()
