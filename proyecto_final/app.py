from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio = 9000
        total_sin_descuento = cantidad * precio

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)
        return f'''
            <h1>Resultado</h1>
            Nombre: {nombre}<br>
            Total sin descuento: {total_sin_descuento}<br>
            Total con descuento: {total_con_descuento}
        '''
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario in usuarios and usuarios[usuario] == contraseña:
            if usuario == 'juan':
                return "Bienvenido administrador juan"
            else:
                return "Bienvenido usuario pepe"
        return "Usuario o contraseña incorrectos"
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
