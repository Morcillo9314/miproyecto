from Modelos.Candidato import  Candidato

class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    def index(self):
        print("Listar todos los Candidatos")
        unCandidato = {
            "cedula":"1234",
            "nombre":"Juan",
            "apellido":"Rubio",
            "numero_resolucion":"12"
        }
        return[unCandidato]

    def create(self,infoCandidato):
        print("Crear un Candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def show(self,id):
        print("Mostrando un Candidato con id ", id)
        elCandidato = {
            "_id":id,
            "cedula":"1234",
            "nombre":"Juan",
            "apellido":"Rubio",
            "numero_resolucion":"12"
        }
        return elCandidato

    def update(self, id, infoCandidato):
        print("Actualizando Candidato con id ", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, id):
        print("Elimiando Candidato con id ", id)
        return {"deleted_count":1}