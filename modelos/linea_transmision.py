from .elemento_red import ElementoRed

class LineaTransmision(ElementoRed):
    """Clase que representa una línea de transmisión entre nodos."""
    def __init__(self, id_elemento, nombre, nodo_origen, nodo_destino, reactancia):
        super().__init__(id_elemento, nombre)
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.reactancia = reactancia