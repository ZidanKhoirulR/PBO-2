import requests
import json
class Tiket:
    def __init__(self):
        self.__id=None
        self.__id_pemesan = None
        self.__id_kereta = None
        self.__no_kursi = None
        self.__jadwal = None
        self.__kelas = None
        self.__url = "http://localhost/appkereta/tiket_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def id_pemesan(self):
        return self.__id_pemesan
        
    @id_pemesan.setter
    def id_pemesan(self, value):
        self.__id_pemesan = value
    @property
    def id_kereta(self):
        return self.__id_kereta
        
    @id_kereta.setter
    def id_kereta(self, value):
        self.__id_kereta = value
    @property
    def no_kursi(self):
        return self.__no_kursi
        
    @no_kursi.setter
    def no_kursi(self, value):
        self.__no_kursi = value
    @property
    def jadwal(self):
        return self.__jadwal
        
    @jadwal.setter
    def jadwal(self, value):
        self.__jadwal = value
    @property
    def kelas(self):
        return self.__kelas
        
    @kelas.setter
    def kelas(self, value):
        self.__kelas = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_id_pemesan(self, id_pemesan):
        url = self.__url+"?id_pemesan="+id_pemesan
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_tiket']
            self.__id_pemesan = item['id_pemesan']
            self.__id_kereta = item['id_kereta']
            self.__no_kursi = item['no_kursi']
            self.__jadwal = item['jadwal']
            self.__kelas = item['kelas']
        return data
    def simpan(self):
        payload = {
            "id_pemesan":self.__id_pemesan,
            "id_kereta":self.__id_kereta,
            "no_kursi":self.__no_kursi,
            "jadwal":self.__jadwal,
            "kelas":self.__kelas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_id_pemesan(self, id_pemesan):
        url = self.__url+"?id_pemesan="+id_pemesan
        payload = {
            "id_pemesan":self.__id_pemesan,
            "id_kereta":self.__id_kereta,
            "no_kursi":self.__no_kursi,
            "jadwal":self.__jadwal,
            "kelas":self.__kelas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_id_pemesan(self,id_pemesan):
        url = self.__url+"?id_pemesan="+id_pemesan
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
