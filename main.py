from pokemon import Pokemon, PokemonElectrico, PokemonAgua, PokemonTierra
from entrenadores import *
from tipos_armas import *
import csv


# EOF
def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    
    
    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    entrenador1 = Entrenador("Entrenador 1", 'coach_1_pokemons.csv')
    entrenador2 = Entrenador("Entrenador 2", 'coach_2_pokemons.csv')
    # funcion main del juego
    combat(entrenador1, entrenador2)
                    
    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
