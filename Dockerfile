FROM mcr.microsoft.com/azure-functions/python:4-python3.10

# Variáveis de ambiente da Azure Function
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Instala dependências Python
COPY requirements.txt /
RUN pip install --upgrade pip && pip install -r /requirements.txt

# Instala Playwright e navegador
RUN apt-get update && \
    apt-get install -y wget && \
    python -m playwright install chromium && \
    mkdir /ms-playwright && \
    cp -r /root/.cache/ms-playwright /ms-playwright

# Copia o código da function
COPY . /home/site/wwwroot