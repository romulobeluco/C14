import requests 

response= requests.get("https://jsonplaceholder.typicode.com/")

if response.status_code==200:
    print("Tudo OK")

else:
    print("Erro")
