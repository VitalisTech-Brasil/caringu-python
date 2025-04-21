FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -m playwright install chromium

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]