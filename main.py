from packages.cliente import Cliente


cliente1 = Cliente(nombre="Juan Perez", email="juan@example.com",
                   direccion="Calle 123", telefono="555-123-4567")


""" cliente1.comprar("cola")
cliente1.comprar("azucar")
cliente1.ver_carrito() """

print(cliente1)
