import random
import time
import os
import cmath



#####                          #####     
#####                          #####
#####       Roulette           #####
#####                          #####
#####                          #####

def roulette(money):
    
    time.sleep(1)
    os.system('clear')
       
    time.sleep(0.5)


    print("""
                                   ___          _     _   _       
                                  | _ \___ _  _| |___| |_| |_ ___ 
                                  |   / _ \ || | / -_)  _|  _/ -_)
                                  |_|_\___/\_,_|_\___|\__|\__\___|

     
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
                                Choose what do you wanna bet for:
                                ---------------------------------
                                    1. High or Low
                                    2. Red or Black
                                    3. Odd or Even                       
                                    4. Single Number

                                    
        """)
            
        bet_game = int(input())
        # We check the input is a number between 1 and 5    
        while(bet_game < 1 or bet_game > 5):
            print(" ")
            print("You need a number between [1-5]")
            bet_game = int(input())

       
        if(bet_game == 1):
            print(" ")
            print("                                   Betting for High or Low")
            print("""     
                                        1. Low [1-18]
                                        2. High [19-36]
        """)
            choice = int(input())
            while(choice != 1 and choice != 2):
                print(" ")
                print("                                             Choose a number between [1-2]")
                choice = int(input())
            number = random.randint(1, 36)
            if(number < 19 and choice == 1):
                print("                                          " + str(number))
                time.sleep(.8)
                print(" ")
                print("                                          you won: " + str(amount) + "$")
                time.sleep(2)
                money = money + amount
            elif(number > 18 and choice == 2):
                print("                                          " + str(number))
                time.sleep(.8)
                print(" ")
                print("                                          you won: " + str(amount) + "$")
                time.sleep(2)
                money = money + amount
            else:
                print("                                          " + str(number))
                time.sleep(.8)
                print(" ")
                print("                                          you lost: " + str(amount) + "$")
                time.sleep(2)
                money = money - amount
            
        if(bet_game == 2):
            print(" ")
            print("                                   Betting for Red or Black")
            print("""     
                                            1. Red
                                            2. Black
            """)
            choice = int(input())
            while(choice != 1 and choice != 2):
                print(" ")
                print("                                             Choose a number between [1-2]")
                choice = int(input())
            number = random.randint(1, 36)
            if(number == choice and choice == 1):
                print("                                          Red ")
                time.sleep(.8)
                print(" ")
                print("                                          you won: " + str(amount) + "$")
                time.sleep(2)
                money = money + amount
            elif(number == choice and choice == 2):
                print("                                          Black ")
                time.sleep(.8)
                print(" ")
                print("                                          you won: " + str(amount) + "$")
                time.sleep(2)
                money = money + amount
            else:
                if(choice == 1):
                    print("                                          Black ")
                    time.sleep(.8)
                    print(" ")
                    print("                                          you lost: " + str(amount) + "$")
                    time.sleep(2)
                    money = money - amount
                else:
                    print("                                          Red ")
                    time.sleep(.8)
                    print(" ")
                    print("                                          you lost: " + str(amount) + "$")
                    time.sleep(2)
                    money = money - amount

            
        if(bet_game == 3):
            print(" ")
            print("                                   Betting for Odd or Even")
            print("""     
                                            1. Odd
                                            2. Even
            """)
            choice = int(input())
            while(choice != 1 and choice != 2):
                print(" ")
                print("                                             Choose a number between [1-2]")
                choice = int(input())
            number = random.randint(1, 36)
            if(number == choice and choice == 1):
                print("                                          Odd--> " + str(number))
                print(" ")
                time.sleep(.8)
                print("                                          you won: " + str(amount) + "$")
                time.sleep(2)
                money = money + amount
            if(number == choice and choice == 2):
                print("                                          Even--> "  + str(number))
                print(" ")
                time.sleep(.8)
                print("                                          you won: " + str(amount) + "$")
                time.sleep(2)
                money = money + amount
            else:
                if(choice == 1):
                    print("                                          Even--> " + str(number))
                    print(" ")
                    time.sleep(.8)
                    print("                                          you lost: " + str(amount) + "$")
                    time.sleep(2)
                    money = money - amount
                else:
                    print("                                          Odd--> " + str(number))
                    print(" ")
                    time.sleep(.8)
                    print("                                          you lost: " + str(amount) + "$")
                    time.sleep(2)
                    money = money - amount
            
        
        if(bet_game == 4):
            print(" ")
            print("                                   Betting for Single Number")
            print("                                     Enter a number [1-36]")
            choice = int(input())
            while(choice < 1 or choice > 36):
                print(" ")
                print("                                             Choose a number between [1-36]")
                choice = int(input())
            number = random.randint(1, 36)
            if(number == choice):
                amount = amount * 3
                print("                                          " + str(number) + " !!!")
                time.sleep(.8)
                print(" ")
                print(" ")
                print("                                          you won: " + str(amount) + "$")
                time.sleep(2)
                money = money + amount
            else:
                print("                                          " + str(number))
                time.sleep(.8)
                print(" ")
                print(" ")
                print("                                          you lost: " + str(amount) + "$")
                time.sleep(2)
                money = money - amount
            
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
        roulette(money)
    else:
        return money