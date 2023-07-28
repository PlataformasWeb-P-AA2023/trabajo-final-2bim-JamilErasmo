from flask import Flask, render_template
import requests
import json
from configuracion import usuario, clave

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/listar_barrios")
def los_barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/listar_barrios/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("listar_barrios.html", datos=datos,
    numero=numero)


@app.route("/listar_personas")
def las_personas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/listar_personas/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("listar_personas.html", datos=datos,
    numero=numero)


@app.route("/listar_locales_comida")
def los_losLocalesComida():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/listar_locales_comida/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("listar_locales_comida.html", datos=datos,
    numero=numero)

@app.route("/listar_locales_repuestos")
def los_losLocalesRepuestos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/listar_locales_repuestos/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("listar_locales_repuestos.html", datos=datos,
    numero=numero)