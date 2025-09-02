import requests
import time

def verificar_api(url: str, metodo: str = "GET", dados=None) -> str:
    """Verifica se a API está respondendo corretamente com suporte a diferentes métodos"""
    try:
        inicio = time.time()
        response = requests.request(metodo.upper(), url, data=dados, timeout=5)
        fim = time.time()
        tempo = round(fim - inicio, 3)

        if response.status_code == 200:
            return f"Sucesso ({metodo}) em {tempo}s"
        else:
            return f"Erro: código {response.status_code} ({metodo}) em {tempo}s"
    except requests.exceptions.RequestException as e:
        return f"Falha na requisição ({metodo}): {e}"

def verificar_conteudo(url: str, texto_esperado: str) -> str:
    """Verifica se o conteúdo esperado existe na resposta"""
    try:
        response = requests.get(url, timeout=5)
        if texto_esperado in response.text:
            return "Conteúdo encontrado "
        else:
            return "Conteúdo não encontrado "
    except requests.exceptions.RequestException as e:
        return f"Falha na requisição: {e}"

def verificar_https(url: str) -> str:
    """Verifica se o site possui SSL válido"""
    try:
        requests.get(url, timeout=5, verify=True)
        return "SSL válido "
    except requests.exceptions.SSLError:
        return "SSL inválido "
    except requests.exceptions.RequestException as e:
        return f"Falha na requisição: {e}"

def verificar_redirecionamento(url: str) -> str:
    """Verifica se há redirecionamentos"""
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        if response.history:
            return f"Redirecionado para {response.url}"
        else:
            return "Sem redirecionamento"
    except requests.exceptions.RequestException as e:
        return f"Falha na requisição: {e}"

def verificar_metodos(url: str, metodos=None) -> dict:
    """Verifica quais métodos HTTP são aceitos por um site"""
    if metodos is None:
        metodos = ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]

    resultados = {}
    for metodo in metodos:
        try:
            response = requests.request(metodo, url, timeout=5)
            resultados[metodo] = f"Código {response.status_code}"
        except requests.exceptions.RequestException as e:
            resultados[metodo] = f"Falha: {e}"
    return resultados

if __name__ == "__main__":
    link = input("Digite o link de um site para ver se existe: ")
    print("\n--- Resultado da verificação da API ---")
    print(verificar_api(link))
    print(verificar_https(link))
    print(verificar_redirecionamento(link))

    palavra = input("\nDigite um texto para buscar no conteúdo da página: ")
    print(verificar_conteudo(link, palavra))

    print("\n--- Verificação dos métodos HTTP ---")
    metodos_resultado = verificar_metodos(link)
    for metodo, resultado in metodos_resultado.items():
        print(f"{metodo}: {resultado}")
