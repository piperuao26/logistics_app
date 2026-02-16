from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    identificacion = Column(String, nullable=False)


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)


class Bodega(Base):
    __tablename__ = "bodegas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)


class Puerto(Base):
    __tablename__ = "puertos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    pais = Column(String, nullable=False)


class EnvioTerrestre(Base):
    __tablename__ = "envios_terrestres"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, nullable=False)
    fecha_registro = Column(Date, nullable=False)
    fecha_entrega = Column(Date, nullable=False)
    bodega_id = Column(Integer, ForeignKey("bodegas.id"))
    precio_envio = Column(Float, nullable=False)
    descuento = Column(Float, nullable=False)
    precio_final = Column(Float, nullable=False)
    placa = Column(String, nullable=False)
    numero_guia = Column(String, unique=True, nullable=False)


class EnvioMaritimo(Base):
    __tablename__ = "envios_maritimos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, nullable=False)
    fecha_registro = Column(Date, nullable=False)
    fecha_entrega = Column(Date, nullable=False)
    puerto_id = Column(Integer, ForeignKey("puertos.id"))
    precio_envio = Column(Float, nullable=False)
    descuento = Column(Float, nullable=False)
    precio_final = Column(Float, nullable=False)
    numero_flota = Column(String, nullable=False)
    numero_guia = Column(String, unique=True, nullable=False)
