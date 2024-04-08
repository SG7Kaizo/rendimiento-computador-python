from flask import Flask, render_template, request
# from calculos_Num_instrucciones import calcular_frecuencia, calcular_tiempo_ejecucion
import string

app = Flask(__name__)

def calcular_tiempo_ejecucion(instrucciones, frecuencia):
    suma_ciclos = sum(instruccion[1] * instruccion[2] for instruccion in instrucciones)
    tiempo_ejecucion = suma_ciclos / frecuencia  # Convertir a microsegundos
    return tiempo_ejecucion

def calcular_frecuencia(instrucciones, tiempo_ejecucion):
    suma_ciclos = sum(instruccion[1] * instruccion[2] for instruccion in instrucciones)
    frecuencia = suma_ciclos / tiempo_ejecucion   # Convertir a segundos
    return frecuencia

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

if __name__ == "__main__":
    app.run(debug=True)
