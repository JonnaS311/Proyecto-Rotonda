from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self,nombre:str,telefono:int,direccion:str,email:str,contrasenia:str,documento:str,tipo_pago:str):
        super().__init__(nombre,telefono,direccion,email,contrasenia)
        self._tipo_pago = tipo_pago
        self._documento = documento


    def realizar_pago(self):
        pass

    @property
    def tipo_pago(self):
        return self._tipo_pago

    @tipo_pago.setter
    def tipo_pago(self, value):
        self._tipo_pago = value

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, value):
        self._documento = value
