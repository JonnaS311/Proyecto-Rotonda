from IProducto import IProducto
class Producto(IProducto):
    def __init__(self, nombre_producto:str, precio:int):
        self._nombre_producto = nombre_producto
        self._precio = precio

    def obtener_precio(self):
        pass

    def mostrar_ingredientes(self)->list:
        pass

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    @property
    def nombre_producto(self):
        return self._nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, value):
        self._nombre_producto = value
