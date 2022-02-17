from random import randint


Want_Play_Game = input('Do you want to play a game of rock paper scissors?  ').lower()
if Want_Play_Game in ('yes', 'yup', 'y', 'sure', 'yeah', 'ok', 'okay'):
    Yes = 1
else:
    Want_Play_Game_2 = input('Ok well then, umm... \n Alright do you want to play tictactoe instead?  ').lower()
    if Want_Play_Game_2 in ('yes', 'yup', 'y', 'sure', 'yeah', 'ok', 'okay'):
        Yes = 2
    else:
        print('Fine then i didnt want to play anyways. Goodbye.')

#Rock Paper Scissors
while Yes == 1:
    Player_choice = input('Ok lets play. Pick R for Rock P for Paper or S for Scissors. ').lower()
    Computer_input = randint(1, 3)
    if Computer_input == 1:
        Computer_choice = 'Rock'
    elif Computer_input == 2:
        Computer_choice = 'Paper'
    else: Computer_choice = 'Scissors'
    if Player_choice == 'r':
        Player_choice_varible = 1
    elif Player_choice == 'p':
        Player_choice_varible = 2
    elif  Player_choice == "s":
        Player_choice_varible = 3
    else: 
        print("that's not a choice")
    print (f'I chose {Computer_choice}')
    outcome = Computer_input - Player_choice_varible
    if outcome in {'-2', '1'}:
        print('I win')
    elif outcome == 0:
        print('We tied')
    else:
        print('You win')
    play_again = input('Do you want to play again.  ').lower()
    if play_again in ('yes', 'yup', 'y', 'sure', 'yeah', 'ok', 'okay'):
        Yes = 1
    else:
        Yes = 2
        print('Ok Lets play tictactoe instead.  ')
        break


#Tictactoe

global Player_input_2
global Player_input_3
global Player_input_4
global Player_input_5

Player_input_1 = "A"
Player_input_2 = "B"
Player_input_3 = "C"
Player_input_4 = "D"
Player_input_5 = "E"

Computer_input_1 = "F"
Computer_input_2 = "G"
Computer_input_3 = "H"
Computer_input_4 = "I"

Spot_1 = '_'
Spot_2 = '_'
Spot_3 = '_'
Spot_4 = '_'
Spot_5 = '_'
Spot_6 = '_'
Spot_7 = '_'
Spot_8 = '_'
Spot_9 = '_'

def Chosen_player_slot_function():

    global Player_input_2
    global Player_input_3
    global Player_input_4
    global Player_input_5

    while Player_input_2 in {Player_input_1, Computer_input_1}:
        Player_input_2 = input('Sorry that sopt has already been filled, Pick a diffrent number.  ')
        if Player_input_5 not in {Player_input_1, Computer_input_1}:
            return
    while Player_input_3 in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2}:
        Player_input_3 = input('Sorry that sopt has already been filled, Pick a diffrent number.  ')
        if Player_input_5 not in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2}:
            return
    while Player_input_4 in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3}:
        Player_input_4 = input('Sorry that sopt has already been filled, Pick a diffrent number.  ')
        if Player_input_5 not in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3}:
            return 
    while Player_input_5 in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Player_input_4, Computer_input_4}:
        Player_input_5 = input('Sorry that sopt has already been filled, Pick a diffrent number.  ')
        if Player_input_5 not in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Player_input_4, Computer_input_4}:
            return

