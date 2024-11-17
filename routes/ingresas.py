from fastapi import APIRouter, HTTPException
from db.db import conn 
from models.models import ingresa
from schemas.schemas import Ingresa

router = APIRouter(
    prefix="/ingresas",
    tags=["ingresas"],
    responses={404: {"description": " Not found"}}
)

@router.get("/")
async def get_ingresas():
    ingresas_src = Ingresa.ingresas_schemas(
        conn.execute(ingresa.select().order_by(ingresa.c.nombre)).fetchall()
    )
    if not ingresas_src: 
        raise HTTPException(status_code=404, detail="No hay ingresos registrados")
    
    return ingresas_src