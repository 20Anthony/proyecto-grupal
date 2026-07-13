class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalle(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.cantidad}"


class Cliente:
    def __init__(self, nombre, id_cliente, correo):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.correo = correo

    def obtener_datos(self):
        return f"Cliente: {self.nombre} | ID: {self.id_cliente} | Email: {self.correo}"


# Pruebas unitarias basicas
if __name__ == "__main__":
    prod = Producto("Laptop", 1200, 5)
    print(prod.mostrar_detalle())