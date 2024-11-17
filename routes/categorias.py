from fastapi import APIRouter, HTTPException
from db.db import conn
from models.models import categoria
from schemas.schemas import Categoria

router = APIRouter(
    prefix="/categorias",
    tags=["categorias"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_categorias():
    categorias_src = Categoria.categorias_schemas(
        conn.execute(categoria.select().order_by(categoria.c.nombre)).fetchall()
    )
    if not categorias_src: 
        raise HTTPException(status_code=404, detail="No hay categorias registradas")
    
    return categorias_src