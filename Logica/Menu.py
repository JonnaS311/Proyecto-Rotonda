class Menu():
    def __init__(self, productos:list, nombre_menu:str, precio_menu:int):
        self._productos = productos
        self._nombre_menu = nombre_menu
        self._precio_menu = precio_menu

    def mostrar_productos(self)->list:
        pass

    def cantidad_productos(self)->int:
        pass

    @property
    def precio_menu(self):
        return self._precio_menu

    @precio_menu.setter
    def precio_menu(self, value):
        self._precio_menu = value

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, value):
        self._productos = value

    @property
    def nombre_menu(self):
        return self._nombre_menu

    @nombre_menu.setter
    def nombre_menu(self, value):
        self._nombre_menu = value