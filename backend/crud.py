from sqlalchemy.orm import Session
import models
import schemas
from sqlalchemy.exc import IntegrityError


# ------------------------
# CLIENTES
# ------------------------

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def get_clientes(db: Session):
    return db.query(models.Cliente).all()


def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()



# ------------------------
# ENVIO TERRESTRE
# ------------------------

def create_envio_terrestre(db: Session, envio: schemas.EnvioTerrestreCreate):
    
    # Calcular descuento
    descuento = 0
    if envio.cantidad > 10:
        descuento = envio.precio_envio * 0.05

    precio_final = envio.precio_envio - descuento

    db_envio = models.EnvioTerrestre(
        cliente_id=envio.cliente_id,
        producto_id=envio.producto_id,
        cantidad=envio.cantidad,
        fecha_registro=envio.fecha_registro,
        fecha_entrega=envio.fecha_entrega,
        bodega_id=envio.bodega_id,
        precio_envio=envio.precio_envio,
        descuento=descuento,
        precio_final=precio_final,
        placa=envio.placa,
        numero_guia=envio.numero_guia
    )

    try:
        db.add(db_envio)
        db.commit()
        db.refresh(db_envio)
        return db_envio
    except IntegrityError:
        db.rollback()
        raise ValueError("El numero de guia ya existe")


def get_envios_terrestres(db: Session, cliente_id: int = None, numero_guia: str = None):
    query = db.query(models.EnvioTerrestre)

    if cliente_id:
        query = query.filter(models.EnvioTerrestre.cliente_id == cliente_id)

    if numero_guia:
        query = query.filter(models.EnvioTerrestre.numero_guia == numero_guia)

    return query.all()



# ------------------------
# PRODUCTOS
# ------------------------

def create_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def get_productos(db: Session):
    return db.query(models.Producto).all()


# ------------------------
# BODEGAS
# ------------------------

def create_bodega(db: Session, bodega: schemas.ProductoBase):
    db_bodega = models.Bodega(**bodega.dict())
    db.add(db_bodega)
    db.commit()
    db.refresh(db_bodega)
    return db_bodega

def get_bodegas(db: Session):
    return db.query(models.Bodega).all()


# ------------------------
# ENVIO MARITIMO
# ------------------------
def create_envio_maritimo(db: Session, envio: schemas.EnvioMaritimoCreate):

    descuento = 0
    if envio.cantidad > 10:
        descuento = envio.precio_envio * 0.03

    precio_final = envio.precio_envio - descuento

    db_envio = models.EnvioMaritimo(
        cliente_id=envio.cliente_id,
        producto_id=envio.producto_id,
        cantidad=envio.cantidad,
        fecha_registro=envio.fecha_registro,
        fecha_entrega=envio.fecha_entrega,
        puerto_id=envio.puerto_id,
        precio_envio=envio.precio_envio,
        descuento=descuento,
        precio_final=precio_final,
        numero_flota=envio.numero_flota,
        numero_guia=envio.numero_guia
    )

    try:
        db.add(db_envio)
        db.commit()
        db.refresh(db_envio)
        return db_envio
    except IntegrityError:
        db.rollback()
        raise ValueError("El numero de guia ya existe")


def get_envios_maritimos(db: Session, cliente_id: int = None, numero_guia: str = None):
    query = db.query(models.EnvioMaritimo)

    if cliente_id:
        query = query.filter(models.EnvioMaritimo.cliente_id == cliente_id)

    if numero_guia:
        query = query.filter(models.EnvioMaritimo.numero_guia == numero_guia)

    return query.all()

# ------------------------
# PUERTOS
# ------------------------

def create_puerto(db: Session, puerto: schemas.PuertoCreate):
    db_puerto = models.Puerto(**puerto.dict())
    db.add(db_puerto)
    db.commit()
    db.refresh(db_puerto)
    return db_puerto

def get_puertos(db: Session):
    return db.query(models.Puerto).all()

