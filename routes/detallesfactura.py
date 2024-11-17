from fastapi import APIRouter, HTTPException
from db.db import conn 
from models.models import detalles_factura
from schemas.schemas import DetalleFactura

router = APIRouter(
    prefix="/detallesfactura",
    tags=["detallesfactura"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_detallesfactura():
    detallesfactura_src = DetalleFactura.detallesfactura_schemas(
        conn.execute(detalles_factura.select().order_by(detalles_factura.c.nombre)).fetchall()
    )
    if not detallesfactura_src: 
        raise HTTPException(status_code=404, detail="No hay detalles de factura registrados")
    
    return detallesfactura_src