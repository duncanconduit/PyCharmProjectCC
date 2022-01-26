from Iso import *
from errors import *
parse_json = getapi(url1)
rates = parse_json["conversion_rates"]
time_updated = parse_json["time_last_update_utc"]

print("Welcome to this currency converter we support 156 currencies\n the rates were last updated at",
      time_updated,
      "\npress 1 to begin or 2 for help (shows currency codes to currency list)")


while True:
    start1 = value_error()
    if start1 != 1 and start1 != 2:
        print("Error: Not a Valid Answer  Try again...")
    else:
        break

if start1 == 1:
    convert(rates)
elif start1 == 2:
    cchelp(open_file("currencies.json"))
    print('when ready restart script to return to menu')
