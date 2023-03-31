
import csv
from pokemon import Pokemon

class Entrenador:
    def __init__(self, name, csv_file):
        self.name = name
        self.pokemon_list = []
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                id, name, attack_name, attack_power, max_health, current_health = row
                pokemon = Pokemon(int(id), name, attack_name, int(attack_power), int(max_health), int(current_health))
                self.pokemon_list.append(pokemon)

    def get_pokemon_in_a_list_of_pokemons(self):
        print("Lista de Pokemons:")
        for i, pokemon in enumerate(self.pokemon_list):
            print(f"{i + 1}. {pokemon}")
        choice = int(input("Elige un Pokemon (1-3): "))
        return self.pokemon_list[choice - 1]

    def coach_is_undefeated(self):
        for pokemon in self.pokemon_list:
            if pokemon.current_health > 0:
                return True
        return False

# Función que realiza un turno de combate entre dos Pokemons
def combat_turn(attacker, defender):
    print(f"{attacker.name} ataca con {attacker.attack_name}!")
    damage = attacker.fight_attack()
    defender.current_health -= damage
    if defender.current_health < 0:
        defender.current_health = 0
    print(f"{defender.name} recibe {damage} puntos de daño.")
    print(f"{defender.name} tiene {defender.current_health} puntos de vida restantes.")
    if defender.current_health == 0:
        print(f"{defender.name} ha sido derrotado!")

# Función que simula un combate entre dos entrenadores
def combat(entrenador1, entrenador2):
    print(f"Comienza el combate entre {entrenador1.name} y {entrenador2.name}!\n")
    # Se elige un Pokemon de cada entrenador para el combate
    p1 = entrenador1.get_pokemon_in_a_list_of_pokemons()
    p2 = entrenador2.get_pokemon_in_a_list_of_pokemons()
    print(f"{entrenador1.name} envía a {p1} al campo de batalla!")
    print(f"{entrenador2.name} envía a {p2} al campo de batalla!\n")
    # Se lleva a cabo el combate hasta que uno de los dos entrenadores se queda sin Pokemons
    while entrenador1.coach_is_undefeated() and entrenador2.coach_is_undefeated():
        # Turno de entrenador1
        print(f"\nTurno de {entrenador1.name} ({p1})")
        combat_turn(p1, p2)
        if p2.current_health == 0:
            print(f"{entrenador2.name} ha sido derrotado!")
            break   
        # Turno de entrenador2
        print(f"\nTurno de {entrenador2.name} ({p2})")  
        combat_turn(p2, p1)
        if p1.current_health == 0:
            print(f"{entrenador1.name} ha sido derrotado!")
            break



