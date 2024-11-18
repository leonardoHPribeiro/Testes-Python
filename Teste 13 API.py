from http.client import responses

import requests

API_key = "14380b95e48777d4bce1ec91430a9523"

cidade = input("nome da cidade: ")

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_key}&lang=pt_br"

request = requests.get(link)
print(request)

request_dic = request.json()
print(request_dic)
m = request_dic['weather'][0]['main']
des = request_dic['weather'][0]['description']
temp = request_dic ['main']['temp'] - 273.15
print('O clima em {} é: clima: {}, descrição: {},temperatura: {:.2f}°C'.format(cidade,m,des,temp))

