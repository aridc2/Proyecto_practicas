class Proyecto:
    def __init__(self,ID,nombre,estado,facturable,jefe_pr):
        self.__ID_pr=ID
        self.__nombre=nombre
        self.__estado=estado
        self.__facturable=facturable
        self.__jefe_pr=jefe_pr
    
    def __str__(self):
       return f'Proyecto: {self.__nombre}\nEstado del proyecto: {self.__estado}\nFacturable: {self.__facturable}\nJefe del proyecto: {self.__jefe_pr}'

    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre=nuevo_nombre


p_1=Proyecto(1,'Proyecto 1','Activo','Si','Pepe')
print(p_1)

p_1.nombre='Proyecto eco'
print(p_1)