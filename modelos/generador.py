from .elemento_red import ElementoRed

class Generador(ElementoRed):
    """Clase que representa un generador, heredando de ElementoRed."""
    def __init__(self, id_elemento, nombre, potencia_maxima, costo_operativo):
        super().__init__(id_elemento, nombre)
        # Atributos privados para proteger matemáticamente los límites físicos
        self.__potencia_maxima = potencia_maxima
        self.__costo_operativo = costo_operativo
        self.__potencia_despachada = 0.0

    # Getters para acceder de forma segura a los valores, el property permite encapsular
    #  la lógica de acceso y validación, por eso lo puse (fran)
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