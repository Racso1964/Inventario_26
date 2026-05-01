# Mensaje de bienvenida
print("🛒 Sistema de Control de Inventario")

# Creando una lista para almacenar productos
inventario = []

def agregar_producto():
    """
    Solicita los datos del producto al usuario y lo agrega al inventario.
    Garantiza que la cantidad y el precio sean números válidos.
    """
    producto = input("Ingrese el nombre del producto: ").strip().title()

    # Validación de la cantidad (solo acepta números enteros positivos)
    cantidad = (input("Ingrese la cantidad inicial en inventario: "))

    while not cantidad.isdigit():
        print("❌ Entrada inválida! La cantidad debe ser un número entero positivo.")
        cantidad = input("Ingrese la cantidad inicial en inventario: ")
    cantidad = int(cantidad)

    


def menu():
    """
    Muestra el menú de opciones y gestiona la interacción del usuario.
    """

    while True:
        print("\nOpciones:")
        print("1 - Agregar producto")
        print("2 - Eliminar producto")
        print("3 - Mostrar inventario")
        print("4 - Salir")
    
        opcion = input("Elija una opción: ")

        #os.system("cls")


        if opcion == "1":
            pass
            
            # Registro de un nuevo producto
            
            
            #precio_unitario = float(input("Ingrese el precio unitario del producto: "))

            # Creando un diccionario para el  producto
            #producto_dict = {
                #"nombre": producto,
                #"cantidad": cantidad,
                #"precio_unitario": precio_unitario,
                #"valor_total": cantidad * precio_unitario
            #}

            # Agregando el producto al inventario
            #inventario.append(producto_dict)
            #print(f"\n✅ ¡Producto '{producto}' agregado al inventario!")
        
    
        elif opcion == "2":
            #Eliminar un producto
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
    
        elif opcion == "4":
            print("\n👋 Saliendo del sistema...")
            break
    
        else:
            print("\n❌ ¡Opción inválida! Elija una opción del 1 al 4.")

    


