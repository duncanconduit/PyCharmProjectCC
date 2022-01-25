import json
import os

import requests


# functions
def cp():
    x = os.getcwd()
    return x


def open_file(name1):
    file = open(cp() + "/" + name1)
    data_json = json.loads(file.read())
    extract_json = data_json["currency_details"]
    return extract_json

def cchelp(a):
    for i in range(0, 156):
        print((a[i])["cc"] + " = " + (a[i])["name"])


def convert(rates):
    while True:
        Currency1 = input("Enter current currency code: ")
        Value2 = float(input("Enter " + Currency1 + " Value: "))
        if Currency1 != "USD":
            Value3 = Value2 / (rates[Currency1])
        else:
            Value3 = Value2
        Currency2 = input("Enter wanted Currency Code: ")
        Value4 = round((Value3 * (rates[Currency2])), 2)
        print(Value2, Currency1 + " =", Value4, Currency2)
        start1 = int(input("Enter 1 to continue or zero to end process\n"))
        if start1 == 0:
            break
        elif start1 != 1:
            print('continuing process Error: Invalid Option')


# retrieving api

url1 = "https://v6.exchangerate-api.com/v6/57b91e9bc9cf2dcff363bde4/latest/USD"
def getapi(url):
    response_API = requests.get(url)
    data: str = response_API.text
    parse_json = json.loads(data)
    return parse_json




# json file




