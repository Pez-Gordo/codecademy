#import libraries
import time
import os
import random

#import classes
from pok_classes import Pokemon
from pok_classes import Trainer

#import pokemon subclasses
from pok_classes import Charmander
from pok_classes import Pikachu
from pok_classes import Squirtle
from pok_classes import Bulbasaur
from pok_classes import Metapod
from pok_classes import Caterpie

#import ascii art file
import pok_ascii


# # # #           # # # #
 # # #  Functions  # # # 
# # # #           # # # # 

# config() --> creates trainers and pokemons. Returns 2 Trainer objects
def config():
    pok_rounds = [1, 2, 3, 4, 5, 6]
    trainer1 = True
    #we get players names
    print(" ")
    print(" ")
    print(" ")
    time.sleep(3)
    print("          Trainer 1 type your name: ")
    trainer_one_name = input()
    print("          Trainer 2 type your name: ")
    trainer_two_name = input()
    time.sleep(2)
    os.system('clear')
    #we loop 6 times to allow players choose their pokemons
    for num in pok_rounds:
        if(num < 4):
            print("          {name} choose your pokemon {number}".format(name = trainer_one_name, number = num))
        else:
            num = num - 3
            print("          {name} choose your pokemon {number}".format(name = trainer_two_name, number = num))
        print("                 ")
        print("                 0. Pikachu")
        print("                 1. Charmander")
        print("                 2. Squirtle")
        print("                 3. Bulbasaur")
        print("                 4. Metapod")
        print("                 5. Caterpie")
        pok_choice = int(input())
        c = 0
        #we check the input. Only [0-5] allowed
        while(pok_choice < 0 or pok_choice > 5):
            print("Wrong choice. Type a number [0-5]")
            pok_choice = int(input())
        if(num == 1):
            if(pok_choice == 0):
                a = Pikachu(random.randint(1, 10))
            elif(pok_choice == 1):
                a = Charmander(random.randint(1, 10))
            elif(pok_choice == 2):
                a = Squirtle(random.randint(1, 10))
            elif(pok_choice == 3):
                a = Bulbasaur(random.randint(1, 10))
            elif(pok_choice == 4):
                a = Metapod(random.randint(1, 10))
            elif(pok_choice == 5):
                a = Caterpie(random.randint(1, 10))
            print("Thanks")
            time.sleep(1)
            os.system('clear')
        if(num == 2):
            if(pok_choice == 0):
                b = Pikachu(random.randint(1, 10))
            elif(pok_choice == 1):
                b = Charmander(random.randint(1, 10))
            elif(pok_choice == 2):
                b = Squirtle(random.randint(1, 10))
            elif(pok_choice == 3):
                b = Bulbasaur(random.randint(1, 10))
            elif(pok_choice == 4):
                b = Metapod(random.randint(1, 10))
            elif(pok_choice == 5):
                b = Caterpie(random.randint(1, 10))
            print("Thanks")
            time.sleep(1)
            os.system('clear')
        if(num == 3):
            if(pok_choice == 0):
                c = Pikachu(random.randint(1, 10))
            elif(pok_choice == 1):
                c = Charmander(random.randint(1, 10))
            elif(pok_choice == 2):
                c = Squirtle(random.randint(1, 10))
            elif(pok_choice == 3):
                c = Bulbasaur(random.randint(1, 10))
            elif(pok_choice == 4):
                c = Metapod(random.randint(1, 10))
            elif(pok_choice == 5):
                c = Caterpie(random.randint(1, 10))
            print("Thanks")
            time.sleep(1)
            os.system('clear')
    
        if(trainer1 and c != 0):
            trainer_one = Trainer([a,b,c], random.randint(1, 4), trainer_one_name)
            trainer1 = False
            c = 0
        elif((trainer1 == False) and (c != 0)):
            trainer_two = Trainer([a,b,c], random.randint(1, 4), trainer_two_name)
        os.system('clear')

    #We print information about players 
    time.sleep(0.8)
    print(trainer_one)
    time.sleep(2)
    print(" ")
    print("Press Enter...")
    input()
    os.system('clear')
    time.sleep(0.8)
    print(trainer_two)
    time.sleep(2)
    print(" ")
    print("Press Enter...")
    input()
    return trainer_one, trainer_two

