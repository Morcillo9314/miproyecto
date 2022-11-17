from Modelos.Resultado import Resultado

class ControladorResultado():
    def __init__(self):
        print("Creando Controlador Resultado")

    def index(self):
        print("Listar todas los Resultados")
        unResultado={
            "_id":"10323",
            "numero_mesa":"01",
            "idcandidato":"wr45"
        }
        return[unResultado]

    def create(self,infoResultado):
        print("Crear un Partido")
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def show(self,id):
        print("Mostrando un Resultado con id ", id)
        elResultado = {
            "_id":id,
            "numero_mesa":"01",
            "idcandidato":"wr45"
        }
        return elResultado

    def update(self, id, infoResultado):
        print("Actualizando Resultado con id ", id)
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def delete(self, id):
        print("Elimiando Resultado con id ", id)
        return {"deleted_count":1}