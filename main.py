from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorCandidato import ControladorCandidato

miControladorMesa = ControladorMesa()
micontroladorPartido = ControladorPartido()
micontroladorResultado = ControladorResultado()
micontroladorCandidato = ControladorCandidato()

##########Inicio Ruta CRUD Mesa###########

@app.route("/mesa",methods=['GET'])
def getMesa():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

##########Inicio Ruta CRUD Candidato###########

@app.route("/candidato",methods=['GET'])
def getCandidato():
    json = micontroladorCandidato.index()
    return jsonify(json)

@app.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = micontroladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    json = micontroladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = micontroladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json = micontroladorCandidato.delete(id)
    return jsonify(json)

##########Inicio Ruta CRUD Partido###########

@app.route("/partido",methods=['GET'])
def getPartido():
    json = micontroladorPartido.index()
    return jsonify(json)

@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = micontroladorPartido.create(data)
    return jsonify(json)

@app.route("/partido/<string:id>",methods=['GET'])
def getPartido(id):
    json = micontroladorPartido.show(id)
    return jsonify(json)

@app.route("/partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = micontroladorPartido.update(id,data)
    return jsonify(json)

@app.route("/partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json = micontroladorPartido.delete(id)
    return jsonify(json)

##########Inicio Ruta CRUD Resultado###########

@app.route("/resultado",methods=['GET'])
def getResultado():
    json = micontroladorResultado.index()
    return jsonify(json)

@app.route("/resultado",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json = micontroladorResultado.create(data)
    return jsonify(json)
@app.route("/resultado/<string:id>",methods=['GET'])
def getResultado(id):
    json = micontroladorResultado.show(id)
    return jsonify(json)
@app.route("/resultado/<string:id>",methods=['PUT'])
def modificarResltado(id):
    data = request.get_json()
    json = micontroladorResultado.update(id,data)
    return jsonify(json)
@app.route("/resultado/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    json = micontroladorResultado.delete(id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])