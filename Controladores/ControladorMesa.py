from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todas las Mesas")
        unaMesa={
            "_id":"123",
            "numero":"01",
            "cantidad_inscritos":"50"
        }
        return[unaMesa]

    def create(self,infoMesa):
        print("Crear una Mesa")
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def show(self,id):
        print("Mostrando una Mesa con id ", id)
        laMesa = {
            "_id":id,
            "numero":"01",
            "cantidad_inscritos":"50"
        }
        return laMesa

    def update(self, id, infoMesa):
        print("Actualizando Mesa con id ", id)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def delete(self, id):
        print("Elimiando Mesa con id ", id)
        return {"deleted_count":1}