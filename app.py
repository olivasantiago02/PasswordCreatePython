from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    longitud = int(request.form['longitud'])
    contrasena_generada = generar_contrasena(longitud)
    return render_template('index.html', contrasena=contrasena_generada)

if __name__ == '__main__':
    app.run(debug=True)
