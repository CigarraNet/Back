from fastapi import APIRouter, HTTPException
from db.db import conn 
from models.models import producto
from schemas.schemas import Producto

router = APIRouter(
    prefix="/productos",
    tags=["productos"], 
    responses={404: {"description": "Not found"}} 
)

@router.get("/")
async def get_productos():
    productos_src = Producto.productos_schemas(
        conn.execute(producto.select().order_by(producto.c.nombre)).fetchall()
    )
    if not productos_src:
        raise HTTPException(status_code=404, detail="No hay productos registrados")
    
    return productos_src