
from Autor import Autor

class Obra():
    
    def __init__(self, tipo, valor, autor, galeria):
        self.tipo: str = tipo
        self.valor: str = valor
        self.autor: Autor = autor
        self.galeria = galeria
  