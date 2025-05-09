###
# Trabajo de Practicas 1º de DAM
# Autor: Ariadne Díaz y Pablo Gutiérrez
# Fecha_Inicio: 2025-05-01
# Definicion de clases
###

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ------------------------------Clase Empresa----------------------------- #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
class Empresa:

    tipos_sociedad = ["Sociedad Anónima", "Sociedad Limitada", " Sociedad Cooperativa", "Sociedad Comanditaria", "Sociedad Civil", "Sociedad autonoma" , "Sociedad annónima", "Sociedad colecctiva"]
    sector = ["Agricultura", "Pesca", "Minería", "Silvicultura","Industria alimentaria", "Construcción", "Metalurgia", "Automoción", "Química", "Textil", "Manufactura","Comercio", "Transporte y logística", "Hostelería y turismo", "Educación", "Sanidad", "Servicios financieros","Consuloría", "Tecnología", "Software", "Consultoría especializada", "Startups tecnológicas","ONG", "Asistencia social", "Servicios culturales", "Formación personal"]
    def __init__(self, CIF, nombre_empresa, tipo_sociedad=None, sector=None, localidad=None, telefono=None):
        self.__CIF = CIF
        self._nombre_empresa = nombre_empresa
        # if tipo_sociedad in Empresa.tipos_sociedad:
        self._tipos_sociedad = tipo_sociedad
        # else:
        #     raise ValueError(f"Tipo de empresa no válido. Debe ser uno de: {', '.join(Empresa.tipos_sociedad)}")
        # if sector in Empresa.sector:
        self._sector = sector
        # else:
        #     raise ValueError(f"Tipo de sector no valido. Debe ser uni de: {', '.join(Empresa.sector)}")
        self._localidad = localidad
        self._telefono = telefono
        
    # Método para mostrar la información de la empresa
    def __str__(self):
        return f'Datos de la empresa: \nCIF: {self.__CIF}\nNombre: {self._nombre_empresa}\nTipo de Sociedad: {self._tipos_sociedad}\nSector: {self._sector}\nLocalidad: {self._localidad}\nTelefono {self._telefono}\n'
    
    # ----------- #
    # # # CIF # # #
    # ----------- #
    @property
    def getCIF(self):
        return self.__CIF
    
    @getCIF.setter
    def setCIF(self, CIF):
        self.__CIF = CIF
        
    @getCIF.deleter
    def delCIF(self):
        del self.__CIF
    # -------------- #
    # # # Nombre # # #
    # -------------- #
    @property
    def getNombre(self):
        return self._nombre_empresa
    
    @getNombre.setter
    def setNombre(self, new_nombre):
        self._nombre_empresa = new_nombre
    
    @getNombre.deleter
    def delNombre(self):
        del self._nombre_empresa
        
    # ------------------------- #
    # # # Tipos de Sociedad # # #
    # ------------------------- #
    @property
    def getTS(self):
        return self._tipos_sociedad
    
    @getTS.setter
    def setTS (self, new_TS):
        self._tipos_sociedad = new_TS
        
    @getTS.deleter
    def delTS(self):
        del self._tipos_sociedad
        
    # -------------- #
    # # # Sector # # #
    # -------------- #
    @property
    def getSector(self):
        return self._sector
    
    @getSector.setter
    def setSector(self, new_sector):
        self._sector = new_sector
        
    @getSector.deleter
    def delSector(self):
        del self._sector
        
    # ----------------- #
    # # # Localidad # # #
    # ----------------- #
    @property
    def getLocalidad(self):
        return self._localidad
    
    @getLocalidad.setter
    def setLocalidad(self, new_localidad):
        self._localidad = new_localidad
        
    @getLocalidad.deleter
    def delLocalidad(self):
        del self._localidad
        
    # ---------------- #
    # # # Telefono # # #
    # ---------------- #
    @property
    def getTelefono(self):
        return self._telefono
    
    @getTelefono.setter
    def setTelefono(self,new_telefono):
        self._telefono = new_telefono
        
    @getTelefono.deleter
    def delTelefono(self):
        del self._telefono
    

        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# -----------------------------Clase Proyecto----------------------------- #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

class Proyecto(Empresa):
    def __init__(self,CIF,nombre_empresa,ID,nombre,estado,facturable,jefe_pr,fecha_in,fecha_fin):
        super().__init__(CIF,nombre_empresa)
        self.__ID_pr=ID
        self.__nombre=nombre
        self.__estado=estado
        self.__facturable=facturable
        self.__jefe_pr=jefe_pr
        self.__fecha_in=fecha_in
        self.__fecha_fin=fecha_fin
    
    def __str__(self):
        return f'Datos del proyecto:\nEmpresa: {self._nombre_empresa}\nProyecto: {self.__nombre}\nEstado del proyecto: {self.__estado}\nFacturable: {self.__facturable}\nJefe del proyecto: {self.__jefe_pr}\nFecha de inicio: {self.__fecha_in}\nFecha fin: {self.__fecha_fin}\n'

    @property
    def ID(self):
        return self.__ID_pr
    @ID.setter
    def ID(self,nuevo_ID):
        self.__ID_pr=nuevo_ID
    @ID.deleter
    def ID(self):
        del self.__ID_pr

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
        return self.__facturable
    @facturable.setter
    def facturable(self,nuevo_facturable):
        self.__facturable=nuevo_facturable
    @facturable.deleter
    def facturable(self):
        del self.__facturable

    @property
    def jefe_pr(self):
        return self.__jefe_pr
    @jefe_pr.setter
    def jefe_pr(self,nuevo_jefe):
        self.__jefe_pr=nuevo_jefe
    @jefe_pr.deleter
    def jefe_pr(self):
        del self.__jefe_pr

    @property
    def fecha_in(self):
        return self.__fecha_in
    @fecha_in.setter
    def fecha_in(self,nueva_fecha):
        self.__fecha_in=nueva_fecha
    @fecha_in.deleter
    def fecha_in(self):
        del self.__fecha_in

    @property
    def fecha_fin(self):
        return self.__fecha_fin
    @fecha_fin.setter
    def fecha_fin(self,nueva_fecha):
        self.__fecha_fin=nueva_fecha
    @fecha_fin.deleter
    def fecha_fin(self):
        del self.__fecha_fin
