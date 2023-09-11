class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.carrito_compras = []

    def __str__(self):
        return f"Se creo el Cliente: {self.nombre}, Email: {self.email}"

    def actualizar_info_contacto(self, email, telefono):
        self.email = email
        self.telefono = telefono

    def actualizar_direccion(self, direccion):
        self.direccion = direccion

    def comprar(self, producto):
        self.carrito_compras.append(producto)

    def ver_carrito(self):
        if self.carrito_compras:
            print("Carrito de compras:")
            for producto in self.carrito_compras:
                print(producto)
        else:
            print("No hay compras en el carrito.")
