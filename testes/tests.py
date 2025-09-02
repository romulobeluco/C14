import unittest
from main import verificar_api, verificar_conteudo, verificar_https, verificar_redirecionamento

# URLs de teste (escolha URLs confiáveis para teste)
URL_VALIDA = "https://httpbin.org"  # site de testes HTTP
URL_INEXISTENTE = "https://naoexiste1234.co"
URL_REDIRECIONAMENTO = "http://httpbin.org/redirect/1"
URL_SSL_INVALIDO = "https://expired.badssl.com/"

class TestMain(unittest.TestCase):

    # =====================
    # Testes positivos
    # =====================

    def test_verificar_api_get(self):
        resultado = verificar_api(URL_VALIDA, metodo="GET")
        self.assertIn("Sucesso", resultado)

    def test_verificar_api_head(self):
        resultado = verificar_api(URL_VALIDA, metodo="HEAD")
        self.assertIn("Sucesso", resultado)

    def test_verificar_api_post(self):
        resultado = verificar_api(URL_VALIDA, metodo="POST", dados={"teste": "ok"})
        self.assertTrue("Sucesso" in resultado or "Código" in resultado)

    def test_verificar_api_put(self):
        resultado = verificar_api(URL_VALIDA, metodo="PUT")
        self.assertTrue("Sucesso" in resultado or "Código" in resultado)

    def test_verificar_api_patch(self):
        resultado = verificar_api(URL_VALIDA, metodo="PATCH")
        self.assertTrue("Sucesso" in resultado or "Código" in resultado)

    def test_verificar_conteudo_existe(self):
        resultado = verificar_conteudo(URL_VALIDA + "/get", "url")
        self.assertIn("Conteúdo encontrado", resultado)

    def test_verificar_https_valido(self):
        resultado = verificar_https(URL_VALIDA)
        self.assertIn("SSL válido", resultado)

    def test_verificar_redirecionamento(self):
        resultado = verificar_redirecionamento(URL_REDIRECIONAMENTO)
        self.assertTrue("Redirecionado para" in resultado or "Sem redirecionamento" in resultado)

    def test_verificar_metodos_get_post(self):
        resultado_get = verificar_api(URL_VALIDA, metodo="GET")
        resultado_post = verificar_api(URL_VALIDA, metodo="POST", dados={"teste": "ok"})
        self.assertTrue("Sucesso" in resultado_get)
        self.assertTrue("Sucesso" in resultado_post or "Código" in resultado_post)

    def test_verificar_redirecionamento_sem(self):
        resultado = verificar_redirecionamento(URL_VALIDA + "/get")
        self.assertIn("Sem redirecionamento", resultado)

    # =====================
    # Testes negativos
    # =====================

    def test_verificar_api_url_invalida(self):
        resultado = verificar_api(URL_INEXISTENTE)
        self.assertIn("Falha na requisição", resultado)

    def test_verificar_api_delete_url_invalida(self):
        resultado = verificar_api(URL_INEXISTENTE, metodo="DELETE")
        self.assertIn("Falha na requisição", resultado)

    def test_verificar_conteudo_nao_existe(self):
        resultado = verificar_conteudo(URL_VALIDA + "/get", "texto_que_nao_existe")
        self.assertIn("Conteúdo não encontrado", resultado)

    def test_verificar_conteudo_site_inexistente(self):
        resultado = verificar_conteudo(URL_INEXISTENTE, "qualquer")
        self.assertIn("Falha na requisição", resultado)

    def test_verificar_https_invalido(self):
        resultado = verificar_https(URL_SSL_INVALIDO)
        self.assertIn("SSL inválido", resultado)

    def test_verificar_metodos_invalido(self):
        resultado = verificar_api(URL_VALIDA, metodo="INVALID")
        self.assertIn("Falha na requisição", resultado)

    def test_verificar_metodos_options(self):
        resultado = verificar_api(URL_VALIDA, metodo="OPTIONS")
        self.assertTrue("Sucesso" in resultado or "Código" in resultado)

    def test_verificar_metodos_patch_negativo(self):
        resultado = verificar_api(URL_INEXISTENTE, metodo="PATCH")
        self.assertIn("Falha na requisição", resultado)

    def test_verificar_redirecionamento_url_inexistente(self):
        resultado = verificar_redirecionamento(URL_INEXISTENTE)
        self.assertIn("Falha na requisição", resultado)

    def test_verificar_api_post_url_inexistente(self):
        resultado = verificar_api(URL_INEXISTENTE, metodo="POST", dados={"teste": "ok"})
        self.assertIn("Falha na requisição", resultado)


if __name__ == "__main__":
    unittest.main()
