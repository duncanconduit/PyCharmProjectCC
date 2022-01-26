from requirements import *
def value_error():
    while True:
        try:
            start = int(input(""))
            break

        except ValueError:
            print("Error: Not a Valid Answer  Try again...")
    return start


def connection_error(url):
    try:
        request = requests.get(url)
        return request
    except requests.exceptions.RequestException:
        print("Unable to connect to data source. Please check internet connection.")
        raise SystemExit()
