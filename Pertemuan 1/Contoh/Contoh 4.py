class Buku:

    def __init__(self, judul, penulis, editor, desainerisi, desainersampul, penerbit, isbn, tahunterbit, gambarsampul, judulhalamanisi, ukuranbuku):
        self.judul = judul
        self.penulis = penulis
        self.editor = editor
        self.desainerisi = desainerisi
        self.desainersampul = desainersampul
        self.penerbit = penerbit
        self.isbn = isbn
        self.tahunterbit = tahunterbit
        self.gambarsampul = gambarsampul
        self.judulhalamanisi = judulhalamanisi
        self.ukuranbuku = ukuranbuku

    def info(self):
        print(f"Judul : {self.judul}\nPenulis : {self.penulis}\nEditor : {self.editor}\nDesainer Isi : {self.desainerisi}\nDesainer Sampul : {self.desainersampul}\nPenerbit : {self.penerbit}\nISBN : {self.isbn}\nTahun Terbit : {self.tahunterbit}\nGambar Sampul : {self.gambarsampul}\nJudul Halaman Isi : {self.judulhalamanisi}\nUkuran Buku : {self.ukuranbuku}")
bukuA = Buku("Sang Pemimpi", "Andrea Hirata", "Imam Ridiyanto", "Kuswanto", "Dini Berry", "PT. Bentang Pustaka", "978-602-8811-37-8", "2011", "Kuswanto", "247 Halaman", "Lebarnya 13,5 cm & Tingginya 20 cm")
bukuA.info()
