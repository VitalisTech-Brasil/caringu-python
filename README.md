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

## Como parar a aplicação Python?

Para parar a aplicação Python rodando no Docker Compose, basta usar o seguinte comando:

```bash
sudo docker compose down
```

Se quiser iniciar novamente, basta usar o seguinte comando:

```bash
sudo docker compose up -d
```