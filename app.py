from flask import Flask, request

app = Flask(__name__)


# Ruta principal: muestra el formulario
@app.route("/")
def inicio():
    # Creamos el formulario HTML básico
    formulario_html = """
    <h2>Formulario de Registro</h2>
    <form action="/enviar" method="POST">
        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre" required><br><br>
        
        <label for="edad">Edad:</label><br>
        <input type="number" id="edad" name="edad" required><br><br>
        
        <input type="submit" value="Enviar">
    </form>
    """
    return formulario_html


# Ruta que recibe los datos del formulario (Método POST)
@app.route("/enviar", methods=["POST"])
def enviar():
    # Obtenemos los datos enviados desde el formulario
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")

    # Mostramos el resultado
    return f"<h3>¡Datos recibidos con éxito!</h3><p>Nombre: {nombre}</p><p>Edad: {edad}</p><a href='/'>Volver</a>"


if __name__ == "__main__":
    app.run(debug=True)