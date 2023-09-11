from packages.cliente import Cliente
from packages.cliente_premium import ClientePremium
from packages.manejo_clientes import guardar_clientes


cliente1 = Cliente(nombre="Juan Perez", email="juan@example.com",
                   direccion="Calle 123", telefono="555-123-4567")

cliente2 = Cliente(nombre="Juana Maria", email="juan@example.com",
                   direccion="Calle 123", telefono="555-123-4567")

cliente3 = ClientePremium(nombre="Maria Rodriguez", email="maria@example.com",
                          direccion="Avenida 456", telefono="555-987-6543", descuento=10)


clientes = [cliente1, cliente2, cliente3]
guardar_clientes(clientes, 'clientes.json')
