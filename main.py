import requests

def verificar_api(url: str):
    """Função para verificar se uma API está respondendo corretamente"""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Operação realizada com sucesso!")
        else:
            print(f"Erro: código {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Falha na requisição: {e}")

if __name__ == "__main__":
    verificar_api("https://jsonplaceholder.typicode.com/")
