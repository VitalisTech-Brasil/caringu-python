import azure.functions as func
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def main(req: func.HttpRequest) -> func.HttpResponse:
    cref = req.params.get('cref')

    if not cref:
        try:
            req_body = req.get_json()
        except ValueError:
            return func.HttpResponse(
                "Parâmetro 'cref' não informado.",
                status_code=400
            )
        else:
            cref = req_body.get('cref')

    if not cref:
        return func.HttpResponse(
            "Parâmetro 'cref' é obrigatório.",
            status_code=400
        )

    # Iniciar o navegador headless
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
    except Exception as e:
        return func.HttpResponse(
            f"Erro ao iniciar o Chrome: {str(e)}",
            status_code=500
        )

    try:
        # Acessar site
        driver.get("https://sistemacref4.com.br/crefonline/SifaOnLineServicosPublicosAction.do?metodo=servicoPublicoProfissionais")
        time.sleep(3)

        # Preencher input com CREF
        cref_input = driver.find_element(By.ID, "buscaRegistro")
        cref_input.send_keys(cref)

        # Clicar no botão de consulta
        botao = driver.find_element(By.XPATH, "//input[@value='CONSULTAR']")
        botao.click()
        time.sleep(5)

        # Coletar os dados da resposta
        resultado = {}

        col_cref = driver.find_elements(By.CLASS_NAME, "table-col-15")
        col_nome = driver.find_elements(By.CLASS_NAME, "table-col-75")

        if col_cref and col_nome:
            resultado = {
                "cref": col_cref[0].text.strip(),
                "nome": col_nome[0].text.strip()
            }
        else:
            resultado = {"mensagem": "Nenhum resultado encontrado."}

        return func.HttpResponse(
            json.dumps(resultado, ensure_ascii=False),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            f"Erro durante a verificação: {str(e)}",
            status_code=500
        )
    finally:
        driver.quit()

