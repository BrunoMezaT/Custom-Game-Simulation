'''
Description: Program that simulates a 'Game'
Programmer: Bruno M.
Date: October 27, 2025
Version: 1.0
'''
#Setup
import random
suits=['Hearts','Diamonds','Clubs','Spades']
x=0

#Trials to simulate
user=int(input("Number of tries: "))

while x < user:
    x+=1
    #Simulating rolling dice and selecting cards
    b_die=random.randint(1,20)
    r_die=random.randint(1,20)
    card1_n=random.randint(1,10)
    card2_n=random.randint(1,10)
    card1=str(card1_n)+' of '+random.choice(suits)
    card2=str(card2_n)+' of '+random.choice(suits)
    print('Black die:', b_die)
    print('Red die:', r_die)
    print(card1)
    print(card2)

    #Simplifying colours
    if 'C' in card1 or 'S' in card1:
        card1_c='black'
    else:
        card1_c='red'
        
    if 'C' in card2 or 'S' in card2:
        card2_c='black'
    else:
        card2_c='red'

    #Checking for biggest victory condition 
    if b_die >=15:
        if card1_c=='black' and card1_n>=6:
            if card2_c=='black' and card2_n>=6:
                print('Won a big prize')
                print()
                continue
    elif r_die >=15:
        if card1_c=='black' and card1_n>=6:
            if card2_c=='black' and card2_n>=6:
                print('Won a big prize')
                print()
                continue

    #Checking for intermediate victory condition 
    if b_die >=9:
        if card1_c=='black' and card2_c=='black':
            print('Won a medium prize')
            print()
            continue
    elif r_die >=15:
        if card1_c=='red' and card2_c=='red':
            print('Won a medium prize')
            print()
            continue

    #Checking for smallest victory condition or concluding the player lost
    if b_die>=11 and r_die>=11:
        print('Won a small prize')
        print()
        continue
    elif card1_n>=6 and card2_n>=6:
        print('Won a small prize')
        print()
        continue
    else:
        print("Lost")
        print()
