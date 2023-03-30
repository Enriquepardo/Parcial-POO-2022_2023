import random 


class Pokemon:
    pokemon_ids = []

    def __init__(self, id, nombre, arma,puntos_salud,indice_ataque,indice_defensa):
        if not isinstance(id, int):
            raise TypeError('ID tiene que ser un numero entero')
        if id in Pokemon.pokemon_ids:
            raise ValueError('ID ya existe para otro pokemon')
        if not isinstance(nombre, str):
            raise TypeError('El nombre debe ser una cadena de caracteres')
        if not isinstance(arma, str):
            raise TypeError('El arma debe ser una cadena de caractere')
        if not isinstance(puntos_salud, int):
            raise TypeError('Los puntos de salud deben ser un numero entero')
        if not isinstance(indice_ataque, int):
            raise TypeError('El indice de ataque debe ser un numero entero')
        if not isinstance(indice_defensa, int):
            raise TypeError('El indice de defensa debe ser un numero entero')

        self.__id = id
        self.__nombre = nombre
        self.__arma = arma
        self.__puntos_salud = puntos_salud
        self.__indice_ataque = indice_ataque
        self.__indice_defensa = indice_defensa

        Pokemon.pokemon_ids.append(id)


    def __str__(self):
        return ' Pokemon ID {} con nombre {} usa de arma {} y tiene {} puntos de salud' .format(self.__id, self.__nombre, self.__arma, self.__puntos_salud)
    
    def __del__(self):
        Pokemon.pokemon_ids.remove(self.__id)


    def get_id(self):
        return self.__id
    
    def get_nombre(self):    
        return self.__nombre
    
    def get_arma(self):
        return self.__arma
    
    def get_puntos_salud(self):
        return self.__puntos_salud
    
    def get_indice_ataque(self):
        return self.__indice_ataque
    
    def get_indice_defensa(self):
        return self.__indice_defensa

    # solo se pueden modificar los puntos de salud
    def set_puntos_salud(self, puntos_salud):
        if not isinstance(puntos_salud, int):
            raise TypeError('Los puntos de salud deben ser un numero entero')
        self.__puntos_salud = puntos_salud


    def is_alive(self):
        if self.__puntos_salud > 0:
            return True
        else:
            return False
    
    def pelea_atacar(self, pokemon_objetivo):
        if not isinstance(pokemon_objetivo, Pokemon):
            raise TypeError('El pokemon objetivo debe ser una instancia de la clase Pokemon')
        else:
            if pokemon_objetivo.is_alive():
                pokemon_objetivo.pelea_defender(self.__indice_ataque)

    def pelea_defender(self, puntos_daño):
    
        if self.__indice_defensa > puntos_daño:
            return 0
        else:
            self.__puntos_salud -= (puntos_daño - self.__indice_defensa)
            return True


