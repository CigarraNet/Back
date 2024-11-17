from fastapi import APIRouter,HTTPException
from db.db import conn
from models.models import factura
from schemas.schemas import Factura

router = APIRouter(
    prefix=("/facturas"),
    tags=["facturas"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_facturas():
    facturas_src = Factura.facturas_schemas(
        conn.execute(factura.select().order_by(factura.c.fecha)).fetchall()
    )
    if not facturas_src:
        raise HTTPException(status_code=404, detail="No hay facturas registradas")
    
    return facturas_src