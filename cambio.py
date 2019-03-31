import requests
import json
# json transforma um objeto em um dicionario

url = "http://data.fixer.io/api/latest?access_key=b41d44f601db6646135e677f18ea6a00"
print ("Acessando base de dados...")
response = requests.get(url)
if response.status_code == 200:
    print ("Base de dados acessada com sucesso!")
    print ("Buscando informações das moedas ...")
    dados = response.json()
    day = dados ['date']
    day= "2019-03-31"
    print("Acessando dados do dia: %s/%s/%s" % (day[8:], day[5:7], day[0:4])) #a ultima posição não é impressa, ex 5:7, imprime do 5 ao 6

    # print(dados['rates']['EUR'])
    # print(dados['rates']['BRL'])
    # print(dados['rates']['USD'])
    # print(dados['rates']['BTC'])

    euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
    print ("O valor do euro é: R$%.2f" % euro_real)
    dollar_real = dados['rates']['BRL'] / dados['rates']['USD']
    print ("O valor dollar é: R$%.2f" % dollar_real)
    btc_real = dados['rates']['BRL'] / dados['rates']['BTC']
    print ("O valor do bitcoin é: R$%.2f" % btc_real)

else:
    print("Site com problemas!")

    