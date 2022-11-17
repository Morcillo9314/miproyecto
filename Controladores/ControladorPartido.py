from Modelos.Candidato import Candidato

class ControladorPartido():
    def __init__(self):
        print("Creando Controlador Partido")

    def index(self):
        print("Listar todas los Partidos")
        unPartido={
            "_id":"1023",
            "nombre":"Partido SuMadre",
            "slogan":"latuya"
        }
        return[unPartido]

    def create(self,infoPartido):
        print("Crear un Partido")
        elPartido = Paetido(infoPartido)
        return elPartido.__dict__

    def show(self,id):
        print("Mostrando un Partido con id ", id)
        elPartido = {
            "_id":id,
            "nombre":"Partido SuMadre",
            "slogan":"latuya"
        }
        return elPartido

    def update(self, id, infoCandidato):
        print("Actualizando Candidato con id ", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, id):
        print("Elimiando Candidato con id ", id)
        return {"deleted_count":1}