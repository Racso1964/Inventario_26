import os

# Mensaje de bienvenida
print("🛒 Sistema de Control de Inventario")

# Creando una lista para almacenar productos
inventario = []

# Bucle principal del sistema
while True:
    print("\nOpciones:")
    print("1 - Agregar producto")
    print("2 - Eliminar producto")
    print("3 - Mostrar inventario")
    print("4 - Salir")
    
    opcion = input("Elija una opción: ")

    os.system("clear")


    if opcion == "1":
        # Registro de un nuevo producto
        producto = input("Ingrese el nombre del producto: ").strip().title()
        cantidad = int(input("Ingrese la cantidad inicial en inventario: "))
        precio_unitario = float(input("Ingrese el precio unitario del producto: "))

        # Creando un diccionario para el  producto
        producto_dict = {
            "nombre": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "valor_total": cantidad * precio_unitario
        }

        # Agregando el producto al inventario
        inventario.append(producto_dict)
        print(f"\n✅ ¡Producto '{producto}' agregado al inventario!")
        
    
    elif opcion == "2":
        # Eliminar un producto
        if not inventario:
            print("\n⚠️ ¡El inventario está vacío!")
            continue
        
        producto_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip().title()

        # Buscar producto en el inventario
        for producto in inventario:
            if producto["nombre"] == producto_eliminar:
                inventario.remove(producto)
                print(f"\n✅ ¡Producto '{producto_eliminar}' eliminado del inventario!")
                break
        else:
            print(f"\n❌ Producto '{producto_eliminar}' no encontrado en el inventario.")
    
    elif opcion == "3":
        # Mostrar inventario actualizado
        if not inventario:
            print("\n⚠️ ¡El inventario está vacío!")
        else:
            print("\n📦 Inventario Actualizado")
            print("-" * 40)
            for producto in inventario:
                print(f"Producto       : {producto['nombre']}")
                print(f"Cantidad       : {producto['cantidad']}")
                print(f"Precio Unitario: $ {producto['precio_unitario']:.2f}")
                print(f"Valor Total    : $ {producto['valor_total']:.2f}")
                print("-" * 40)
    
    
    
    
    
    
    
    
    
    # Mostrando los productos registrados
    print("\n📦 Inventario Actualizado")
    print("-" * 40)

    print(f"Producto       : {inventario[0]['nombre']}")
    print(f"Cantidad       : {inventario[0]['cantidad']}")
    print(f"Precio Unitario: $ {inventario[0]['precio_unitario']:.2f}")
    print(f"Valor Total    : $ {inventario[0]['valor_total']:.2f}")
    print("-" * 40)

    print(f"Producto       : {inventario[1]['nombre']}")
    print(f"Cantidad       : {inventario[1]['cantidad']}")
    print(f"Precio Unitario: $ {inventario[1]['precio_unitario']:.2f}")
    print(f"Valor Total    : $ {inventario[1]['valor_total']:.2f}")
    print("-" * 40)






