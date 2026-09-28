from types import MappingProxyType
from modelos.barra import Barra
from modelos.carga import Carga
from modelos.generador import Generador
from modelos.linea_transmision import LineaTransmision

class SistemaPotencia:
    """Clase gestora que administra la topología y elementos de la red."""
    def __init__(self):
        self.__generadores = {}
        self.__cargas = {}
        self.__lineas = {}
        self.__barras = {}

    @property
    def generadores(self):
        return MappingProxyType(self.__generadores)  ## para dejar solo lectura, no se puede modificar desde afuera
    @property
    def cargas(self):
        return MappingProxyType(self.__cargas)
    @property
    def lineas(self):
        return MappingProxyType(self.__lineas)
    @property
    def barras(self):
        return MappingProxyType(self.__barras)

    def _verificar_barra_registrada(self, barra):
        if self.__barras.get(barra.id_elemento) is not barra:
            raise ValueError(
                f"La barra {barra.id_elemento!r} no está registrada en el "
                "sistema. Agréguela antes con agregar_barra().")

    def agregar_generador(self, generador):
        if not isinstance(generador, Generador):
            raise TypeError("Se esperaba un objeto de la clase Generador.")
        if generador.id_elemento in self.__generadores:
            raise ValueError(f"Ya existe un generador con ID {generador.id_elemento}.")
        self._verificar_barra_registrada(generador.barra)
        self.__generadores[generador.id_elemento] = generador

    def agregar_carga(self, carga):
        if not isinstance(carga, Carga):
            raise TypeError("Se esperaba un objeto de la clase Carga.")
        if carga.id_elemento in self.cargas:
            raise ValueError(f"Ya existe una carga con ID {carga.id_elemento}.")
        self._verificar_barra_registrada(carga.barra)
        self.__cargas[carga.id_elemento] = carga

    def agregar_linea(self, linea):
        if not isinstance(linea, LineaTransmision):
            raise TypeError("Se esperaba un objeto de la clase LineaTransmision.")
        if linea.id_elemento in self.lineas:
            raise ValueError(f"Ya existe una línea con ID {linea.id_elemento}.")
        self._verificar_barra_registrada(linea.barra_origen)
        self._verificar_barra_registrada(linea.barra_destino)
        self.__lineas[linea.id_elemento] = linea
        
    def agregar_barra(self, barra):
        if not isinstance(barra, Barra):
            raise TypeError("Se esperaba un objeto de la clase Barra.")
        if barra.id_elemento in self.barras:
            raise ValueError(f"Ya existe una barra con ID {barra.id_elemento}.")
        self.__barras[barra.id_elemento] = barra
 
    def demanda_total(self):
        return sum(c.demanda_activa for c in self.__cargas.values())
 
    def capacidad_total(self):
        return sum(g.potencia_maxima for g in self.__generadores.values())
 
    def resumen(self):
        elementos = [
            *self.__barras.values(),
            *self.__generadores.values(),
            *self.__cargas.values(),
            *self.__lineas.values(),
        ]
        return "\n".join(e.resumen() for e in elementos)
 
    def despacho_economico(self):
        """Asigna la potencia despachada de cada generador.
 
        Ordenará los generadores por costo operativo (de menor a mayor) y
        los despachará hasta cubrir ``demanda_total()``.
 
        Raises:
            NotImplementedError: se implementa en el Hito 2.
        """
        raise NotImplementedError("Se implementará en el Hito 2.")
 
    def construir_ybus(self):
        """Ensambla la matriz de admitancia nodal (Ybus) de la red.
 
        Raises:
            NotImplementedError: se implementa en el Hito 3.
        """
        raise NotImplementedError("Se implementará en el Hito 3.")
 
    def resolver_flujo(self, inyecciones):
        """Resuelve Y · V = I y retorna el voltaje de cada barra.
 
        Args:
            inyecciones: inyección de corriente de cada barra.
 
        Raises:
            NotImplementedError: se implementa en el Hito 3.
        """
        raise NotImplementedError("Se implementará en el Hito 3.")