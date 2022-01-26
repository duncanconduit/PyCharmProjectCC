import os
import time
try:
    import requests
except ModuleNotFoundError:
    print('Welcome, now performing first time setup.')
    time.sleep(2)
    bashCommand = "pip install -r requirements.txt"
    os.system(bashCommand)
    print('///////////////////////////////////////////\n')
    os.system('python main.py')
    raise SystemExit()
