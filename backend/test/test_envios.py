import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

headers = {"Authorization": "Bearer secret123"}


def test_token_invalido():
    response = client.get("/clientes")
    assert response.status_code == 403 or response.status_code == 401


def test_descuento_terrestre():

    # Crear cliente
    cliente = client.post("/clientes", json={
        "nombre": "Test",
        "email": "test@test.com",
        "identificacion": "123"
    }, headers=headers)

    cliente_id = cliente.json()["id"]

    # Crear producto
    producto = client.post("/productos", json={
        "nombre": "Producto Test"
    }, headers=headers)

    producto_id = producto.json()["id"]

    # Crear bodega
    bodega = client.post("/bodegas", json={
        "nombre": "Bodega Test",
        "ubicacion": "Bogota"
    }, headers=headers)

    bodega_id = bodega.json()["id"]

    # Crear envio con descuento
    envio = client.post("/envios-terrestres", json={
        "cliente_id": cliente_id,
        "producto_id": producto_id,
        "cantidad": 20,
        "fecha_registro": "2026-02-16",
        "fecha_entrega": "2026-02-20",
        "bodega_id": bodega_id,
        "precio_envio": 1000,
        "placa": "ABC123",
        "numero_guia": "ZZZZ123456"
    }, headers=headers)

    data = envio.json()

    assert envio.status_code == 200
    assert data["descuento"] == 50
    assert data["precio_final"] == 950
