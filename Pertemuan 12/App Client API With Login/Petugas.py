import requests
import json
class Petugas:
    def __init__(self):
        self.__id=None
        self.__kode_petugas = None
        self.__nama_petugas = None
        self.__no_telp = None
        self.__alamat = None
        self.__url = "http://localhost/appperpus/petugas_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_petugas(self):
        return self.__kode_petugas
        
    @kode_petugas.setter
    def kode_petugas(self, value):
        self.__kode_petugas = value
    @property
    def nama_petugas(self):
        return self.__nama_petugas
        
    @nama_petugas.setter
    def nama_petugas(self, value):
        self.__nama_petugas = value
    @property
    def no_telp(self):
        return self.__no_telp
        
    @no_telp.setter
    def no_telp(self, value):
        self.__no_telp = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_petugas(self, kode_petugas):
        url = self.__url+"?kode_petugas="+kode_petugas
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_petugas']
            self.__kode_petugas = item['kode_petugas']
            self.__nama_petugas = item['nama_petugas']
            self.__no_telp = item['no_telp']
            self.__alamat = item['alamat']
        return data
    def simpan(self):
        payload = {
            "kode_petugas":self.__kode_petugas,
            "nama_petugas":self.__nama_petugas,
            "no_telp":self.__no_telp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_petugas(self, kode_petugas):
        url = self.__url+"?kode_petugas="+kode_petugas
        payload = {
            "kode_petugas":self.__kode_petugas,
            "nama_petugas":self.__nama_petugas,
            "no_telp":self.__no_telp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_petugas(self,kode_petugas):
        url = self.__url+"?kode_petugas="+kode_petugas
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
