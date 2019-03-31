import requests
import json # json transforma um objeto em um dicionario
import pandas as pd # "as" colocar um apelido para o pandas = pd para simplificar
import decimal


url = "http://data.fixer.io/api/latest?access_key=b41d44f601db6646135e677f18ea6a00"
print ("Acessando base de dados...")
response = requests.get(url)
if response.status_code == 200:
    print ("Base de dados acessada com sucesso!")
    print ("Buscando informações das moedas ...")
    dados = response.json()
    day = dados ['date']
    print("Acessando dados do dia: %s/%s/%s" % (day[8:], day[5:7], day[0:4])) #a ultima posição não é impressa, ex 5:7, imprime do 5 ao 6

    euro_real = round(dados['rates']['BRL'] / dados['rates']['EUR'], 2)
    dollar_real = round(dados['rates']['BRL'] / dados['rates']['USD'], 2)
    btc_real = round(dados['rates']['BRL'] / dados['rates']['BTC'], 2)

    print ("O valor do euro é: R$%.2f" % euro_real)
    print ("O valor dollar é: R$%.2f" % dollar_real)
    print ("O valor do bitcoin é: R$%.2f" % btc_real)
    
    df = pd.DataFrame({'Moedas':['Euro','Dollar','Bitcoin'], 'Valores':[euro_real, dollar_real, btc_real]})
    df.to_csv("valores.csv", index=False, sep=";")
    print("Arquivo exportado com sucesso!")

else:
    print("Site com problemas!")

    