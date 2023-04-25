class Usuario():

    def __init__(self,nombre:str,telefono:int,direccion:str,email:str,contrasenia:str):
        self._nombre = nombre
        self._telefono = telefono
        self._direccion = direccion
        self._email = email
        self._contrasenia = contrasenia


    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, value):
        self._contrasenia = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    def verificar_contrasenia(self,contrasenia:str)->bool:
        return contrasenia == self._contrasenia