# turn() --> controls the action of the game. One turn for each player and 10 rounds. Takes the 2 Trainers objects as parameters
def turn(t1, t2):
    t1.isActive = True
    rondas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    for num in rondas:
        time.sleep(.8)
        choice = 1
        while(choice != 0 and choice != 3):
            os.system('clear')
            print(" ")
            print("         --------")
            print("         Round " + str(num) + ":")
            time.sleep(0.6)
            print(" ")
            print("         ----------------------------------------")
            print("         Player 1 is your turn: Choose an option:")
            print("                                        ")
            time.sleep(0.6)
            print("                     0. Attack")
            print("                     1. Potion")
            print("                     2. Change Pokemon")
            print("                     3. Skip Turn")
        
            choice = int(input())
            if(choice == 0):
                time.sleep(.8)
                t1.attack_other_trainer(t2)
            elif(choice == 1):
                time.sleep(.8)
                t1.use_potion()
            elif(choice == 2):
                time.sleep(.8)
                print(" ")
                print("Choose [0-2] for new active pokemon")
                user_input = int(input())
                t1.switch_active_pokemon(user_input)
            elif(choice == 3):
                time.sleep(.8)
                print("         Skipping turn")
                time.sleep(.3)
                print("             Skipping turn")
                time.sleep(.3)
                print("         Skipping turn")
                time.sleep(.3)
            else:
                print("Wrong choice. You need a number between 0 and 3 for your actions.")
    
        choice = 1
        while(choice != 0 and choice != 3):
            os.system('clear')
            print(" ")
            print("         --------")
            print("         Round " + str(num) + ":")
            time.sleep(0.6)
            print(" ")
            print("         ----------------------------------------")
            print("         Player 2 is your turn: Choose an option:")
            print("                                        ")
            time.sleep(0.6)
            print("                     0. Attack")
            print("                     1. Potion")
            print("                     2. Change Pokemon")
            print("                     3. Skip Turn")
            
            choice = int(input())

            if(choice == 0):
                time.sleep(.8)
                t2.attack_other_trainer(t1)
            elif(choice == 1):
                time.sleep(.8)
                t2.use_potion()
            elif(choice == 2):
                time.sleep(.8)
                print("Choose [0-2] for new active pokemon")
                user_input = int(input())
                t2.switch_active_pokemon(user_input)
            elif(choice == 3):
                time.sleep(.8)
                print("         Skipping turn")
                time.sleep(.3)
                print("     Skipping turn")
                time.sleep(.3)
                print("         Skipping turn")
                time.sleep(.3)
            else:
                print("Wrong choice --> missed turn. You need a number between 0 and 3 for your actions. Pay more attention in next round")
        

#we print the welcome
def intro():
    time.sleep(1)
    os.system('clear')
    time.sleep(1)
    print(" ")
    print(" ")
    print(" ")
    print("                     Welcome to:")
    time.sleep(2)
    print("""
     ___     _                        __  __         _              
    | _ \___| |_____ _ __  ___ _ _   |  \/  |__ _ __| |_ ___ _ _ ___
    |  _/ _ \ / / -_) '  \/ _ \ ' \  | |\/| / _` (_-<  _/ -_) '_(_-<
    |_| \___/_\_\___|_|_|_\___/_||_| |_|  |_\__,_/__/\__\___|_| /__/

    """)
    time.sleep(2)

# we print info to the screen and greet players
def game_over():
    os.system('clear')
    time.sleep(1)
    print(" ")
    print(" ")
    print(" ")
    print("""
                         ___                   ___              
                        / __|__ _ _ __  ___   / _ \__ _____ _ _ 
                       | (_ / _` | '  \/ -_) | (_) \ V / -_) '_|
                        \___\__,_|_|_|_\___|  \___/ \_/\___|_| 


    """)
    time.sleep(1)
    print(" ")
    print(" ")
    print(" ")
    print("""                            
                                Thanks for coming !!! 



    """)
    time.sleep(1)

