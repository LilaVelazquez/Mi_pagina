
# =========================================================
# PROYECTO TURÍSTICO - SAN FELIPE DEL PROGRESO
# DESARROLLADO CON PYTHON Y FLASK
# =========================================================

# Importamos Flask y requests
# Flask sirve para crear páginas web con Python
from flask import Flask, render_template, abort
import requests

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
        "descripcion2": """
        Es uno de los espacios culturales más
        representativos del municipio de San Felipe del Progreso. Fue creado
        para preservar la identidad, las tradiciones y la riqueza cultural
        del pueblo mazahua.

        Durante todo el año recibe visitantes interesados en conocer su
        arquitectura, monumentos y ceremonias tradicionales. Además,
        es sede de eventos culturales, deportivos y festividades que
        fortalecen el patrimonio indígena de la región.
        """,

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
         "descripcion2": """ 
        La prensa de Tepetitlán está ubicada en el municipio de San Felipe de Progreso, 
        el cual se ubica al noroeste del Estado de México.
        
        Puedes ingresar por San Felipe del Progreso – Ixtlahuaca, desviación a Santa Cruz Mextepec, 
        por la carretera San Felipe – Carmona km 2, desviación a Estutempan. El lugar es muy bello, 
        pero no es apto para nadar, así que para evitar accidentes no debes sumergirte en sus aguas, 
        solo está permitido el pasar por algunas orillas o en las lanchas. 
        
        Si deseas pasar un bello día con tu familia, este lugar puede ser el indicado para tu familia, 
        amigos o pareja, la gente que se encarga de supervisar área es muy amable. """,
        
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
        "descripcion2": """
         La cascada Salto de tigre un paraíso natural, ubicado en carretera Santa Ana Nichi, 
         Municipio de San Felipe del Progreso. llegar es muy fácil hay que tomar una unidad del municipio 
         de san Felipe del progreso a la comunidad de Santa Ana Nichi. 
        
          Al pasar por una de las curvas del barrio del tigre aparece un pequeño paraíso rodeado de cerros, 
         campos y hasta una encantadora presa, un riachuelo se trasforma en una belleza de más de 20 metros de 
         altura rodeada de encinos y briza fresca parece sacado de una postal, es una de las más hermosas del 
         Estado de México. """,   
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
eventos = [

    {
        "nombre": "Feria de Nuestro Padre Jesús",
        "fecha": "Enero",
        "lugar": "Plaza Principal",
        "descripcion": "Danzas tradicionales, música, gastronomía local y una peculiar ofrenda de palomitas de maíz "
        "que los pobladores llevan al santo patrono desde hace más de 300 años"
        
    },

    {
        "nombre": "Rodadas turísticas",
        "fecha": "Enero",
        "lugar": "Centro ceremonial Mazahua y Presa de Tepetilán",
        "descripcion": "Eventos promovidos para impulsar el turismo que convocan a cientos de motociclistas"
        "y ciclistas para recorrer el Centro Ceremonial Mazahua y la presa de Tepetitlán."
        
    },

    {
        "nombre": "Festival Cultural Mazahua",
        "fecha": "15 al 18 de agosto",
        "lugar": "Centro Ceremonial Mazahua",
        "descripcion": "Evento con danzas, música tradicional, gastronomía y artesanías."
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

@app.route("/eventos")
def eventos_page():

    return render_template(
        "eventos.html",
        eventos=eventos
    )

def obtener_clima(latitud, longitud):

        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitud}"
        f"&longitude={longitud}"
        "&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
    )

    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()

        datos = respuesta.json()
        print("Respuesta de Open-Meteo:", datos)

        return datos.get("current")

    except Exception as e:
        print("Error al obtener el clima:", e)
        return None
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
    lugar_encontrado = None
    for lugar in lugares:
        if lugar["id"] == id_lugar:
            lugar_encontrado = lugar
            break
    if lugar_encontrado is None:
        abort(404)
    clima = obtener_clima(
        lugar_encontrado["latitud"],
        lugar_encontrado["longitud"]
    )
    return render_template(
        "detalle.html",
        lugar=lugar_encontrado,
        clima=clima
    )
    
# =========================================================
# INICIAR SERVIDOR
# =========================================================
# debug=True actualiza la página automáticamente
# cuando guardas cambios

if __name__ == "__main__":
    app.run(debug=True)
