class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalle(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.cantidad}"