from errors import *


# functions


def get_api_2(x):
    url = ("https://data.messari.io/api/v1/assets/" + x + "/metrics")
    response_API = connection_error(url)
    data = response_API.text
    parse_json = json.loads(data)
    return parse_json


def crypto_2(x, c):
    b = get_api_2(x)
    e = ("price_" + c.lower())
    d = ((b['data'])["market_data"])[e]
    return d


def cchelp(a):
    for i in range(0, 156):
        print((a[i])["cc"] + " = " + (a[i])["name"])


def convert(rates):
    while True:
        currency1 = (input("Enter current currency code: ")).upper()
        value2 = float_error("Enter " + currency1 + " Value: ")
        currency2 = input("Enter wanted Currency Code: ")
        if currency1 == 'ETH' or currency1 == 'BTC':
            value3 = value2 * crypto_2(currency1, "USD")
        elif currency1 != 'USD':
            value3 = value2 / rates[currency1]
        else:
            value3 = value2
        if currency2 == 'ETH' or currency2 == 'BTC':
            Value4 = round(value3 / (crypto_2(currency2, "USD")), 5)
        else:
            Value4 = round((value3 * (rates[currency2])), 2)
        print(value2, currency1 + " =", Value4, currency2)
        start1 = int(input("Enter 1 to continue or 0 to end process\n"))
        if start1 == 0:
            break
        elif start1 != 1:
            print('continuing process Error: Invalid Option')


# retrieving api

url1 = "https://v6.exchangerate-api.com/v6/57b91e9bc9cf2dcff363bde4/latest/USD"
url2 = "https://data.messari.io/api/v1/assets/btc/metrics"


def getapi(url):
    response_API = connection_error(url)
    data: str = response_API.text
    parse_json = json.loads(data)
    return parse_json
