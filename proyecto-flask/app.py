from flask import Flask, render_template
import requests
import json
from configuracion import usuario, clave

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/Persona")
def personas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/Persona/",
            auth=(usuario, clave))
    personas = json.loads(r.content)['results']
    numero_personas = json.loads(r.content)['count']
    return render_template("listar_personas.html", personas=personas,
    numero_personas=numero_personas)

@app.route("/Barrio")
def barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/Barrio/",
            auth=(usuario, clave))
    barrios = json.loads(r.content)['results']
    numero_barrios = json.loads(r.content)['count']
    return render_template("listar_barrios.html", barrios=barrios,
    numero_barrios=numero_barrios)

@app.route("/localComida")
def localesCo():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/localComida/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("listar_locales_comida.html", datos=datos,
    numero=numero)

@app.route("/localRepuestos")
def localesRe():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/localRepuestos/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("listar_locales_repuestos.html", datos=datos,
    numero=numero)