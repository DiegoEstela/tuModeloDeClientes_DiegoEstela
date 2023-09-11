from packages.cliente import Cliente


class ClientePremium(Cliente):
    def __init__(self, nombre, email, direccion, telefono, descuento):
        super().__init__(nombre, email, direccion, telefono)
        self.descuento = descuento

    def aplicar_descuento(self, monto):
        return monto * (1 - self.descuento / 100)
