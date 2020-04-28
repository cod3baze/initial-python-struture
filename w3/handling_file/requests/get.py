import requests

try:
    x = requests.get('https://w3schools.com/python/demopage.htm')
    print(x.text)
except Exception as e:
    print(e.args)
finally:
    print("fim")