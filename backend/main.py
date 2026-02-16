from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
import models, schemas, crud
from security import verify_token

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Logistics API")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def root():
    return {"message": "Logistics API running"}


# ------------------------
# CLIENTES
# ------------------------

@app.post("/clientes", response_model=schemas.ClienteResponse, dependencies=[Depends(verify_token)])
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_cliente(db, cliente)


@app.get("/clientes", response_model=list[schemas.ClienteResponse], dependencies=[Depends(verify_token)])
def list_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db)


@app.get("/clientes/{cliente_id}", response_model=schemas.ClienteResponse, dependencies=[Depends(verify_token)])
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.get_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente


# ------------------------
# ENVIO TERRESTRE
# ------------------------

@app.post("/envios-terrestres", response_model=schemas.EnvioTerrestreResponse, dependencies=[Depends(verify_token)])
def create_envio_terrestre(envio: schemas.EnvioTerrestreCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_envio_terrestre(db, envio)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.get("/envios-terrestres", response_model=list[schemas.EnvioTerrestreResponse], dependencies=[Depends(verify_token)])
def list_envios_terrestres(
    cliente_id: int = None,
    numero_guia: str = None,
    db: Session = Depends(get_db)
):
    return crud.get_envios_terrestres(db, cliente_id, numero_guia)




# ------------------------
# PRODUCTOS
# ------------------------

@app.post("/productos", response_model=schemas.ProductoResponse, dependencies=[Depends(verify_token)])
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db, producto)

@app.get("/productos", response_model=list[schemas.ProductoResponse], dependencies=[Depends(verify_token)])
def list_productos(db: Session = Depends(get_db)):
    return crud.get_productos(db)

# ------------------------
# BODEGAS
# ------------------------

@app.post("/bodegas", response_model=schemas.BodegaResponse, dependencies=[Depends(verify_token)])
def create_bodega(bodega: schemas.BodegaCreate, db: Session = Depends(get_db)):
    return crud.create_bodega(db, bodega)

@app.get("/bodegas", response_model=list[schemas.BodegaResponse], dependencies=[Depends(verify_token)])
def list_bodegas(db: Session = Depends(get_db)):
    return crud.get_bodegas(db)


# ------------------------
# ENVIOS MARITIMOS
# ------------------------


@app.post("/envios-maritimos", response_model=schemas.EnvioMaritimoResponse, dependencies=[Depends(verify_token)])
def create_envio_maritimo(envio: schemas.EnvioMaritimoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_envio_maritimo(db, envio)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/envios-maritimos", response_model=list[schemas.EnvioMaritimoResponse], dependencies=[Depends(verify_token)])
def list_envios_maritimos(
    cliente_id: int = None,
    numero_guia: str = None,
    db: Session = Depends(get_db)
):
    return crud.get_envios_maritimos(db, cliente_id, numero_guia)

# ------------------------
# PUERTOS
# ------------------------


@app.post("/puertos", response_model=schemas.PuertoResponse, dependencies=[Depends(verify_token)])
def create_puerto(puerto: schemas.PuertoCreate, db: Session = Depends(get_db)):
    return crud.create_puerto(db, puerto)

@app.get("/puertos", response_model=list[schemas.PuertoResponse], dependencies=[Depends(verify_token)])
def list_puertos(db: Session = Depends(get_db)):
    return crud.get_puertos(db)
