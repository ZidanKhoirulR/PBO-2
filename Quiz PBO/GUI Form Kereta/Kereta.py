import requests
import json
class Kereta:
    def __init__(self):
        self.__id=None
        self.__id_kereta = None
        self.__tujuan = None
        self.__id_gerbong = None
        self.__url = "http://localhost/appkereta/kereta_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def id_kereta(self):
        return self.__id_kereta
        
    @id_kereta.setter
    def id_kereta(self, value):
        self.__id_kereta = value
    @property
    def tujuan(self):
        return self.__tujuan
        
    @tujuan.setter
    def tujuan(self, value):
        self.__tujuan = value
    @property
    def id_gerbong(self):
        return self.__id_gerbong
        
    @id_gerbong.setter
    def id_gerbong(self, value):
        self.__id_gerbong = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_id_kereta(self, id_kereta):
        url = self.__url+"?id_kereta="+id_kereta
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__id_kereta = item['id_kereta']
            self.__tujuan = item['tujuan']
            self.__id_gerbong = item['id_gerbong']
        return data
    def simpan(self):
        payload = {
            "id_kereta":self.__id_kereta,
            "tujuan":self.__tujuan,
            "id_gerbong":self.__id_gerbong
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_id_kereta(self, id_kereta):
        url = self.__url+"?id_kereta="+id_kereta
        payload = {
            "id_kereta":self.__id_kereta,
            "tujuan":self.__tujuan,
            "id_gerbong":self.__id_gerbong
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_id_kereta(self,id_kereta):
        url = self.__url+"?id_kereta="+id_kereta
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
