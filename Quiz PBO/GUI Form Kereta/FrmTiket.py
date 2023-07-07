import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Tiket import *
class FrmTiket:
    
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
        Label(mainFrame, text='ID_PEMESAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_KERETA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NO_KURSI:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JADWAL:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KELAS:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtId_pemesan = Entry(mainFrame) 
        self.txtId_pemesan.grid(row=0, column=1, padx=5, pady=5)
        self.txtId_pemesan.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtId_kereta = Entry(mainFrame) 
        self.txtId_kereta.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtNo_kursi = Entry(mainFrame) 
        self.txtNo_kursi.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtKelas = Entry(mainFrame) 
        self.txtKelas.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_tiket','id_pemesan','id_kereta','no_kursi','jadwal','kelas')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_tiket', text='ID')
        self.tree.column('id_tiket', width="30")
        self.tree.heading('id_pemesan', text='ID Pemesan')
        self.tree.column('id_pemesan', width="100")
        self.tree.heading('id_kereta', text='ID Kereta')
        self.tree.column('id_kereta', width="80")
        self.tree.heading('no_kursi', text='No Kursi')
        self.tree.column('no_kursi', width="70")
        self.tree.heading('jadwal', text='Jadwal')
        self.tree.column('jadwal', width="80")
        self.tree.heading('kelas', text='Kelas')
        self.tree.column('kelas', width="60")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtId_pemesan.delete(0,END)
        self.txtId_pemesan.insert(END,"")
        self.txtId_kereta.delete(0,END)
        self.txtId_kereta.insert(END,"")
        self.txtNo_kursi.delete(0,END)
        self.txtNo_kursi.insert(END,"")
        self.txtKelas.delete(0,END)
        self.txtKelas.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data tiket
        obj = Tiket()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_tiket"],d["id_pemesan"],d["id_kereta"],d["no_kursi"],d["jadwal"],d["kelas"]))
    def onCari(self, event=None):
        id_pemesan = self.txtId_pemesan.get()
        obj = Tiket()
        a = obj.get_by_id_pemesan(id_pemesan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        id_pemesan = self.txtId_pemesan.get()
        obj = Tiket()
        res = obj.get_by_id_pemesan(id_pemesan)
        self.txtId_pemesan.delete(0,END)
        self.txtId_pemesan.insert(END,obj.id_pemesan)
        self.txtId_kereta.delete(0,END)
        self.txtId_kereta.insert(END,obj.id_kereta)
        self.txtNo_kursi.delete(0,END)
        self.txtNo_kursi.insert(END,obj.no_kursi)
        self.txtKelas.delete(0,END)
        self.txtKelas.insert(END,obj.kelas)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        id_pemesan = self.txtId_pemesan.get()
        id_kereta = self.txtId_kereta.get()
        no_kursi = self.txtNo_kursi.get()
        jadwal = self.txtJadwal.get()
        kelas = self.txtKelas.get()
        # create new Object
        obj = Tiket()
        obj.id_pemesan = id_pemesan
        obj.id_kereta = id_kereta
        obj.no_kursi = no_kursi
        obj.jadwal = jadwal
        obj.kelas = kelas
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
        obj = Tiket()
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
    aplikasi = FrmTiket(root2, "Aplikasi Data Tiket")
    root2.mainloop()
