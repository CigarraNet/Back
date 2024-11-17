from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt 
from db.db import conn 
from decouple import config
from models.models import empleado
from schemas.schemas import Empleado

oauth_schemas = OAuth2PasswordBearer(tokenUrl="Login")

ALGORITHM = config("ALGORITHM")
SECRETE_KEY = config("SECRET_KEY")

async def auth_user(token: str = Depends(oauth_schemas)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Contraseña incorrecta",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try: 
        usuario = jwt.decode(token, SECRETE_KEY, algorithms=[ALGORITHM]).get("sub")
        if usuario is None:
            raise exception
    except jwt.PyJWTError:
        raise exception
    return Empleado.empleado_schemas(conn.execute(empleado.select().where(empleado.c.numero_documento == usuario)).fetchone())

async def user_empleadoactual(current: Empleado = Depends(auth_user)):
    return current
