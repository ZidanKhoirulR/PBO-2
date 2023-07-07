import requests
import json
class Pemesan:
    def __init__(self):
        self.__id=None
        self.__id_pemesan = None
        self.__nama_pemesan = None
        self.__kelamin = None
        self.__alamat_pemesan = None
        self.__NoTlp = None
        self.__url = "http://localhost/appkereta/pemesan_api.php"
                    
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
    def nama_pemesan(self):
        return self.__nama_pemesan
        
    @nama_pemesan.setter
    def nama_pemesan(self, value):
        self.__nama_pemesan = value
    @property
    def kelamin(self):
        return self.__kelamin
        
    @kelamin.setter
    def kelamin(self, value):
        self.__kelamin = value
    @property
    def alamat_pemesan(self):
        return self.__alamat_pemesan
        
    @alamat_pemesan.setter
    def alamat_pemesan(self, value):
        self.__alamat_pemesan = value
    @property
    def NoTlp(self):
        return self.__NoTlp
        
    @NoTlp.setter
    def NoTlp(self, value):
        self.__NoTlp = value
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
            self.__id = item['id']
            self.__id_pemesan = item['id_pemesan']
            self.__nama_pemesan = item['nama_pemesan']
            self.__kelamin = item['kelamin']
            self.__alamat_pemesan = item['alamat_pemesan']
            self.__NoTlp = item['NoTlp']
        return data
    def simpan(self):
        payload = {
            "id_pemesan":self.__id_pemesan,
            "nama_pemesan":self.__nama_pemesan,
            "kelamin":self.__kelamin,
            "alamat_pemesan":self.__alamat_pemesan,
            "NoTlp":self.__NoTlp
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_id_pemesan(self, id_pemesan):
        url = self.__url+"?id_pemesan="+id_pemesan
        payload = {
            "id_pemesan":self.__id_pemesan,
            "nama_pemesan":self.__nama_pemesan,
            "kelamin":self.__kelamin,
            "alamat_pemesan":self.__alamat_pemesan,
            "NoTlp":self.__NoTlp
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
