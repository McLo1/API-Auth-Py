from sqlalchemy.orm import Session

from test_connection import test_connection
from fastapi import Depends, FastAPI, HTTPException
from schemas import UserCreate, UserResponse, LoginRequest
from database import get_db
from auth import get_password_hash, verify_password, create_access_token, get_current_user
from models import User

test_connection()
# Função retorna se está conectado ou erro

app = FastAPI()

@app.get("/teste")
def hello_teste():
    return {"mensagem " : "API Rodando"}

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    
    try:
        hashed_password = get_password_hash(user.password)

        db_user = User( 
            email=user.email,
            hashed_password=hashed_password
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/login")
def login(user_credential: LoginRequest, db: Session = Depends(get_db)):

    #Busca o usuario pelo email
    user = db.query(User).filter(User.email == user_credential.email).first()

    #Verifica se o ususario existe no banco
    if not user:
        return HTTPException(status_code=401, detail="Credenciais Inválidas")

    #Verifica a senha
    if not verify_password(user_credential.password, user.hashed_password):
        return HTTPException(status_code=401, detail="Credenciais inválidas")

    #Cria o token
    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.get("/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user