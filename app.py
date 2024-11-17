from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import roles, tiposdocumento, tiposcontrato, categorias, formaspago, facturas, empleados, productos, proveedores, ingresas, detallesfactura


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(roles.router)

app.include_router(tiposdocumento.router)

app.include_router(tiposcontrato.router)

app.include_router(categorias.router)

app.include_router(formaspago.router)

app.include_router(facturas.router)

app.include_router(empleados.router)

app.include_router(productos.router)

app.include_router(proveedores.router)

app.include_router(ingresas.router)

app.include_router(detallesfactura.router)

@app.get("/")
def main():
    return {"message": "Hello World"}