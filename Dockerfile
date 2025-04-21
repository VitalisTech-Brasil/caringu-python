FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

# Cria diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y wget

# Instala dependências Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Instala navegadores do Playwright
RUN python -m playwright install chromium