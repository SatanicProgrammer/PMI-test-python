# --------- Práctica dirigida Nro 2 - Módulo I Python ---------
# Alexander Burgos Ninatanta

# Problema 01

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = 'Peruana'

    def cumpleaños(self):
        self.edad += 1


persona_random = Persona('Chloe', 20)
persona_random.cumpleaños()
print(persona_random.edad)

