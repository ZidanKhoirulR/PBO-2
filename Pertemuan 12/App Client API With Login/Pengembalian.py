import requests
import json
class Pengembalian:
    def __init__(self):
        self.__id=None
        self.__kode_pengembalian = None
        self.__tanggal_pengembalian = None
        self.__denda = None
        self.__id_buku = None
        self.__id_anggota = None
        self.__id_petugas = None
        self.__url = "http://localhost/appperpus/pengembalian_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_pengembalian(self):
        return self.__kode_pengembalian
        
    @kode_pengembalian.setter
    def kode_pengembalian(self, value):
        self.__kode_pengembalian = value
    @property
    def tanggal_pengembalian(self):
        return self.__tanggal_pengembalian
        
    @tanggal_pengembalian.setter
    def tanggal_pengembalian(self, value):
        self.__tanggal_pengembalian = value
    @property
    def denda(self):
        return self.__denda
        
    @denda.setter
    def denda(self, value):
        self.__denda = value
    @property
    def id_buku(self):
        return self.__id_buku
        
    @id_buku.setter
    def id_buku(self, value):
        self.__id_buku = value
    @property
    def id_anggota(self):
        return self.__id_anggota
        
    @id_anggota.setter
    def id_anggota(self, value):
        self.__id_anggota = value
    @property
    def id_petugas(self):
        return self.__id_petugas
        
    @id_petugas.setter
    def id_petugas(self, value):
        self.__id_petugas = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_pengembalian(self, kode_pengembalian):
        url = self.__url+"?kode_pengembalian="+kode_pengembalian
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_pengembalian']
            self.__kode_pengembalian = item['kode_pengembalian']
            self.__tanggal_pengembalian = item['tanggal_pengembalian']
            self.__denda = item['denda']
            self.__id_buku = item['id_buku']
            self.__id_anggota = item['id_anggota']
            self.__id_petugas = item['id_petugas']
        return data
    def simpan(self):
        payload = {
            "kode_pengembalian":self.__kode_pengembalian,
            "tanggal_pengembalian":self.__tanggal_pengembalian,
            "denda":self.__denda,
            "id_buku":self.__id_buku,
            "id_anggota":self.__id_anggota,
            "id_petugas":self.__id_petugas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_pengembalian(self, kode_pengembalian):
        url = self.__url+"?kode_pengembalian="+kode_pengembalian
        payload = {
            "kode_pengembalian":self.__kode_pengembalian,
            "tanggal_pengembalian":self.__tanggal_pengembalian,
            "denda":self.__denda,
            "id_buku":self.__id_buku,
            "id_anggota":self.__id_anggota,
            "id_petugas":self.__id_petugas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_pengembalian(self,kode_pengembalian):
        url = self.__url+"?kode_pengembalian="+kode_pengembalian
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
