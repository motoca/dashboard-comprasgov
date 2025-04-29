
# Imagem base
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copiar os arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expor a porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar a aplicação
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
