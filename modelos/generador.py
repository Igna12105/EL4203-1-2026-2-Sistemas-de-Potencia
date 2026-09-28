from .elemento_red import ElementoRed
from .barra import Barra

class Generador(ElementoRed):
    """Clase que representa un generador, heredando de ElementoRed."""
    def __init__(self, id_elemento, nombre, potencia_maxima, costo_operativo, barra):
        super().__init__(id_elemento, nombre)
        # Atributos privados para proteger matemáticamente los límites físicos
        self.__potencia_despachada = 0.0
        self.potencia_maxima = potencia_maxima
        self.costo_operativo = costo_operativo
        self.barra = barra
        

    # Getters para acceder de forma segura a los valores, el property permite encapsular
    #  la lógica de acceso y validación, por eso lo puse
    @property
    def potencia_maxima(self):
        return self.__potencia_maxima

    @property
    def costo_operativo(self):
        return self.__costo_operativo

    @property
    def potencia_despachada(self):
        return self.__potencia_despachada

    # Setter con validación para no despachar más energía de la posible
    # la misma idea con el setter y el property (fran)
    @potencia_despachada.setter
    def potencia_despachada(self, valor):
        if valor < 0:
            raise ValueError("La potencia despachada no puede ser negativa.")
        if valor > self.__potencia_maxima:
            raise ValueError(f"Error de validación: Se intentó despachar {valor} MW, superando la Potencia Máxima de {self.__potencia_maxima} MW.")
        self.__potencia_despachada = valor

    @costo_operativo.setter
    def costo_operativo(self, valor):
        if valor < 0:
            raise ValueError("El costo operativo debe ser no negativo.")
        self.__costo_operativo =  valor

    @potencia_maxima.setter
    def potencia_maxima(self, valor):
        if valor <= 0:
            raise ValueError("La potencia máxima debe ser mayor a cero")
        if valor < self.__potencia_despachada:
            raise ValueError(f"La potencia máxima {valor} MW no puede ser menor que la potencia despachada actual {self.__potencia_despachada} MW.")
        self.__potencia_maxima =  valor

    @property
    def barra(self):
        return self.__barra
    @barra.setter
    def barra(self, valor):
        if not isinstance(valor, Barra):
            raise TypeError("barra debe ser un objeto de la clase Barra.")
        self.__barra = valor
    def resumen(self):
        """Descripción de una línea del generador."""
        return (f"Generador {self.id_elemento} ({self.nombre}) en "
                f"{self.barra.id_elemento}: {self.potencia_despachada} / "
                f"{self.potencia_maxima} MW, "
                f"{self.costo_operativo} USD/MWh")