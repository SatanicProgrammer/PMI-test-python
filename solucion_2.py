# --------- Práctica dirigida Nro 2 - Módulo I Python ---------
# Alexander Burgos Ninatanta

# Problema 02

class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo
        self.nacionalidad = 'Peruana'

    def cumpleaños(self):
        self.edad += 1

    def mostrarsaldo(self):
        return self.__saldo

    def darsaldo(self, saldofuera):
        self.__saldo = saldofuera


class Usuario(Persona):

    def transferencia(self, otra_persona, monto):
        if monto > self.mostrarsaldo():
            print('Saldo insuficiente.')
        else:
            self.darsaldo(self.mostrarsaldo() - monto)
            otra_persona.darsaldo(otra_persona.mostrarsaldo() + monto)


primera_persona = Usuario('Cris', 20, 400)
segunda_persona = Usuario('Rick', 22, 600)
primera_persona.transferencia(segunda_persona, 200)
print(primera_persona.mostrarsaldo())