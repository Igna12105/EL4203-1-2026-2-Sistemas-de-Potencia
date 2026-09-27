from modelos.generador import Generador
from modelos.carga import Carga
from gestores.sistema_potencia import SistemaPotencia

def main():
    # Iniciar el gestor
    red_nacional = SistemaPotencia()

    # Crear elementos respetando la herencia y paso de parámetros, puse esos valores
    # arbitrarios para la demostración, pero podrían ser cualquier cosa (fran)
    gen_1 = Generador(id_elemento=1, nombre="Central Colbún", potencia_maxima=500.0, costo_operativo=25.5)
    carga_1 = Carga(id_elemento=2, nombre="Consumo Santiago", demanda_activa=350.0)

    # Agregar a la topología
    red_nacional.agregar_generador(gen_1)
    red_nacional.agregar_carga(carga_1)

    print(f"[{gen_1.nombre}] Límite máximo operativo: {gen_1.potencia_maxima} MW")

    # Demostración del encapsulamiento y validación
    try:
        gen_1.potencia_despachada = 300.0 # Funciona
        print(f"[{gen_1.nombre}] Despacho exitoso: {gen_1.potencia_despachada} MW")
        
        gen_1.potencia_despachada = 600.0 # Esto activará el error controlado
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()