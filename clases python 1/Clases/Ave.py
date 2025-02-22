from Clases.Animal import Animal
class Ave(Animal):
    def __init__(self,nombre,peso,año_nacimiento,propietario):
        super().__init__(nombre,peso)
        self.año_nacimiento = año_nacimiento
        self.propietario = propietario

    def imprimiraño_nacimiento(self):    
        return f'El animal nació en el año : {self.año_nacimiento} y su propietario es : {self.propietario}'

    def calcular_edad(self, año_actual):
        
        edad = año_actual - self.año_nacimiento
        if edad >= 5:
            return f'{self.nombre} es MAYOR DE EDAD (Edad: {edad} años)'
        else:
            return f'{self.nombre} es MENOR DE EDAD (Edad: {edad} años)'
        