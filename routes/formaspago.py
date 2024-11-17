from fastapi import APIRouter, HTTPException
from db.db import conn
from models.models import forma_pago
from schemas.schemas import FormaPago

router = APIRouter(
    prefix=("/formaspago"),
    tags=["formaspago"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_formaspago():
    formaspago_src = FormaPago.formaspago_schemas(
        conn.execute(forma_pago.select().order_by(forma_pago.c.pago)).fetchall()
    )
    if not formaspago_src:
        raise HTTPException(status_code=404, detail="No hay pagos registrados")
    
    return formaspago_src