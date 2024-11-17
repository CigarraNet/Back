from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date, Time, Float, Boolean
from db.db import metadata, engine


tipo_documento = Table(
    "TipoDocumento",
    metadata, 
    Column("id_tipo_documento", Integer, primary_key=True),
    Column("nombre", String(50)),
    Column("acronimo", String(4))
)

tipo_contrato = Table(
    "TipoContrato",
    metadata,
    Column("id_tipo_contrato", Integer, primary_key=True),
    Column("contrato", String(20))
)

rol = Table(
    "Rol", 
    metadata,
    Column("id_rol", Integer, primary_key=True),
    Column("rol", String(20))
)

categoria = Table(
    "Categoria",
    metadata,
    Column("id_categoria", Integer, primary_key=True),
    Column("nombre", String(20))
)

forma_pago = Table(
    "FormaPago",
    metadata,
    Column("id_forma_pago", Integer, primary_key=True),
    Column("pago", String(20))
)

factura = Table(
    "Factura",
    metadata,
    Column("id_factura", Integer, primary_key=True),
    Column("fecha", Date),
    Column("total", Float)
)

empleado = Table(
    "Empleado",
    metadata,
    Column("id_empleado", Integer, primary_key=True),
    Column("nombre", String(20)),
    Column("apellidos", String(20)),
    Column("telefono", String(20)),
    Column("salario", Float),
    Column("numero_documento", Integer),
    Column("id_rol", Integer, ForeignKey("rol.id_rol"), nullable=False),
    Column("id_tipo_documento", Integer, ForeignKey("tipo_documento.id_tipo_documento"), nullable=False),
    Column("id_tipo_contrato", Integer, ForeignKey("tipo_contrato.id_tipo_contrato"), nullable=False)
)

producto = Table(
    "Productos",
    metadata, 
    Column("id_productos", Integer, primary_key=True),
    Column("nombre", String(50)),
    Column("cantidad_TO", Integer),
    Column("precio_venta", Float),
    Column("precio_compra", Float),
    Column("fecha_vencimiento", Date),
    Column("fecha_ingreso", Date),
    Column("id_categoria", Integer, ForeignKey("categoria.id_categoria"), nullable=False) 
)

proveedor = Table(
    "Proveedor",
    metadata,
    Column("id_proveedor", Integer, primary_key=True),
    Column("nombre", String(20)),
    Column("telefono", Integer),
    Column("id_empleado", Integer, ForeignKey("empleado.id_empleado"), nullable=False) 
)

ingresa = Table(
    "Ingresa",
    metadata,
    Column("id_ingresa", Integer, primary_key=True),
    Column("nombre", String(50)),
    Column("cantidad_ING", Integer),
    Column("id_proveedor", Integer, ForeignKey("proveedor.id_proveedor"), nullable=False)
)

detalles_factura = Table(
    "DetallesFactura",
    metadata,
    Column("id_detalle", Integer, primary_key=True),
    Column("cantidad", Integer),
    Column("nombre", String(255)),
    Column("precio", Float),
    Column("id_productos", Integer, ForeignKey("producto.id_productos"), nullable=False),
    Column("id_forma_pago", Integer, ForeignKey("forma_pago.id_forma_pago"), nullable=False),
    Column("id_factura", Integer, ForeignKey("factura.id_factura"), nullable=False)
)

