from fastapi import FastAPI, Request
from playwright.sync_api import sync_playwright
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/consultar")
async def consulta_cref(registro: str = None):
    if not registro:
        return JSONResponse({"erro": "Parâmetro 'registro' obrigatório."}, status_code=400)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            url = "https://sistemacref4.com.br/crefonline/SifaOnLineServicosPublicosAction.do?metodo=servicoPublicoProfissionais"
            page.goto(url)

            page.fill('#buscaRegistro', registro)
            page.click("input[value='CONSULTAR']")
            page.wait_for_selector('.table-col-15', timeout=10000)

            crefs = page.locator('.table-col-15').all_text_contents()
            nomes = page.locator('.table-col-75').all_text_contents()
            browser.close()

            resultados = []
            for cref, nome in zip(crefs, nomes):
                cref = cref.strip()
                nome = nome.strip()
                if cref and nome and cref.upper() != "REGISTRO" and nome.upper() != "NOME":
                    resultados.append({"cref": cref, "nome": nome})

            return JSONResponse(resultados, status_code=200)

    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)