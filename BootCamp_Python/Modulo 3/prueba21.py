'''Crea un programa que simule una tienda de mascotas. El programa debe permitir al
usuario agregar productos al carrito, ver los productos en el carrito y finalizar la compra.
Los productos disponibles se almacenarán en un diccionario, donde la clave será el
nombre del producto y el valor será su precio. El programa debe terminar cuando el
usuario decida finalizar la compra.'''

productos = {
    "Perro": {
    "Croquetas": 15.99,
    "Juguete": 9.99,
    "Collar": 7.99
    },
    "Gato": {
    "Croquetas": 12.99,
    "Rascador": 25.99,
    "Juguete": 8.99
    }
}
carrito = {}
continuar_compra = True
while continuar_compra:
    print("\nBienvenido a la tienda de mascotas!")
    print("¿Qué deseas hacer?")
    print("1. Agregar producto al carrito")
    print("2. Ver carrito")
    print("3. Finalizar compra")
    opcion = input("Ingrese una opción (1, 2 o 3): ")
    if opcion == "1":
        mascota = input("Ingrese el tipo de mascota (Perro o Gato): ")
        if mascota in productos:
            for producto, precio in productos[mascota].items():
                print(f"- {producto}: ${precio}")
            producto_agregar = input("Ingrese el producto a agregar: ")
            if producto_agregar in productos[mascota]:
                carrito[producto_agregar]=productos[mascota][producto_agregar]
                print(f"{producto_agregar} agregado al carrito.")
            else:
                print("Producto no disponible.")
        else:
            print("Mascota no encontrada.")
    elif opcion == "2":
        if carrito:
            print("\nProductos en el carrito:")
            for producto, precio in carrito.items():
                print(f"- {producto}: ${precio}")
        else:
            print("El carrito está vacío.")
    elif opcion == "3":
        continuar_compra = False
        print("\nGracias por su compra!")
        # Aquí puedes agregar código para calcular el total, generar una factura, etc.
    else:
        print("Opción inválida.")