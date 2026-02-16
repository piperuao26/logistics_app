CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    identificacion TEXT NOT NULL
);

CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

CREATE TABLE bodegas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    ubicacion TEXT NOT NULL
);

CREATE TABLE puertos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    pais TEXT NOT NULL
);

CREATE TABLE envios_terrestres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER NOT NULL,
    fecha_registro DATE NOT NULL,
    fecha_entrega DATE NOT NULL,
    bodega_id INTEGER,
    precio_envio REAL NOT NULL,
    descuento REAL NOT NULL,
    precio_final REAL NOT NULL,
    placa TEXT NOT NULL,
    numero_guia TEXT UNIQUE NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    FOREIGN KEY(producto_id) REFERENCES productos(id),
    FOREIGN KEY(bodega_id) REFERENCES bodegas(id)
);

CREATE TABLE envios_maritimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER NOT NULL,
    fecha_registro DATE NOT NULL,
    fecha_entrega DATE NOT NULL,
    puerto_id INTEGER,
    precio_envio REAL NOT NULL,
    descuento REAL NOT NULL,
    precio_final REAL NOT NULL,
    numero_flota TEXT NOT NULL,
    numero_guia TEXT UNIQUE NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    FOREIGN KEY(producto_id) REFERENCES productos(id),
    FOREIGN KEY(puerto_id) REFERENCES puertos(id)
);
