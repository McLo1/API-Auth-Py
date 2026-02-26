from database import engine, Base
from models import User
from sqlalchemy import inspect

# Cria tabela no banco
def create_table():
    try:
        Base.metadata.create_all(bind=engine)
        print("Tabela criada com sucesso!")
    except Exception as e:
        print("Erro ao criar a tabela", e)


# Testa Conexão
def test_connection():

    try:
        with engine.connect() as connection:
            print("Conectado ao banco de dados")
    except Exception as e:
        print("Erro ao conectar ao banco de dados: ", e)

    # Verifica se a tabela existe no banco
    inspection = inspect(engine).has_table("users")

    if inspection:
        print("A tabela existe no banco")
    else:
        print("A tabela não existe no banco")
        create_table()
