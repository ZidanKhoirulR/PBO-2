import requests
import json
class Gerbong:
    def __init__(self):
        self.__id=None
        self.__id_gerbong = None
        self.__jumlah_kursi = None
        self.__url = "http://localhost/appkereta/gerbong_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def id_gerbong(self):
        return self.__id_gerbong
        
    @id_gerbong.setter
    def id_gerbong(self, value):
        self.__id_gerbong = value
    @property
    def jumlah_kursi(self):
        return self.__jumlah_kursi
        
    @jumlah_kursi.setter
    def jumlah_kursi(self, value):
        self.__jumlah_kursi = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_id_gerbong(self, id_gerbong):
        url = self.__url+"?id_gerbong="+id_gerbong
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__id_gerbong = item['id_gerbong']
            self.__jumlah_kursi = item['jumlah_kursi']
        return data
    def simpan(self):
        payload = {
            "id_gerbong":self.__id_gerbong,
            "jumlah_kursi":self.__jumlah_kursi
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_id_gerbong(self, id_gerbong):
        url = self.__url+"?id_gerbong="+id_gerbong
        payload = {
            "id_gerbong":self.__id_gerbong,
            "jumlah_kursi":self.__jumlah_kursi
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_id_gerbong(self,id_gerbong):
        url = self.__url+"?id_gerbong="+id_gerbong
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
