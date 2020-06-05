import random
import time
import os
import cmath



#####                          #####     
#####                          #####
#####         Cho  Han         #####
#####                          #####
#####                          #####

def cho_han(money):
    
    time.sleep(1)
    os.system('clear')
    time.sleep(0.5)

    print("""
                                  ___ _             _  _           
                                 / __| |_  ___     | || |__ _ _ _  
                                | (__| ' \/ _ \    | __ / _` | ' \ 
                                 \___|_||_\___/    |_||_\__,_|_||_|

     
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
                                    Please Make a Choice:
                                    ---------------------

                                        1. Cho (Even)
                                        2. Han (Odd)
        """)
        bet = int(input())
        while(bet != 1 and bet != 2):
            print("                           Wrong number. Choose [1-2]")
            bet = int(input())
        
        time.sleep(1)
        print("""
                                        Throwing Dices
        """)
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        if((dice1 + dice2) % 2 == 0):
            print(" ")
            print("                                             " + str(dice1 + dice2))
            time.sleep(1)
            print(" ")
            print("                                             Cho (Even)")
            time.sleep(1)
            if(bet == 1):
                print(" ")
                print("                                          you won: " + str(amount) + "$")
                time.sleep(1)
                money = money + amount
            else:
                print(" ")
                print("                                          you lost: " + str(amount) + "$")
                time.sleep(1)
                money = money - amount
        else:
            print()
            print("                                             " + str(dice1 + dice2))
            time.sleep(1)
            print(" ")
            print("                                             Han (Odd)")
            time.sleep(1)
            if(bet == 2):
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
        print("                                     You have no money left")
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
        cho_han(money)
    else:
        return money