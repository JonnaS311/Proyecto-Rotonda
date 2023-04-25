from abc import abstractmethod
from abc import ABCMeta

class IProducto(metaclass=ABCMeta):
    @abstractmethod
    def obtener_precio(self):
        pass