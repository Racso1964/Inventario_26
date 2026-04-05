# Mensaje de bienvenida
print("🛒 Sistema de Control de Inventario")

# Creando una lista para almacenar productos
inventario = []

# Agregar el primer producto
producto1 = input("Ingrese el nombre del primer producto producto: ").strip().title()
cantidad1 = int(input("Ingrese la cantidad inicial en inventario: "))
precio_unitario1 = float(input("Ingrese el precio unitario del producto: "))

# Creando un diccionario para el primer producto
producto_dict1 = {
    "nombre": producto1,
    "cantidad": cantidad1,
    "precio_unitario": precio_unitario1,
    "valor_total": cantidad1 * precio_unitario1
}

# Agregando a la lista
inventario.append(producto_dict1)

# Agregar el segundo producto
producto2 = input("Ingrese el nombre del segundo producto: ").strip().title()
cantidad2 = int(input("Ingrese la cantidad inicial en inventario: "))
precio_unitario2 = float(input("Ingrese el precio unitario del producto: "))

producto_dict2 = {
    "nombre": producto2,
    "cantidad": cantidad2,
    "precio_unitario": precio_unitario2,
    "valor_total": cantidad2 * precio_unitario2
}

inventario.append(producto_dict2)

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