while Yes == 2:
    Player_input_1 = input(f'You go first, pick a number 1-9 to place your choice(one is in the top right and nin in the bottom left). \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
    computer_input_1 = randint(1,9)
    while computer_input_1 in {Player_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Player_input_4,}:
        computer_input_1 = randint(1,9)
        if computer_input_1 not in {Player_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Player_input_4,}:
            break

    if Player_input_1 == 1:
        Spot_1 = 'X'
    elif Player_input_1 == 2:
        Spot_2 = 'X'
    elif Player_input_1 == 3:
        Spot_3 = 'X'
    elif Player_input_1 == 4:
        Spot_4 = 'X'      
    elif Player_input_1 == 5:
        Spot_5 = 'X'
    elif Player_input_1 == 6:
        Spot_6 = 'X'
    elif Player_input_1 == 7:
        Spot_7 = 'X'
    elif Player_input_1 == 8:
        Spot_8 = 'X'
    elif Player_input_1 == 9:
        Spot_9 = 'X'
    else:
        print("broken")

    if Computer_input_1 == 1:
        Spot_1 = 'O'
    elif Computer_input_1 == 2:
        Spot_2 = 'O'
    elif Computer_input_1 == 3:
        Spot_3 = 'O'
    elif Computer_input_1 == 4:
        Spot_4 = 'O' 
    elif Computer_input_1 == 5:
        Spot_5 = 'O'
    elif Computer_input_1 == 6:
        Spot_6 = 'O'
    elif Computer_input_1 == 7:
        Spot_7 = 'O'
    elif Computer_input_1 == 8:
        Spot_8 = 'O'
    elif Computer_input_1 == 9:
        Spot_9 = 'O'
    else:
        print("broken")

    Player_input_2 = input(f'I went in space {computer_input_1}, now it is your turn. Here is the new board \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
    Chosen_player_slot_function()
    Computer_input_2 = randint(1,9)
    while Computer_input_2 in {Player_input_1, Computer_input_1, Player_input_2, Player_input_3, Computer_input_3, Player_input_4,}:
        Computer_input_2 = randint (1,9)
        if Computer_input_2 not in {Player_input_1, Computer_input_1, Player_input_2, Player_input_3, Computer_input_3, Player_input_4,}:
            break

    if Player_input_2 == 1:
        Spot_1 = 'X'
    elif Player_input_2 == 2:
        Spot_2 = 'X'
    elif Player_input_2 == 3:
        Spot_3 = 'X'
    elif Player_input_2 == 4:
        Spot_4 = 'X'      
    elif Player_input_2 == 5:
        Spot_5 = 'X'
    elif Player_input_2 == 6:
        Spot_6 = 'X'
    elif Player_input_2 == 7:
        Spot_7 = 'X'
    elif Player_input_2 == 8:
        Spot_8 = 'X'
    elif Player_input_2 == 9:
        Spot_9 = 'X'
    else:
        print("broken")

    if Computer_input_2 == 1:
        Spot_1 = 'O'
    elif Computer_input_2 == 2:
        Spot_2 = 'O'
    elif Computer_input_2 == 3:
        Spot_3 = 'O'
    elif Computer_input_2 == 4:
        Spot_4 = 'O'      
    elif Computer_input_2 == 5:
        Spot_5 = 'O'
    elif Computer_input_2 == 6:
        Spot_6 = 'O'
    elif Computer_input_2 == 7:
        Spot_7 = 'O'
    elif Computer_input_2 == 8:
        Spot_8 = 'O'
    elif Computer_input_2 == 9:
        Spot_9 = 'O'

    Player_input_3 = input(f'I went in space {Computer_input_2}, now it is your turn. Here is the new board \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
    Chosen_player_slot_function()
    Computer_input_3 = randint(1,9)
    while Computer_input_3 in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Player_input_4,}:
        Computer_input_3 = randint (1,9)
        if Computer_input_3 not in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Player_input_4,}:
            break

    if Player_input_3 == 1:
        Spot_1 = 'X'
    elif Player_input_3 == 2:
        Spot_2 = 'X'
    elif Player_input_3 == 3:
        Spot_3 = 'X'
    elif Player_input_3 == 4:
        Spot_4 = 'X' 
    elif Player_input_3 == 5:
        Spot_5 = 'X'
    elif Player_input_3 == 6:
        Spot_6 = 'X'
    elif Player_input_3 == 7:
        Spot_7 = 'X'
    elif Player_input_3 == 8:
        Spot_8 = 'X'
    elif Player_input_3 == 9:
        Spot_9 = 'X'

    if Computer_input_3 == 1:
        Spot_1 = 'O'
    elif Computer_input_3 == 2:
        Spot_2 = 'O'
    elif Computer_input_3 == 3:
        Spot_3 = 'O'
    elif Computer_input_3 == 4:
        Spot_4 = 'O'
    elif Computer_input_3 == 5:
        Spot_5 = 'O'
    elif Computer_input_3 == 6:
        Spot_6 = 'O'
    elif Computer_input_3 == 7:
        Spot_7 = 'O'
    elif Computer_input_3 == 8:
        Spot_8 = 'O'
    elif Computer_input_3 == 9:
        Spot_9 = 'O'

    Player_input_4 = input(f'I went in space {Computer_input_3}, now it is your turn. Here is the new board \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
    Chosen_player_slot_function()
    Computer_input_4 = randint(1,9)
    while Computer_input_4 in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Player_input_4,}:
        Computer_input_4 = randint (1,9)
        if Computer_input_4 not in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Player_input_4,}:
            break
        
    if Player_input_4 == 1:
        Spot_1 = 'X'
    elif Player_input_4 == 2:
        Spot_2 = 'X'
    elif Player_input_4 == 3:
        Spot_3 = 'X'
    elif Player_input_4 == 4:
        Spot_4 = 'X'       
    elif Player_input_4 == 5:
        Spot_5 = 'X'
    elif Player_input_4 == 6:
        Spot_6 = 'X'
    elif Player_input_4 == 7:
        Spot_7 = 'X'
    elif Player_input_4 == 8:
        Spot_8 = 'X'
    elif Player_input_4 == 9:
        Spot_9 = 'X'

    if Computer_input_4 == 1:
        Spot_1 = 'O'
    elif Computer_input_4 == 2:
        Spot_2 = 'O'
    elif Computer_input_4 == 3:
        Spot_3 = 'O'
    elif Computer_input_4 == 4:
        Spot_4 = 'O'       
    elif Computer_input_4 == 5:
        Spot_5 = 'O'
    elif Computer_input_4 == 6:
        Spot_6 = 'O'
    elif Computer_input_4 == 7:
        Spot_7 = 'O'
    elif Computer_input_4 == 8:
        Spot_8 = 'O'
    elif Computer_input_4 == 9:
        Spot_9 = 'O'

    Player_input_5 = input(f'I went in space {Computer_input_4}, now it is your turn. Here is the new board \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
    Chosen_player_slot_function()
    quit()










#    else:
#        if Player_input_1 == 1:
#            Spot_1 = 'X'
#        elif Player_input_1 == 2:
#            Spot_2 = 'X'
#        elif Player_input_1 == 3:
#            Spot_3 = 'X'
#        elif Player_input_1 == 4:
#            Spot_4 = 'X'       
#        elif Player_input_1 == 5:
#            Spot_5 = 'X'
#        elif Player_input_1 == 6:
#            Spot_6 = 'X'
#        elif Player_input_1 == 7:
#            Spot_7 = 'X'
#        elif Player_input_1 == 8:
#            Spot_8 = 'X'
#        elif Player_input_1 == 9:
#            Spot_9 = 'X'
#        return