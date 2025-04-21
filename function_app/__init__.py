import azure.functions as func
from playwright.sync_api import sync_playwright


def main_teste(req: func.HttpRequest) -> func.HttpResponse:
    cref_registro = req.params.get('registro')

    if not cref_registro:
        return func.HttpResponse("Parâmetro 'registro' obrigatório.", status_code=400)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            url = "https://sistemacref4.com.br/crefonline/SifaOnLineServicosPublicosAction.do?metodo=servicoPublicoProfissionais"
            page.goto(url)

            page.fill('#buscaRegistro', cref_registro)
            page.click("input[value='CONSULTAR']")

            page.wait_for_selector('.table-col-15', timeout=10000)

            crefs = page.locator('.table-col-15').all_text_contents()
            nomes = page.locator('.table-col-75').all_text_contents()

            browser.close()

            resultados = []
            for cref, nome in zip(crefs, nomes):
                cref = cref.strip()
                nome = nome.strip()

                # Ignora cabeçalhos e linhas vazias
                if cref and nome and cref.upper() != "REGISTRO" and nome.upper() != "NOME":
                    resultados.append({
                        "cref": cref,
                        "nome": nome
                    })

            return func.HttpResponse(str(resultados), status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)
