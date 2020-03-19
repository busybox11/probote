import os
import requests
import sys
import credentials

r = requests.post('http://127.0.0.1:21727/', json={"type": "login", "username": credentials.username, "password": credentials.password, "url": credentials.url, "cas": credentials.cas})
data = r.json()
if data['success'] == True:
    print("Succesfully logged in for Pronote")
    import bot
elif data['error'] == "Mauvais identifiants":
    print('Error : wrong credentials')
