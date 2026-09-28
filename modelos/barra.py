
from .elemento_red import ElementoRed


class Barra(ElementoRed):
    """Barra (nodo) de la red donde se conectan generadores, cargas y
    extremos de líneas de transmisión
    """
    def __init__(self, id_elemento, nombre, voltaje=1.0):
        super().__init__(id_elemento, nombre)
        self.voltaje = voltaje 

    @property
    def voltaje(self):
        return self.__voltaje

    @voltaje.setter
    def voltaje(self, valor):
        if valor < 0:
            raise ValueError("El voltaje de una barra no puede ser negativo.")
        self.__voltaje = float(valor)
    def resumen(self):
        """Descripción de una línea de la barra."""
        return (f"Barra {self.id_elemento} ({self.nombre}): "
                f"{self.voltaje} p.u.")