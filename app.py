from flask import Flask, render_template, request, jsonify



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    if request.method == 'POST':
        tiempo = ""
        tiempo = request.form.get('tiempo')  # Obtener el valor de tiempo del formulario
        magnitud =request.form.get('magnitud_tiempo')
        return render_template('ejercicio1.html', tiempo=tiempo, magnitud_tiempo=magnitud)  # Pasar el valor de tiempo al template HTML
    else:
        return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.after_request
def deshabilitar_cache(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":
    app.run(debug=True)
