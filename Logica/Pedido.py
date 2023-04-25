from Logica.Cliente import Cliente
from Logica.Favorito import Favorito


class Pedido():
    def __init__(self,cliente:Cliente, precio:int, estado:str, restaurantes:list):
        self._cliente = cliente
        self._precio = precio
        self._estado = estado
        self._restaurantes = restaurantes

    def aniadir_comida(self):
        pass

    def eliminar_comida(self):
        pass

    def editar_comida(self):
        pass

    def actualizar_estado(self):
        pass

    def aniadir_favorito(self)->Favorito:
        pass

    def traer_favorito(self):
        pass

    @property
    def cliente(self):
        return self._cliente

    @property
    def precio(self):
        return self._precio

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def restaurantes(self):
        return self._restaurantes