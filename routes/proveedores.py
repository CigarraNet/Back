from fastapi import APIRouter,HTTPException
from db.db import conn
from models.models import proveedor
from schemas.schemas import Proveedor

router = APIRouter(
    prefix="/proveedores",
    tags=["proveedores"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_proveedores(): 
    proveedores_src = Proveedor.proveedores_schemas(
        conn.execute(proveedor.select().order_by(proveedor.c.nombre)).fetchall()
    )
    if not proveedores_src: 
        raise HTTPException(status_code=404, detail="No hay proveedores registrados")
    
    return proveedores_src