import time
import os

import pok_ascii
from pok_ascii import print_pok


class Pokemon:
    # To create a pokemon, give it a name, type, and level. Its max health is determined by its level. Its starting health is its max health and it is not knocked out when it starts.
    def __init__(self, name, type, level = 5):
        self.name = name
        self.level = level
        self.max_level = 10
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False


    def __repr__(self):
        # Printing a pokemon will print a pokemon, it's level, name, health and type
        time.sleep(.8)
        return """                    
                    ---------------
                    name: {name} 
                    level: {level} 
                    health: {health} 
                    type: {type}
                    ---------------

        """.format(level = self.level, name = self.name, health=self.health, type = self.type)

    def revive(self):
        # Reviving a pokemon will flip it's status to False
        self.is_knocked_out = False
        # A revived pokemon can't have 0 health. This is a safety precaution. revive() should only be called if the pokemon was given some health, but if it somehow has no health, its health gets set to 1.
        if self.health == 0:
            self.health = 1
        print("{name} was revived!".format(name = self.name))

    def knock_out(self):
        # Knocking out a pokemon will flip its status to True.
        self.is_knocked_out = True
        # A knocked out pokemon can't have any health. This is a safety precaution. knock_out() should only be called if heath was set to 0, but if somehow the pokemon had health left, it gets set to 0.
        if self.health != 0:
            self.health = 0
        print("{name} was knocked out!".format(name = self.name))

    def lose_health(self, amount):
        # Deducts heath from a pokemon and prints the current health reamining
        self.health -= amount
        if self.health <= 0:
            #Makes sure the health doesn't become negative. Knocks out the pokemon.
            self.health = 0
            self.knock_out()
        else:
            time.sleep(2)
            print(" ")
            print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def gain_health(self, amount):
        # Adds to a pokemon's heath
        # If a pokemon goes from 0 heath, then revive it
        if self.health == 0:
            self.revive()
        self.health += amount
        # Makes sure the heath does not go over the max health
        if self.health >= self.max_health:
            self.health = self.max_health
        print(" ")
        print("{name} now has {health} health.".format(name = self.name, health = self.health))
        time.sleep(2)

    def attack(self, other_pokemon):
        # Checks to make sure the pokemon isn't knocked out
        if self.is_knocked_out:
            time.sleep(.8)
            print(" ")
            print("{name} can't attack because it is knocked out!".format(name = self.name))
            time.sleep(2)
            return
        # If the pokemon attacking has a disadvantage, then it deals damage equal to half its level to the other pokemon
        if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            time.sleep(.8)
            print(" ")
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = round(self.level * 0.5)))
            time.sleep(2)
            print(" ")
            print("It's not very effective")
            time.sleep(2)
            other_pokemon.lose_health(round(self.level * 0.5))
            time.sleep(2)
        # If the pokemon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other pokemon
        if (self.type == other_pokemon.type):
            time.sleep(.8)
            print(" ")
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
            other_pokemon.lose_health(self.level)
            time.sleep(2)

        # If the pokemon attacking has advantage, then it deals damage equal to double its level to the other pokemon
        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            time.sleep(.8)
            print(" ")
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
            time.sleep(2)
            print(" ")
            print("It's super effective")
            other_pokemon.lose_health(self.level * 2)
            time.sleep(2)


# Six classes that are subclasses of Pokemon. Charmander is a fire type, Squirtle is a Water type, and Bulbasaur is a Grass type.
class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)

class Pikachu(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Pikachu", "Fire", level)

class Caterpie(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Caterpie", "Water", level)

class Metapod(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Metapod", "Grass", level)

class Trainer:
    # A trainer has a list of pokemon, a number of potions and a name. When the trainer gets created, the first pokemon in their list of pokemons is the active pokemon (number 0)
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name
        self.isActive = False

    def __repr__(self):
        # Prints the name of the trainer, the pokemons they currently have, and the current active pokemon.
        time.sleep(.8)
        
        for pokemon in self.pokemons:
            os.system('clear')
            print(" ")
            print(" ")
            print("      Trainer {name} has the following pokemons:".format(name = self.name))
            print(" ")
            print(" ")
            print(pokemon)
            time.sleep(1)
            print_pok(pokemon.name)
            time.sleep(1)
                
        time.sleep(2)
        print("Press Enter...")
        input()
        return "The current active pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)

    def switch_active_pokemon(self, new_active):
        # Switches the active pokemon to the number given as a parameter
        # First checks to see the number is valid (between 0 and the length of the list)
        if new_active < len(self.pokemons) and new_active >= 0:
            # You can't switch to a pokemon that is knocked out
            if self.pokemons[new_active].is_knocked_out:
                time.sleep(2)
                print(" ")
                print("{name} is knocked out. You can't make it your active pokemon".format(name = self.pokemons[new_active].name))
                time.sleep(2)
            # You can't switch to your current pokemon
            elif new_active == self.current_pokemon:
                time.sleep(2)
                print(" ")
                print("{name} is already your active pokemon".format(name = self.pokemons[new_active].name))
                time.sleep(2)
            # Switches the pokemon
            else:
                self.current_pokemon = new_active
                time.sleep(2)
                print(" ")
                print("Go {name}, it's your turn!".format(name = self.pokemons[self.current_pokemon].name))
                time.sleep(2)
                name = self.pokemons[self.current_pokemon].name
                os.system('clear')
                print_pok(name)
                

    def use_potion(self):
        # Uses a potion on the active pokemon, assuming you have at least one potion.
        if(self.pokemons[self.current_pokemon].health == self.pokemons[self.current_pokemon].max_health):
            time.sleep(.8)
            print(" ")
            print("You can't use a potion now. Current pokemon is healthy enough.")
            time.sleep(2)
        else:
            #we check if we have  any potions left
            if self.potions > 0:
                time.sleep(.8)
                print(" ")
                print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
                time.sleep(2)
                # A potion restores 20 health
                self.pokemons[self.current_pokemon].gain_health(20)
                self.potions -= 1
            else:
                time.sleep(.8)
                print("You don't have any more potions")
                time.sleep(2)

    def attack_other_trainer(self, other_trainer):
        # Your current pokemon attacks the other trainer's current pokemon
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        if(my_pokemon.is_knocked_out):
            time.sleep(0.8)
            print(" ")
            print("Your pokemon is knocked out. Missed turn")
            time.sleep(1.8)
        #whe check that the other trainer's pokemon is not knocked out
        elif(their_pokemon.is_knocked_out):
            time.sleep(0.8)
            print(" ")
            print("You cannot attack a knocked out pokemon. Missed turn")
            time.sleep(1.8)
        else:
            my_pokemon.attack(their_pokemon)
            #we increase pokemon level in case of a ko
            if(their_pokemon.is_knocked_out):
                if(self.pokemons[self.current_pokemon].level < self.pokemons[self.current_pokemon].max_level):
                    self.pokemons[self.current_pokemon].level += 1
                    print(" ")
                    print("You knocked him out. Your {pok} is now level: {lev}".format(pok = self.pokemons[self.current_pokemon].name, lev = self.pokemons[self.current_pokemon].level))
                    time.sleep(2)
                #we want to check that the current pokemon is not in mas level
                else: 
                    print(" ")
                    print("You knocked him out but your {pok} is already in max level.".format(pok = self.pokemons[self.current_pokemon].name))
                    time.sleep(2)