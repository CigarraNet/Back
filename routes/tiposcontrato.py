from fastapi import APIRouter, HTTPException
from db.db import conn
from models.models import tipo_contrato
from schemas.schemas import TipoContrato

router = APIRouter(
    prefix="/tiposcontrato",
    tags=["tiposcontrato"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_tiposcontrato():
    tipo_contrato_src = TipoContrato.tiposcontrato_schemas(
        conn.execute(tipo_contrato.select().order_by(tipo_contrato.c.contrato)).fetchall()
    )
    if not tipo_contrato_src:
        raise HTTPException(status_code=404, detail="No hay contratos registrados")
    
    return tipo_contrato_src