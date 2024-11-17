from pydantic import BaseModel
from db.db import conn
from models import models
from datetime import date

class TipoDocumento(BaseModel):
    id_tipo_documento: int | None = None
    nombre: str
    acronimo: str
    
    def tipo_documento_schemas(tipo_documento) -> dict:
        return{
            "id_tipo_documento": tipo_documento.id_tipo_documento,
            "nombre": tipo_documento.nombre,
            "acronimo": tipo_documento.acronimo
        }
        
    def tiposdocumento_schemas(tiposdocumento) -> list:
        return[TipoDocumento.tipo_documento_schemas(tipo_documento) for tipo_documento in tiposdocumento]


class TipoContrato(BaseModel):
    id_tipo_contrato: int | None = None
    contrato: str
    
    def tipo_contrato_schemas(tipo_contrato) -> dict:
        return{
            "id_tipo_contrato": tipo_contrato.id_tipo_contrato,
            "contrato": tipo_contrato.contrato
        }
        
    def tiposcontrato_schemas(tiposcontrato) -> list:
        return[TipoContrato.tipo_contrato_schemas(tipo_contrato)for tipo_contrato in tiposcontrato]
    

class Rol(BaseModel):
    id_rol: int | None = None
    rol: str
    
    def rol_schemas(rol) -> dict:
        return {
            "id_rol": rol.id_rol,
            "rol": rol.rol
        }
        
    def roles_schemas(roles) -> list:
        return[Rol.rol_schemas(rol) for rol in roles]
    
    
class Categoria(BaseModel):
    id_categoria: int | None = None
    nombre: str
    
    def categoria_schemas(categoria) -> dict:
        return{
            "id_categoria": categoria.id_categoria,
            "nombre": categoria.nombre
        }
        
    def categorias_schemas(categorias) -> list:
        return[Categoria.categoria_schemas(categoria) for categoria in categorias]
    
    
class FormaPago(BaseModel):
    id_forma_pago: int | None = None
    pago: str
    
    def formapago_schemas(forma_pago) -> dict:
        return{
            "id_forma_pago": forma_pago.id_forma_pago,
            "pago": forma_pago.pago
        }
        
    def formaspago_schemas(formaspago) -> list:
        return[FormaPago.formapago_schemas(forma_pago) for forma_pago in formaspago]
    

class Factura(BaseModel):
    id_factura: int | None = None
    fecha: date
    total: float
    
    def factura_schemas(factura) -> dict:
        return{
            "id_factura": factura.id_factura,
            "fecha": factura.fecha,
            "total": factura.total
        }
        
    def facturas_schemas(facturas) -> list:
        return[Factura.factura_schemas(factura) for factura in facturas]


class Empleado(BaseModel):
    id_empleado: int | None = None
    nombre: str
    apellidos: str
    telefono: str 
    salario: float
    numero_documento: int
    id_rol: int
    id_tipo_documento: int 
    id_tipo_contrato: int 
    
    def empleado_schemas_db(empleado) -> dict:
        return {"id_empleado": empleado.id_empleado, 
                "nombre": empleado.nombre, 
                "apellidos": empleado.apellidos, 
                "telefono": empleado.telefono, 
                "salario": empleado.salario, 
                "numero_documento": empleado.numero_documento, 
                "id_rol": empleado.id_rol,
                "id_tipo_documento": empleado.id_tipo_documento,
                "id_tipo_contrato": empleado.id_tipo_contrato}
        
    def empleados_schemas_db(empleados) -> list: 
        return[Empleado.empleado_schemas_db(empleado) for empleado in empleados]
    
    def empleado_schemas(empleado) -> dict:
        print(empleado)
        rol = Rol.rol_schemas(
            conn.execute(models.rol.select().where(models.rol.c.id_rol == empleado.id_rol)).fetchone()
        )
        
        tipo_documento = TipoDocumento.tipo_documento_schemas(
            conn.execute(models.tipo_documento.select().where(models.tipo_documento.c.id_tipo_documento == empleado.id_tipo_documento)).fetchone()
        )
     
        tipo_contrato = TipoContrato.tipo_contrato_schemas(
            conn.execute(models.tipo_contrato.select().where(models.tipo_contrato.c.id_tipo_contrato == empleado.id_tipo_contrato)).fetchone()
        )
        return {"id_empleado": empleado.id_empleado, 
                "nombre": empleado.nombre, 
                "apellidos": empleado.apellidos, 
                "telefono": empleado.telefono, 
                "salario": empleado.salario, 
                "numero_documento": empleado.numero_documento, 
                "id_rol": rol,
                "id_tipo_documento": tipo_documento,
                "id_tipo_contrato": tipo_contrato}
    
    def empleados_schemas(empleados) -> dict:
        return [Empleado.empleado_schemas(empleado) for empleado in empleados]
    
    
