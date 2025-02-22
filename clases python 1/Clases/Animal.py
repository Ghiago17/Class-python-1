class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def imprimirnombre(self):
        return f'El nombre del animal es : {self.nombre} y su  Peso: {self.peso}'