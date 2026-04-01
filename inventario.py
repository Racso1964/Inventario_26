# Mensaje de bienvenida
print("🛒 Sistema de Control de Inventario")

# Solicitando información al usuario
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad inicial en inventario: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: "))

# Cálculo del valor total del inventario
valor_total = cantidad * precio_unitario

# Mostrando los datos formateados
print("\n📦 Inventario Inicial")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: $ {precio_unitario:.2f}")
print(f"Valor total del inventario: $ {valor_total:.2f}")