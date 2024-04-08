import string

def calcular_tiempo_ejecucion(instrucciones, frecuencia):
    suma_ciclos = sum(instruccion[1] * instruccion[2] for instruccion in instrucciones)
    tiempo_ejecucion = suma_ciclos / frecuencia  # Convertir a microsegundos
    return tiempo_ejecucion

def calcular_frecuencia(instrucciones, tiempo_ejecucion):
    suma_ciclos = sum(instruccion[1] * instruccion[2] for instruccion in instrucciones)
    frecuencia = suma_ciclos / tiempo_ejecucion   # Convertir a segundos
    return frecuencia

def main():
    instrucciones = []
    num_instrucciones = int(input("Ingrese el número de instrucciones: "))

    for i in range(num_instrucciones):
        nombre_instruccion = string.ascii_uppercase[i]  # Generar nombres de instrucciones conforme al alfabeto
        ciclos = int(input("Ingrese el número de ciclos de la instrucción {}: ".format(nombre_instruccion)))
        repeticiones = int(input("Ingrese el número de repeticiones de la instrucción {}: ".format(nombre_instruccion)))
        instrucciones.append((nombre_instruccion, ciclos, repeticiones))

    print("Tabla de instrucciones:")
    print("Instrucción | Ciclos | Veces que se repite")
    for instruccion in instrucciones:
        print("{:<12} | {:<6} | {:<16}".format(*instruccion))

    opcion = input("\n¿Deseas calcular el tiempo de ejecución (T) o la frecuencia (F)? ").upper()

    if opcion == 'T':
        frecuencia = float(input("Ingresa la frecuencia en MHz: "))
        tiempo_total = calcular_tiempo_ejecucion(instrucciones, frecuencia)
        print("El tiempo de ejecución necesario para estas instrucciones es:", tiempo_total, "microsegundos")
    elif opcion == 'F':
        tiempo_ejecucion = float(input("Ingresa el tiempo de ejecución en microsegundos: "))
        frecuencia_calculada = calcular_frecuencia(instrucciones, tiempo_ejecucion)
        print("La frecuencia necesaria para ejecutar estas instrucciones es:", frecuencia_calculada, "MHz")
    else:
        print("Opción no válida. Por favor, ingresa 'T' para calcular el tiempo de ejecución o 'F' para calcular la frecuencia.")


if __name__ == "__main__":
    main()
