from abc import ABC, abstractmethod
 
 
class ElementoRed(ABC):
    def __init__(self, id_elemento, nombre):
        self.__id_elemento = id_elemento
        self.nombre = nombre
 
    @property
    def id_elemento(self):
        return self.__id_elemento
 
    @property
    def nombre(self):
        return self.__nombre
 
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        self.__nombre = valor
 
    @abstractmethod
    def resumen(self):
        """Retorna una descripción de una línea del elemento."""
 
    def __str__(self):
        """Representación legible: delega en ``resumen()``."""
        return self.resumen()
 
    def __repr__(self):
        """Representación técnica común a todos los elementos."""
        return (f"{type(self).__name__}(id={self.id_elemento}, "
                f"nombre={self.nombre})")
 