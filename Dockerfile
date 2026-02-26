# Usar uma imagem base oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Instalar dependências do sistema necessárias para o psycopg2 e outras libs
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
# Como o código está na pasta /app local, copiamos para o diretório atual no container
COPY ./app ./app

# Expor a porta que o FastAPI vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
# Nota: o diretório de trabalho é /app, e o main.py está em /app/app/main.py
# Ou podemos mudar o PYTHONPATH ou rodar de dentro da pasta app.
# Ajustando para rodar a partir da raiz /app:
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
