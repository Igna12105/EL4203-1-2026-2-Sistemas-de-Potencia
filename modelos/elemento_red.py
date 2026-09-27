class ElementoRed:
    """Superclase base para los elementos lógicos del sistema eléctrico."""
    def __init__(self, id_elemento, nombre):
        self.id_elemento = id_elemento
        self.nombre = nombre