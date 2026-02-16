from pydantic import BaseModel, Field, EmailStr
from datetime import date


# --------------------
# Cliente
# --------------------

class ClienteBase(BaseModel):
    nombre: str
    email: EmailStr
    identificacion: str


class ClienteCreate(ClienteBase):
    pass


class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True


# --------------------
# Producto
# --------------------

class ProductoBase(BaseModel):
    nombre: str


class ProductoCreate(ProductoBase):
    pass


class ProductoResponse(ProductoBase):
    id: int

    class Config:
        from_attributes = True


# --------------------
# Envío Terrestre
# --------------------

class EnvioTerrestreCreate(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int
    fecha_registro: date
    fecha_entrega: date
    bodega_id: int
    precio_envio: float
    placa: str = Field(..., pattern="^[A-Z]{3}[0-9]{3}$")
    numero_guia: str = Field(..., min_length=10, max_length=10)


class EnvioTerrestreResponse(EnvioTerrestreCreate):
    id: int
    descuento: float
    precio_final: float

    class Config:
        from_attributes = True


# --------------------
# Envío Marítimo
# --------------------

class EnvioMaritimoCreate(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int
    fecha_registro: date
    fecha_entrega: date
    puerto_id: int
    precio_envio: float
    numero_flota: str = Field(..., pattern="^[A-Z]{3}[0-9]{4}[A-Z]$")
    numero_guia: str = Field(..., min_length=10, max_length=10)


class EnvioMaritimoResponse(EnvioMaritimoCreate):
    id: int
    descuento: float
    precio_final: float

    class Config:
        from_attributes = True



class BodegaBase(BaseModel):
    nombre: str
    ubicacion: str

class BodegaCreate(BodegaBase):
    pass

class BodegaResponse(BodegaBase):
    id: int

    class Config:
        from_attributes = True


class PuertoBase(BaseModel):
    nombre: str
    pais: str

class PuertoCreate(PuertoBase):
    pass

class PuertoResponse(PuertoBase):
    id: int

    class Config:
        from_attributes = True

