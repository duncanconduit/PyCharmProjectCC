from requirements import *
import json


def cp():
    x = os.getcwd()
    return x



def open_file(name1):
    file = open(cp() + "/" + name1)
    data_json = json.loads(file.read())
    extract_json = data_json["currency_details"]
    return extract_json


def int_error(a):
    while True:
        try:
            b = int(input(a))
            break

        except ValueError:
            print("Error: Not a Valid Answer  Try again...")
    return b


def float_error(a):
    while True:
        try:
            b = float(input(a))
            break

        except ValueError:
            print("Error: Not a Valid Answer  Try again...")
    return b

def cc_error():
    b = open_file("currencies.json")
    c = open_file("cryptocurrencies.json")
    while True:
        try:
            x = input("")
            b.get(x)
            break
        except ValueError:
            print("Error: Not a Valid Answer  Try again...")
    return x

def connection_error(url):
    try:
        request = requests.get(url)
        return request
    except requests.exceptions.RequestException:
        print("Unable to connect to data source. Please check internet connection.")
        raise SystemExit()


