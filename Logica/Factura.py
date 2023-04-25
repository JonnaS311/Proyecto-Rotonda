from datetime import datetime
from Logica.Pedido import Pedido

class Factura():
    def __init__(self, pedido:Pedido, fecha:datetime):
        self._pedido = pedido
        self._fecha = fecha

    def verificar_pago(self)->bool:
        pass

    def registrar(self):
        pass

    @property
    def fecha(self):
        return self._fecha

    @property
    def pedido(self):
        return self._pedido