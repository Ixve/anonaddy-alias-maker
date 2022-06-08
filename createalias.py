import requests
import random

token = "PUT YOUR TOKEN HERE"

def r(length):
    return ''.join(random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm') for i in range (length))
    
def grabusername():
    url = 'https://app.anonaddy.com/api/v1/account-details'
    headers = {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
      'Authorization': 'Bearer {token}'
    }

    c = requests.get(url, headers=headers).json()
    global v
    v = c["data"]["username"]
    

def genalias():
    url = 'https://app.anonaddy.com/api/v1/aliases'
    headers = {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': f'Bearer {token}'
        }

    payload = {
            "domain": "{v}.anonaddy.com",
            "description": f"pyAliasMaker | {r(8)}",
            "format": "custom",
            "local_part": f"{r(10)}",
        }

    x = requests.post(url, headers=headers, json=payload).json()
    print("Alias created: ", x)

grabusername()
genalias()
