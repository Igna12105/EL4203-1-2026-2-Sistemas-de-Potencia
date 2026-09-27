from .elemento_red import ElementoRed

class Carga(ElementoRed):
    """Clase que representa una carga o demanda del sistema."""
    def __init__(self, id_elemento, nombre, demanda_activa):
        super().__init__(id_elemento, nombre)
        self.demanda_activa = demanda_activa