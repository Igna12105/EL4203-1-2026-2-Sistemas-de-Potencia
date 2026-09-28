from .elemento_red import ElementoRed
from .barra import Barra

class LineaTransmision(ElementoRed):
    """Clase que representa una línea de transmisión entre nodos."""
    def __init__(self, id_elemento, nombre, barra_origen, barra_destino, reactancia):
        super().__init__(id_elemento, nombre)
        self.barra_origen = barra_origen
        self.barra_destino = barra_destino
        if barra_origen.id_elemento == barra_destino.id_elemento:
            raise ValueError("Origen y destino deben ser barras distintas.")
        self.reactancia = reactancia
    @property
    def barra_origen(self):
        return self.__barra_origen
    @property
    def barra_destino(self):
        return self.__barra_destino
    @property
    def reactancia(self):
        return self.__reactancia
    @barra_origen.setter
    def barra_origen(self, valor):
        if not isinstance(valor, Barra):
            raise TypeError("barra_origen debe ser un objeto de la clase Barra.")
        self.__barra_origen = valor
    @barra_destino.setter
    def barra_destino(self, valor):
        if not isinstance(valor, Barra):
            raise TypeError("barra_destino debe ser un objeto de la clase Barra.")
        self.__barra_destino = valor
    @reactancia.setter
    def reactancia(self, valor):
        if valor <= 0:
            raise ValueError("La reactancia debe ser mayor que cero.")
        self.__reactancia = valor
    def resumen(self):
        """Descripción de una línea de la línea de transmisión."""
        return (f"Línea {self.id_elemento} ({self.nombre}): "
                f"{self.barra_origen.id_elemento} -> "
                f"{self.barra_destino.id_elemento}, X = {self.reactancia}")