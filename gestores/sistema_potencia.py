class SistemaPotencia:
    """Clase gestora que administra la topología y elementos de la red."""
    def __init__(self):
        self.generadores = []
        self.cargas = []
        self.lineas = []

    def agregar_generador(self, generador):
        self.generadores.append(generador)

    def agregar_carga(self, carga):
        self.cargas.append(carga)

    def agregar_linea(self, linea):
        self.lineas.append(linea)