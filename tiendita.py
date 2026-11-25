import sqlite3
conexion = sqlite3.connect("tiendita.db")

conexion.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        precio_centavos INTEGER,
        cantidad INTEGER
    )
""")

conexion.execute("""
    INSERT INTO productos (nombre, precio_centavos, cantidad)
    VALUES (?, ?, ?)
""", ("Agua", 500, 12))

conexion.commit()
print("Producto guardado.")

conexion.close()