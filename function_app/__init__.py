import azure.functions as func
import json
import asyncio
from playwright.async_api import async_playwright
import os

def encontrar_chromium_executavel():
    path_base = os.path.join(os.getcwd(), ".playwright")
    for nome in os.listdir(path_base):
        if nome.startswith("chromium-"):
            return os.path.join(path_base, nome, "chrome-linux", "chrome")
    raise FileNotFoundError("Chromium não encontrado em .playwright")


async def buscar_cref(cref: str):

    executable_path = encontrar_chromium_executavel()

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True,
            executable_path=executable_path
        )

        page = await browser.new_page()

        await page.goto(
            "https://sistemacref4.com.br/crefonline/SifaOnLineServicosPublicosAction.do?metodo=servicoPublicoProfissionais")
        await page.fill("#buscaRegistro", cref)
        await page.click("input[value='CONSULTAR']")
        await page.wait_for_selector(".table-col-15", timeout=5000)

        try:
            cref_element = await page.query_selector(".table-col-15")
            nome_element = await page.query_selector(".table-col-75")

            if cref_element and nome_element:
                return {
                    "cref": await cref_element.inner_text(),
                    "nome": await nome_element.inner_text()
                }
            else:
                return {"mensagem": "Nenhum resultado encontrado."}
        finally:
            await browser.close()


def main(req: func.HttpRequest) -> func.HttpResponse:
    cref = req.params.get('cref') or req.get_json().get('cref')

    if not cref:
        return func.HttpResponse("Parâmetro 'cref' é obrigatório.", status_code=400)

    resultado = asyncio.run(buscar_cref(cref))

    return func.HttpResponse(
        json.dumps(resultado, ensure_ascii=False),
        mimetype="application/json",
        status_code=200
    )