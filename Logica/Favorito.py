from Logica.Cliente import Cliente
from Logica.Pedido import Pedido


class Favorito():
    def __init__(self,cliente:Cliente, precio:int, estado:str):
        self._cliente = cliente
        self._precio = precio
        self._estado = estado
        self._pedido = precio

    def restaurar(self)->Pedido:
        pass