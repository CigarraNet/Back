from fastapi import APIRouter, HTTPException, Depends
from db.db import conn 
from models.models import empleado
from schemas.schemas import Empleado
import jwt
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from decouple import config 
from datetime import datetime, timedelta
from auth.auth_user import user_empleadoactual

router = APIRouter(
    prefix="/empleados",
    tags=["empleados"],
    responses={404: {"description": "Not found"}}
)

Crypt_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto" 
)

ALGORITHM = config("ALGORITHM")
SECRETE_KEY = config("SECRET_KEY")
ACCESS_TOKEN_DURATION = int(config("ACCESS_TOKEN_DURATION"))

@router.get("/")
async def get_roles():
    empleados_src = Empleado.empleados_schemas(
        conn.execute(empleado.select().order_by(empleado.c.nombre)).fetchall()
    )
    if not empleados_src: 
        raise HTTPException(status_code=404, detail="No hay empleados registrados")
    
    return empleados_src


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_src = conn.execute(empleado.select().where(empleado.c.numero_documento == form.username)).first()
    if not user_src:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    user = Empleado.empleado_schemas(user_src)
    
    if not str(user["numero_documento"]) == str(form.password):
        raise HTTPException(status_code=404, detail="Contraseña incorrecta")
    
    access_token = jwt.encode(
        {
        "sub": user["numero_documento"],
        "exp": datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_DURATION)
        },
        SECRETE_KEY,
        algorithm=ALGORITHM
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
async def me(empleado: Empleado = Depends(user_empleadoactual)):
    return empleado