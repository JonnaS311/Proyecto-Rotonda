from datetime import datetime
from Logica import Producto
from Logica.Menu import Menu
from Usuario import Usuario

class Restaurante(Usuario):
    def __init__(self,nombre:str,telefono:int,direccion:str,email:str,contrasenia:str,horario:datetime,
                 lista_producto:list = None, lista_menu:list = None):
        super().__init__(nombre,telefono,direccion,email,contrasenia)
        self.horario = horario
        self.lista_producto = lista_producto
        self.lista_menu = lista_menu

    def crear_menu(self)->Menu:
        pass

    def crear_producto(self)->Producto:
        pass

    @property
    def lista_menu(self):
        return self.lista_menu

    @lista_menu.setter
    def lista_menu(self, value):
        self.lista_menu = value

    @property
    def horario(self):
        return self.horario

    @horario.setter
    def horario(self, value):
        self.horario = value

    @property
    def lista_producto(self):
        return self.lista_producto

    @lista_producto.setter
    def lista_producto(self, value):
        self.lista_producto = value