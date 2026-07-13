class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalle(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.cantidad}"

# Pruebas unitarias basicas
if __name__ == "__main__":
    prod = Producto("Laptop", 1200, 5)
    print(prod.mostrar_detalle())