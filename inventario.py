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

    # Validación del precio unitario (solo acepta números decimales positivos)
    precio_unitario = (input("Ingrese el precio unitario del producto: "))
    while not (precio_unitario.replace(".", "").isdigit() or precio_unitario.replace(",", "").isdigit()):
        print("❌ Entrada inválida! El precio debe ser un número positivo (ej: 10.50).")
        precio_unitario = input("Ingrese el precio unitario del producto: ")

    # Reemplazar coma por punto, si es necesario
    precio_unitario = float(precio_unitario.replace(",", "."))

    #Creando un diccionario para el  producto
    producto_dict = {
                "nombre": producto,
                "cantidad": cantidad,
                "precio_unitario": precio_unitario,
                "valor_total": cantidad * precio_unitario
    }

    # Agregando el producto al inventario
    inventario.append(producto_dict)
    print(f"\n✅ ¡Producto '{producto}' agregado al inventario!")

def eliminar_producto(producto_eliminar):
    """
    Elimina un producto del inventario según el nombre proporcionado.

    Parámetros:
    - producto_eliminar (str): Nombre del producto a eliminar.

    Retorno:
    - None
    """
    if not inventario:
                print("\n⚠️ ¡El inventario está vacío!")
                return
    
    for producto in inventario:
        if producto["nombre"] == producto_eliminar:
            inventario.remove(producto)
            print(f"\n✅ ¡Producto '{producto_eliminar}' eliminado del inventario!")
            return
                
    print(f"\n❌ Producto '{producto_eliminar}' no encontrado en el inventario.")

def mostrar_inventario():
    """
    Muestra todos los productos registrados en el inventario.
    """
    if not inventario:
        print("\n⚠️ ¡El inventario está vacío!")
        return

    print("\n📦 Inventario Actualizado")
    print("-" * 40)
    for producto in inventario:
        print(f"Producto       : {producto['nombre']}")
        print(f"Cantidad       : {producto['cantidad']}")
        print(f"Precio Unitario: $ {producto['precio_unitario']:.2f}")
        print(f"Valor Total    : $ {producto['valor_total']:.2f}")
        print("-" * 40)

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
            agregar_producto()
        elif opcion == "2":       
            producto_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip().title()






            # Buscar producto en el inventario
            
            
                
    
        elif opcion == "3":
            # Mostrar inventario actualizado
            
            else:
                
    
        elif opcion == "4":
            print("\n👋 Saliendo del sistema...")
            break
    
        else:
            print("\n❌ ¡Opción inválida! Elija una opción del 1 al 4.")

# Llamando al menú para iniciar el sistema
menu()

    


