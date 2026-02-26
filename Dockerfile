# Usar uma imagem base oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Instalar dependências do sistema necessárias para o psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o CONTEÚDO da pasta app para a raiz do WORKDIR (/app)
# Isso permite que os imports funcionem como 'from test_connection import ...'
COPY ./app /app

# Expor a porta que o FastAPI vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
# Agora apontamos para 'main:app' diretamente, pois main.py está em /app/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
