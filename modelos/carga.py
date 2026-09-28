from .elemento_red import ElementoRed
from .barra import Barra

class Carga(ElementoRed):
    """Clase que representa una carga o demanda del sistema."""
    def __init__(self, id_elemento, nombre, demanda_activa, barra):
        super().__init__(id_elemento, nombre)
        
        self.demanda_activa = demanda_activa
        self.barra = barra
    @property
    def demanda_activa(self):
        return self.__demanda_activa
    @property
    def barra(self):
        return self.__barra
    
    @demanda_activa.setter
    def demanda_activa(self, valor):
        if valor < 0:
            raise ValueError("La demanda activa no puede ser negativa.")
        self.__demanda_activa = valor
    @barra.setter
    def barra(self, valor):
        if not isinstance(valor, Barra):
            raise TypeError("barra debe ser un objeto de la clase Barra.")
        self.__barra = valor
    def resumen(self):
        """Descripción de una línea de la carga."""
        return (f"Carga {self.id_elemento} ({self.nombre}) en "
                f"{self.barra.id_elemento}: {self.demanda_activa} MW")