# EL4203 - Programación Avanzada

## Proyecto Semestral: Sistemas de Potencia (Opción A)

Universidad de Chile — Facultad de Ciencias Físicas y Matemáticas
Departamento de Ingeniería Eléctrica

## Descripción

Este repositorio contiene el desarrollo del proyecto semestral del curso
EL4203, correspondiente a la Opción A del catálogo: un simulador de una red
eléctrica de potencia. El objetivo del proyecto es que el software sea
capaz de realizar, en etapas sucesivas, el despacho económico de
generadores y la resolución del flujo de potencia simplificado (DC) de la
red, a partir de una arquitectura orientada a objetos que represente los
elementos físicos del sistema.

El desarrollo se organiza en tres hitos, de acuerdo con la pauta del curso.
Actualmente el repositorio se encuentra en la etapa correspondiente al
Hito 1, en la que se definió la arquitectura del software y se construyó
el esqueleto del código.

## Estructura del repositorio

El paquete `modelos` agrupa las clases que representan los elementos
físicos de la red (`ElementoRed` y sus subclases), mientras que `gestores`
agrupa las clases encargadas de administrar la topología y la operación
del sistema, actualmente representada por `SistemaPotencia`.

## Arquitectura orientada a objetos

Para esta primera etapa, se diseñó una jerarquía de clases que abstrae los
elementos físicos del sistema eléctrico a entidades lógicas:

- **`ElementoRed`**: superclase abstracta de la que heredan todos los
  elementos de la red. Define los atributos comunes (`id_elemento`,
  `nombre`) y obliga a cada subclase a implementar su propio método
  `resumen()`.
- **`Barra`**: representa un nodo de la red, donde se conectan
  generadores, cargas y líneas de transmisión.
- **`Generador`**: modela un generador, con su potencia máxima, costo
  operativo y potencia despachada. Estos atributos se protegen mediante
  encapsulamiento, de forma que no sea posible despachar más potencia de
  la físicamente disponible.
- **`Carga`**: representa una demanda del sistema conectada a una barra.
- **`LineaTransmision`**: conecta dos barras de la red a través de su
  reactancia.
- **`SistemaPotencia`**: clase gestora que administra la topología
  completa, validando que cada elemento agregado sea del tipo correcto,
  que no existan identificadores duplicados y que las barras referenciadas
  estén previamente registradas en el sistema.

El diagrama de clases UML correspondiente a esta arquitectura se encuentra
en el informe entregado para este hito.

## Estado del proyecto

- **Hito 1 (actual)**: arquitectura orientada a objetos, encapsulamiento
  de los límites físicos del sistema y esqueleto funcional del código.
  Los métodos `despacho_economico()`, `construir_ybus()` y
  `resolver_flujo()` se encuentran declarados, pero su implementación
  corresponde a etapas posteriores del proyecto.
- **Hito 2 (pendiente)**: implementación del algoritmo de ordenamiento
  para el despacho económico, uso de estructuras Hash para el acceso a las
  barras y análisis de complejidad Big-O.
- **Hito 3 (pendiente)**: vectorización con NumPy para el ensamblaje de la
  matriz de admitancia nodal y la resolución del flujo de potencia, junto
  con la generación de gráficos bajo el estándar IEEE.

## Ejecución

El archivo `main.py` construye una red de ejemplo y permite verificar el
correcto funcionamiento de las clases y sus validaciones. Para ejecutarlo,
basta con correr, desde la raíz del repositorio:

```
python main.py
```
