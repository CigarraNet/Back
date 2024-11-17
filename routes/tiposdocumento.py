from fastapi import APIRouter, HTTPException
from db.db import conn
from models.models import tipo_documento
from schemas.schemas import TipoDocumento

router = APIRouter(
    prefix="/tiposdocumento",
    tags=["tiposdocumento"],
    responses={404: {"description": "Not found"}}
)
  
@router.get("/")
async def get_tiposdocumento():
    tiposdocumento_src = TipoDocumento.tiposdocumento_schemas(
        conn.execute(tipo_documento.select().order_by(tipo_documento.c.nombre)).fetchall()
    )
    if not tiposdocumento_src:
        raise HTTPException(status_code=404, detail="No hay tiposdocumento registrados")
    
    return tiposdocumento_src
