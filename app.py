
# =========================================================
# PROYECTO TURÍSTICO - SAN FELIPE DEL PROGRESO
# DESARROLLADO CON PYTHON Y FLASK
# =========================================================

# Importamos Flask
# Flask sirve para crear páginas web con Python
from flask import Flask, render_template, abort

# Creamos nuestra aplicación Flask
app = Flask(__name__)

# =========================================================
# LISTA DE LUGARES TURÍSTICOS
# =========================================================
# Aquí guardamos información de cada lugar
# Usamos listas y diccionarios (Python básico)

lugares = [

    # Lugar turístico 1
    {
        # ID único del lugar
        "id": 1,

        # Nombre del lugar
        "nombre": "Centro Ceremonial Mazahua",

        # Imagen del lugar
        "imagen": "https://th.bing.com/th/id/OIP.MQq949MhqLSB4aorcf4YGwHaEo?w=297&h=185&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",

        # Descripción corta
        "descripcion": "Espacio cultural que representa la identidad mazahua.",

        # Ubicación
        "ubicacion": "Santa Ana Nichi, San Felipe del Progreso, Estado de México",
        
        "latitud": 19.572714,
        "longitud": -99.962900,
        
        
        # Lista de actividades
        "actividades": [
            "Senderismo, picnic, eventos",
            "Exhibidor de herbívoros, salón de artesanías y salón de rituales",
            "Servicios:Estacionamiento, caseta de administración, vigilancia, palapas y sanitarios"
        ]
    },

    # Lugar turístico 2
    {
        "id": 2,
        "nombre": "Presa de Tepetitlán",
        "imagen": "https://th.bing.com/th/id/OIP.9sy6JlYLRwaWHs8bKyvvMQHaEK?w=317&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "descripcion": "Lugar natural ideal para descansar y disfrutar paisajes.",
        "ubicacion": "San Antonio Mextepec, San Felipe del Progreso, Estado de México",
        "latitud": 19.661047,
        "longitud": -99.961116,
        
        "actividades": [
            "Paseos en lancha, Convivencia familiar",
            "Pesca reacreativa, observación de aves",
            "Fotografía de paisajes, caminar"
        ]
    },

    # Lugar turístico 3
    {
        "id": 3,
        "nombre": "Cascada del salto del tigre",
        "imagen": "https://th.bing.com/th/id/OIP.eLxz1wg27J8-N6jBZSB2XAHaEi?w=291&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "descripcion": "Caída de agua escondida entre el cerro del Tigre y cañadas boscosas en San Felipe del Progreso",
        "ubicacion": "Villa de Santa Ana Nichi, San Felipe del Progreso, Estado de México",
        "latitud": 19.588630,
        "longitud": -99.956051,  
        "actividades": [
            "Conexión con la naturaleza",
            "Senderismo",
            "Ecoturismo, exploración cultural"
        ]
    }
]

# =========================================================
# RUTA PRINCIPAL
# =========================================================
# Cuando el usuario entra a:
# http://127.0.0.1:5000
# Flask mostrará index.html

@app.route("/")
def inicio():

    # render_template sirve para abrir un archivo HTML
    # También enviamos la lista de lugares
    return render_template("index.html", lugares=lugares)


# =========================================================
# RUTA DE DETALLE
# =========================================================
# Esta ruta se usa cuando el usuario da clic
# en un lugar turístico

# Ejemplo:
# /lugar/1
# /lugar/2

@app.route("/lugar/<int:id_lugar>")
def detalle_lugar(id_lugar):

    # Variable vacía
    lugar_encontrado = None

    # Recorremos todos los lugares
    for lugar in lugares:

        # Verificamos si el ID coincide
        if lugar["id"] == id_lugar:

            # Guardamos el lugar encontrado
            lugar_encontrado = lugar

            # Rompemos el ciclo
            break

    # Si no existe el lugar
    # mostramos error 404
    if lugar_encontrado is None:
        abort(404)

    # Abrimos detalle.html
    # y enviamos la información del lugar
    return render_template(
        "detalle.html",
        lugar=lugar_encontrado
    )


# =========================================================
# INICIAR SERVIDOR
# =========================================================
# debug=True actualiza la página automáticamente
# cuando guardas cambios

if __name__ == "__main__":
    app.run(debug=True)
