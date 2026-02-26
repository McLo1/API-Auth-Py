# Auth API (FastAPI) 🔐

Uma API de Autenticação robusta e segura construída com **FastAPI**, utilizando **JSON Web Tokens (JWT)** para segurança e **PostgreSQL** como banco de dados. Este projeto foi desenvolvido para fornecer uma base sólida para sistemas de login, registro de usuários e proteção de rotas.

## 🚀 Funcionalidades

- **Registro de Usuários**: Cadastro seguro com hashing de senhas utilizando `bcrypt`.
- **Autenticação JWT**: Login com geração de tokens de acesso (Bearer Token).
- **Proteção de Rotas**: Middleware para validação de tokens e identificação do usuário atual.
- **Persistência de Dados**: Integração com PostgreSQL através do SQLAlchemy ORM.
- **Containerização**: Configuração pronta para rodar em Docker.
- **Documentação Automática**: Acesso ao Swagger UI (`/docs`) e ReDoc (`/redoc`).

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Banco de Dados**: PostgreSQL
- **ORM**: SQLAlchemy
- **Segurança**: JWT (jose), Passlib (bcrypt)
- **Infraestrutura**: Docker & Docker Compose

## 📋 Pré-requisitos

- Docker e Docker Compose **OU**
- Python 3.8+ e PostgreSQL instalado localmente.

## ⚙️ Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/auth-api.git
   cd auth-api
   ```

2. Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:
   ```bash
   DATABASE_URL=postgresql://user:password@localhost:5432/auth_db
   SECRET_KEY=sua_chave_secreta_aqui
   ```

## 🐳 Rodando com Docker (Recomendado)

A maneira mais rápida de subir o ambiente completo:

```bash
docker-compose up --build
```
A API estará disponível em `http://localhost:8000`.

## 🐍 Rodando Localmente

1. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/bin/activate  # Linux/macOS
   # venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

2. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

## 🔌 Endpoints da API

| Método | Endpoint | Descrição | Protegido |
| :--- | :--- | :--- | :---: |
| `GET` | `/teste` | Verifica se a API está online | ❌ |
| `POST` | `/users` | Cria um novo usuário | ❌ |
| `POST` | `/login` | Autentica usuário e retorna o Token JWT | ❌ |
| `GET` | `/me` | Retorna os dados do usuário logado | ✅ |

## 📖 Documentação

Com a API rodando, acesse:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---
Desenvolvido por [McLo1](https://github.com/McLo1)
