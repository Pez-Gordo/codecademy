import random
import time
import os
import cmath

from goc_cho import cho_han
from goc_card import cards_battle
from goc_roulette import roulette
from goc_flip import flip_coin

money = 10000

def intro(money):
    
    time.sleep(0.5)
    os.system('clear')
    time.sleep(1)
    print("""
                                 _   _   _   _   _   _   _     _   _  
                                / \ / \ / \ / \ / \ / \ / \   / \ / \ 
                               ( W | e | l | c | o | m | e ) ( T | o )
                                \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ 

                    
    """)
    time.sleep(1)
    os.system('clear')
    time.sleep(0.5)
    print("""



                 ___      __  __     ___    ___   __    ___ _      _        ___     
                / __|__ _|  \/  |___/ __|  / _ \ / _|  / __| |_   /_\  _ _ / __|___ 
               | (_ / _` | |\/| / -_)__ \ | (_) |  _| | (__| ' \ / _ \| ' \ (__/ -_)
                \___\__,_|_|  |_\___|___/  \___/|_|    \___|_||_/_/ \_\_||_\___\___|

    """)
    time.sleep(1)
    print("""
                                What game do you want to play?

                                    1. flip the coin
                                    2. cho-han
                                    3. cards battle
                                    4. roulette

                                    5. exit
    """)

    game = int(input())
    # We check the input is a number between 1 and 5    
    while(game < 1 or game > 5):
        print(" ")
        print("You need a number between [1-5]")
        game = int(input())

    if(game == 5):
        money = game_over(money)
    if(game == 1):
        money = flip_coin(money)
    if(game == 2):
        money = cho_han(money)
    if(game == 3):
        money = cards_battle(money)
    if(game == 4):
        money = roulette(money)

    if(game != 5):
        intro(money)

def game_over(money):
    print(" ")
    print("                                       End of Game")
    print(" ")
    time.sleep(1.2)
    print(" ")
    print(" ")

    if(money > 10000):
        print("                                   You won: " + str(money - 10000) + " dollars")
        print(" ")
        print(" ")
    elif(money < 10000):
        print("                                   You lost: " + str(10000 - money) + " dollars")
        print(" ")
        print(" ")

    

intro(money)