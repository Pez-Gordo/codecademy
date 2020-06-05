import random
import time
import os
import cmath



#####                          #####     
#####                          #####
#####       Flip the coin      #####
#####                          #####
#####                          #####


def flip_coin(money):

    os.system('clear')
       
    time.sleep(0.5)

    print("""
                 ___ _ _        _   _           ___     _      
                | __| (_)_ __  | |_| |_  ___   / __|___(_)_ _  
                | _|| | | '_ \ |  _| ' \/ -_) | (__/ _ \ | ' \ 
                |_| |_|_| .__/  \__|_||_\___|  \___\___/_|_||_|
                        |_|                                    

     
    """)
    if(money > 0):
        print("                                          You have: " + str(money) + "$")
        time.sleep(0.5)
        print("""
                                    How much do you wanna bet?
                                        
        """)
        
        amount = int(input())
        
        while(amount > money):
            print("                      You cannot bet more money than you have. Try again")
            amount = int(input())
        time.sleep(2)
        print("""
                                    Heads(1) or Tails(2)?
        """)
        bet = int(input())
        while(bet != 1 and bet != 2):
            print("                           Wrong number. Choose [1-2]")
            bet = int(input())
        
        time.sleep(1)
        print("""
                                        Flipping coin
        """)
        coin = random.randint(1, 2)
        if(coin == 1):
            print(" ")
            print("                                             Heads")
            time.sleep(1)
        else:
            print(" ")
            print("                                             Tails")
            time.sleep(1)
        
        if(bet == coin):
            print(" ")
            print("                                          you won: " + str(amount) + "$")
            time.sleep(1)
            money = money + amount
            
        else:
            print(" ")
            print("                                          you lost: " + str(amount) + "$")
            time.sleep(1)
            money = money - amount
            
        time.sleep(1.2)
        
    else:
        print("                                You have no money left")
        time.sleep(1)
        game_over(money)
    
    print("""
                            Press "R" for another round
                            Press "C" to change game
                            """)

    choice = input()

    while(choice != "r" and choice != "c"):
        print("                             choose (R) or (C)")
        choice = input()
    if(choice == "r"):
        flip_coin(money)
    else:
        return money