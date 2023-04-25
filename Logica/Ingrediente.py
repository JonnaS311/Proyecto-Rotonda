from Logica import Producto_decorado


class Ingrediente(Producto_decorado):
    def __new__(cls,nombre_ingrediente:str, valor_adicional:int ,*args, **kwargs):
        cls._nombre_ingrediente = nombre_ingrediente
        cls._valor_adicional = valor_adicional

    @property
    def nombre_ingrediente(self):
        return self._nombre_ingrediente

    @nombre_ingrediente.setter
    def nombre_ingrediente(self, value):
        self._nombre_ingrediente = value

    @property
    def valor_adicional(self):
        return self._valor_adicional

    @valor_adicional.setter
    def valor_adicional(self, value):
        self._valor_adicional = value