class Producto(BaseModel):
    id_producto: int | None = None
    nombre: str
    cantidad_TO: int
    precio_venta: float 
    precio_compra: float
    fecha_vencimiento: date
    fecha_ingreso: date
    id_categoria: int  
    
    def producto_schemas_db(producto) -> dict:
        return {"id_productos": producto.id_productos, 
                "nombre": producto.nombre, 
                "cantidad_TO": producto.cantidad_TO, 
                "precio_venta": producto.precio_venta, 
                "precio_compra": producto.precio_compra, 
                "fecha_vencimiento": producto.fecha_vencimiento, 
                "fecha_ingreso": producto.fecha_ingreso,
                "id_categoria": producto.id_categoria}
        
    def productos_schemas_db(productos) -> list: 
        return[Producto.producto_schemas_db(producto) for producto in productos]
    
    def producto_schemas(producto) -> dict:
        categoria = Categoria.categoria_schemas(
            conn.execute(models.categoria.select().where(models.categoria.c.id_categoria == producto.id_categoria)).fetchone()
        )
        return {"id_productos": producto.id_productos, 
                "nombre": producto.nombre, 
                "cantidad_TO": producto.cantidad_TO, 
                "precio_venta": producto.precio_venta, 
                "precio_compra": producto.precio_compra, 
                "fecha_vencimiento": producto.fecha_vencimiento, 
                "fecha_ingreso": producto.fecha_ingreso,
                "id_categoria": categoria}
    
    def productos_schemas(productos) -> list:
        return [Producto.producto_schemas(producto) for producto in productos]
    
    
class Proveedor(BaseModel):
    id_proveedor: int | None = None
    nombre: str
    telefono: int
    id_empleado: int
    
    def proveedor_schemas_db(proveedor) -> dict: 
        return {"id_proveedor": proveedor.id_proveedor,
                "nombre": proveedor.nombre,
                "telefono": proveedor.telefono,
                "id_empleado": proveedor.id_empleado}
        
    def proveedores_schemas_db(proveedores) -> list: 
        return[Proveedor.proveedor_schemas_db(proveedor) for proveedor in proveedores]
    
    def proveedor_schemas(proveedor) -> dict:
        empleado= Empleado.empleado_schemas(
            conn.execute(models.empleado.select().where(models.empleado.c.id_empleado == proveedor.id_empleado)).fetchone()
        )
        return {"id_proveedor": proveedor.id_proveedor,
                "nombre": proveedor.nombre,
                "telefono": proveedor.telefono,
                "id_empleado": empleado}
    
    def proveedores_schemas(proveedores) -> list: 
        return [Proveedor.proveedor_schemas(proveedor) for proveedor in proveedores]
    
    
class Ingresa(BaseModel): 
    id_ingresa: int | None = None
    nombre: str
    cantidad_ING: int
    id_proveedor: int
    
    def ingresa_schemas_db(ingresa) -> dict:
        return {"id_ingresa": ingresa.id_ingresa,
                "nombre": ingresa.nombre,
                "cantidad_ING": ingresa.cantidad_ING, 
                "id_proveedor": ingresa.id_proveedor}
        
    def ingresas_schemas_db(ingresas) -> list: 
        return[Ingresa.ingresas_schemas_db(ingresa) for ingresa in ingresas]
    
    def ingresa_schemas(ingresa) -> dict:
        print(ingresa)
        proveedor = Proveedor.proveedor_schemas(
            conn.execute(models.proveedor.select().where(models.proveedor.c.id_proveedor == ingresa.id_proveedor)).fetchone()
        )
        return {"id_ingresa": ingresa.id_ingresa,
                "nombre": ingresa.nombre,
                "cantidad_ING": ingresa.cantidad_ING, 
                "id_proveedor": proveedor}
    
    def ingresas_schemas(ingresas) -> list:
        return[Ingresa.ingresa_schemas(ingresa) for ingresa in ingresas]
    
    
class DetalleFactura(BaseModel):
    id_detalle: int | None = None
    cantidad: int
    nombre: str
    precio: float
    id_productos: int
    id_forma_pago: int
    id_factura: int
    
    def detalle_factura_schemas_db(detalle_factura) -> dict:
        return {"id_detalle": detalle_factura.id_detalle,
                "cantidad": detalle_factura.cantidad,
                "nombre": detalle_factura.nombre,
                "precio": detalle_factura.precio,
                "id_productos": detalle_factura.id_productos,
                "id_forma_pago": detalle_factura.id_forma_pago,
                "id_factura": detalle_factura.id_factura}
        
    def detallesfactura_schemas_db(detallesfactura) -> list:
        return[DetalleFactura.detalle_factura_schemas_db(detalle_factura) for detalle_factura in detallesfactura]
    
    def detalle_factura_schemas(detalle_factura) -> dict:
        producto = Producto.producto_schemas(
            conn.execute(models.producto.select().where(models.producto.c.id_productos == detalle_factura.id_productos)).fetchone()
        )
        
        forma_pago = FormaPago.formapago_schemas(
            conn.execute(models.forma_pago.select().where(models.forma_pago.c.id_forma_pago == detalle_factura.id_forma_pago)).fetchone()
        )
        
        factura = Factura.factura_schemas(
            conn.execute(models.factura.select().where(models.factura.c.id_factura == detalle_factura.id_factura)).fetchone()
        )
        return {"id_detalle": detalle_factura.id_detalle,
                "cantidad": detalle_factura.cantidad,
                "nombre": detalle_factura.nombre,
                "precio": detalle_factura.precio,
                "id_producto": producto,
                "id_forma_pago": forma_pago,
                "id_factura": factura}
        
    def detallesfactura_schemas(detallesfactura) -> list:
        return [DetalleFactura.detalle_factura_schemas(detalle_factura) for detalle_factura in detallesfactura]
    