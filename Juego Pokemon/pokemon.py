
import random


class Pokemon:
    ID = []
    salud_max = 100
    salud_min = 0
    ataque_max = 10
    ataque_min = 1
    defensa_max = 10
    defensa_min = 1
    tipos_arma = ["Puñetazo", "Patada", "Codazo", "Cabezazo"]

    def __init__(self, ID,nombre,tipo_arma,puntos_salud,indice_ataque,indice_defensa):
        self.ID = ID
        self.nombre = nombre
        self.tipo_arma = tipo_arma
        self.puntos_salud = puntos_salud
        self.indice_ataque = indice_ataque
        self.indice_defensa = indice_defensa


    def enum_arma(self):
        return list(enumerate(self.tipos_arma))






