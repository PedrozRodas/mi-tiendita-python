import sqlite3
opcion = ""

while opcion !="0":
    print("\n--- MI TIENDITA ---")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Ver producto")
    print("0. Salir")
    
    opcion = input("Elige una opcion: ").strip()
    
    if opcion == "1":
        conexion = sqlite3.connect("tiendita.db")
        
        resultado = conexion.execute("""
            SELECT id, nombre, precio_centavos, cantidad
            FROM productos
            """)
        for producto in resultado:
            print(producto)
        
        conexion.close()
        
    elif opcion == "2":
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio en centavos: "))
        cantidad = int(input("Cantidad disponible: "))

        conexion = sqlite3.connect("tiendita.db")

        conexion.execute("""
            INSERT INTO productos (nombre, precio_centavos, cantidad)
            VALUES (?, ?, ?)
        """, (nombre, precio, cantidad))

        conexion.commit()
        conexion.close()

        print("Producto guardado.")
        
    elif opcion == "3":
        try:
            id_producto = int(input("ID del producto que quieres vender: "))
        except ValueError:
            print("El ID debe ser un numero. Por ejemplo 3.")
            continue

        conexion = sqlite3.connect("tiendita.db")

        producto = conexion.execute("""
            SELECT nombre, cantidad
            FROM productos
            WHERE id = ?
        """, (id_producto,)).fetchone()

        if producto is None:
            print("No existe un producto con ese ID.")
        else:
            print("Producto encontrado:", producto)
            unidades = int(input("¿Cuántas unidades quieres vender? "))
            disponibles = producto[1]

            if unidades <= 0:
                print("Debes vender al menos una unidad.")
            elif unidades > disponibles:
                print("No hay suficientes unidades.")
            else:
                conexion.execute("""
                    UPDATE productos
                    SET cantidad = cantidad - ?
                    WHERE id = ?
                """, (unidades, id_producto))

                conexion.commit()
                print("Venta realizada.")

        conexion.close()
                
    elif opcion == "0":
        print("Hasta luego")
    else:
        print("opcion no valida.")