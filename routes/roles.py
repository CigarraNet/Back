from fastapi import APIRouter, HTTPException
from db.db import conn 
from models.models import rol 
from schemas.schemas import Rol

router = APIRouter(
    prefix="/roles",
    tags=["roles"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_roles():
    roles_src = Rol.roles_schemas(
        conn.execute(rol.select().order_by(rol.c.rol)).fetchall()
    )
    if not roles_src:
        raise HTTPException(status_code=404, detail="No hay roles registrados")
    
    return roles_src