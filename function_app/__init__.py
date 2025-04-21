import azure.functions as func
import json
import asyncio
from playwright.async_api import async_playwright

async def buscar_cref(cref: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://sistemacref4.com.br/crefonline/SifaOnLineServicosPublicosAction.do?metodo=servicoPublicoProfissionais")
        await page.fill("#buscaRegistro", cref)
        await page.click("input[value='CONSULTAR']")
        await page.wait_for_timeout(3000)

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