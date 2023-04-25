from IProducto import IProducto
from abc import ABCMeta
class Producto_decorado(IProducto,ABCMeta):
    def __new__(cls, iproducto:IProducto, *args, **kwargs):
        cls.iproducto = iproducto

    def obtener_precio(self):
        pass

    def producto_decorado(cls,iproducto:IProducto):
        pass

    def get_pbase(cls):
        return cls.iproducto
