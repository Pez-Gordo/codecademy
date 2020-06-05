import random
import time
import os
import cmath



#####                          #####     
#####                          #####
#####       Cards Battle       #####
#####                          #####
#####                          #####
    

def cards_battle(money):
   
    time.sleep(1)
    os.system('clear')
       
    time.sleep(0.5)

    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    figure = ["Spades", "Hearts", "Diamonds", "Clubs"]

    print("""
                             ___             _      ___       _   _   _     
                            / __|__ _ _ _ __| |___ | _ ) __ _| |_| |_| |___ 
                           | (__/ _` | '_/ _` (_-< | _ \/ _` |  _|  _| / -_)
                            \___\__,_|_| \__,_/__/ |___/\__,_|\__|\__|_\___|
                                                              _
                                      ,'`.    _  _    /\    _(_)_
                                     (_,._)  ( `' )  <  >  (_)+(_)
                                       /\     `.,'    \/      |
     
    """)
    if(money > 0):
        print("                                            You have: " + str(money) + "$")
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
                            Press enter to pick a card from the stack:
                            ------------------------------------------                        
        """)
        input()
        
        time.sleep(1)
        print("""
                                        Picking card...
        """)
        time.sleep(1)
        user_rand_card = random.randint(0, 12)
        user_rand_figure = random.randint(0, 3)

        user_card = cards[user_rand_card] + " of " + figure[user_rand_figure]
        
        comp_rand_card = random.randint(0, 12)
        comp_rand_figure = random.randint(0, 3)
        
        comp_card = cards[comp_rand_card] + " of " + figure[comp_rand_figure]

        while(user_card == comp_card):
            comp_rand_card = random.randint(0, 12)
            comp_rand_figure = random.randint(0, 3)
        
            comp_card = cards[comp_rand_card] + " of " + figure[comp_rand_figure]
        

        print("""
                                    User card: {user_card}
                                    Comp card: {comp_card}
        """.format(user_card = user_card, comp_card = comp_card))
        time.sleep(1)
        
        if(user_rand_card == comp_rand_card):
            print(" ")
            print("                                             This is a draw")
            time.sleep(1)
        
        elif(user_rand_card > comp_rand_card):
                print(" ")
                print("                                          you won: " + str(amount) + "$")
                time.sleep(2)
                money = money + amount
        elif(user_rand_card < comp_rand_card):
                print(" ")
                print("                                          you lost: " + str(amount) + "$")
                time.sleep(2)
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
        cards_battle(money)
    else:
        return money