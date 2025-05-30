class Proyecto:
    def __init__(self,ID,CIF,nombre,estado,facturable,jefe_pr):
        self.__ID_pr=ID
        self.__CIF=CIF
        self.__nombre=nombre
        self.__estado=estado
        self.__facturable=facturable
        self.__jefe_pr=jefe_pr
    
    def __str__(self):
        return f'Proyecto: {self.__nombre}\nEstado del proyecto: {self.__estado}\nFacturable: {self.__facturable}\nJefe del proyecto: {self.__jefe_pr}'

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self,nuevo_ID):
        self.__ID=nuevo_ID
    @ID.deleter
    def ID(self):
        del self.__ID

    @property
    def CIF(self):
        return self.__CIF
    @CIF.setter
    def CIF(self,nuevo_CIF):
        self.__CIF=nuevo_CIF
    @CIF.deleter
    def CIF(self):
        del self.__CIF

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre=nuevo_nombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self,nuevo_estado):
        self.__estado=nuevo_estado
    @estado.deleter
    def estado(self):
        del self.__estado
    
    @property
    def facturable(self):
        return self.__estado
    @facturable.setter
    def facturable(self,nuevo_facturable):
        self.__facturable=nuevo_facturable
    @facturable.deleter
    def facturable(self):
        del self.__facturable

    @property
    def jefe_pr(self):
        return self.__jefe_pr
    @facturable.setter
    def jefe_pr(self,nuevo_jefe):
        self.__jefe_pr=nuevo_jefe
    @facturable.deleter
    def jefe_pr(self):
        del self.__jefe_pr


p_1=Proyecto(1,22222,'Proyecto 1','Activo','Si','Pepe')
print(p_1)

p_1.nombre='Proyecto eco'
print(p_1)

