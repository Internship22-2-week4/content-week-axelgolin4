from Galeria import Galeria


class Foto(Galeria):
    
    def __init__(self,nombre, fecha, uri):
        self.nombre: str = nombre
        self.fecha: str = fecha
        self.uri: str = uri

    def agregar(self):
        pass