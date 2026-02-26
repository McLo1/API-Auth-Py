from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oAuth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# senha_teste = "1234"


# hash_da_senha = get_password_hash(senha_teste)
# print(f"Hash da senha: ", hash_da_senha)

# verificar_senha = verify_password("1234", hash_da_senha)
# print(f"A senha '1234' é válida? {verificar_senha}")

# hash_da_senha2 = get_password_hash(senha_teste)
# print(f"Novo hash da senha: ", hash_da_senha2)

#-------------------__#__---------------------------__# -------------------


load_dotenv()



SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict): 
    to_encode = data.copy()                                                 
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)                                
    to_encode.update({"exp": expire})                                       
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) 
    return encoded_jwt

def get_current_user(
        token: str = Depends(oAuth2_scheme),
        db: Session = Depends(get_db)
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id: str = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Credenciais Inválidas")
        
    except JWTError:
        raise HTTPException(status_code=401, detail="Credenciais Inválidas")
    
    user = db.query(User).filter(User.id == int(user_id)).first()

    if user is None:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    return user

