# Instruções para Configuração da Aplicação Python

## Passos para rodar a aplicação Python dentro da VM

1. **Acesse a VM:**
   - Use o comando SSH para acessar sua VM:
     ```bash
     ssh user@<IP-da-VM>
     ```

2. **Clone o repositório Python:**
   - Dentro da VM, clone o repositório onde está o código Python:
     ```bash
     git clone https://github.com/VitalisTech-Brasil/caringu-python.git
     ```

3. **Acesse o diretório do repositório:**
   - Navegue até o diretório do repositório:
     ```bash
     cd caringu-python
     ```

4. **Permissões para o script `setup.sh`:**
   - Dê permissão de execução para o script `setup.sh`:
     ```bash
     chmod +x setup.sh
     ```

5. **Rodar o script `setup.sh`:**
   - Execute o script `setup.sh` para realizar as configurações e rodar a aplicação:
     ```bash
     bash setup.sh
     ```

6. **Pronto! A aplicação estará rodando.**
   - Após a execução do script, o Docker deve estar configurado e a aplicação Python estará disponível na porta `8000` da sua VM.

---

## Passos para rodar a aplicação localmente

Existem duas formas de rodar a aplicação localmente no seu computador:

### Opção 1: Usando Docker Desktop (Recomendado - Mais fácil)

1. **Instale o Docker Desktop:**
   - Baixe e instale o Docker Desktop para Windows/Mac/Linux:
     - Windows/Mac: https://www.docker.com/products/docker-desktop
     - Linux: Siga as instruções para sua distribuição
   - Certifique-se de que o Docker Desktop está rodando antes de continuar

2. **Clone o repositório (se ainda não tiver):**
   ```bash
   git clone https://github.com/VitalisTech-Brasil/caringu-python.git
   cd caringu-python
   ```

3. **Suba os containers:**
   ```bash
   docker compose up -d
   ```

4. **Pronto! A aplicação estará rodando.**
   - A aplicação Python estará disponível em `http://localhost:8000`

### Opção 2: Usando PyCharm (Mais trabalhoso)

1. **Instale o PyCharm:**
   - Baixe e instale o PyCharm (Community ou Professional):
     - https://www.jetbrains.com/pycharm/download/

2. **Clone o repositório (se ainda não tiver):**
   ```bash
   git clone https://github.com/VitalisTech-Brasil/caringu-python.git
   cd caringu-python
   ```

3. **Abra o projeto no PyCharm:**
   - Abra o PyCharm
   - Selecione `File > Open` e escolha a pasta `caringu-python`

4. **Configure o interpretador Python:**
   - Vá em `File > Settings > Project: caringu-python > Python Interpreter`
   - Crie um novo ambiente virtual ou use um existente
   - Certifique-se de usar Python 3.8 ou superior

5. **Instale as dependências:**
   - Abra o terminal no PyCharm (`Alt + F12` ou `View > Tool Windows > Terminal`)
   - Instale as dependências:
     ```bash
     pip install --upgrade pip
     pip install -r requirements.txt
     python -m playwright install chromium
     ```

6. **Configure a execução:**
   - Vá em `Run > Edit Configurations`
   - Clique em `+` e selecione `Python`
   - Configure:
     - **Script path:** `main.py`
     - **Parameters:** `--host 0.0.0.0 --port 8000`
     - **Working directory:** Selecione a pasta do projeto
   - Ou execute diretamente via terminal:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```

7. **Execute a aplicação:**
   - Clique no botão `Run` ou pressione `Shift + F10`
   - A aplicação estará disponível em `http://localhost:8000`

---

## Como parar a aplicação Python?

### Na VM (Nuvem):

Para parar a aplicação Python rodando no Docker Compose, basta usar o seguinte comando:

```bash
sudo docker compose down
```

Se quiser iniciar novamente, basta usar o seguinte comando:

```bash
sudo docker compose up -d
```

### Localmente (Docker Desktop):

Para parar a aplicação Python rodando no Docker Compose, basta usar o seguinte comando:

```bash
docker compose down
```

Se quiser iniciar novamente, basta usar o seguinte comando:

```bash
docker compose up -d
```

### Localmente (PyCharm):

Para parar a aplicação, basta clicar no botão `Stop` na barra de ferramentas do PyCharm ou pressionar `Ctrl + F2`.