from random import randint

Yes = None

Want_Play_Game = input('Oh, hello there, I didnt see yo- umm, my name is William, D-Do you want to play a game of rock paper scissors?  ').lower()
if Want_Play_Game in ('yes', 'yup', 'y', 'sure', 'yeah', 'ok', 'okay'):
    Yes = 1
else:
    Want_Play_Game_2 = input('Ok well then, umm... \n Well how about tictactoe instead?  ').lower()
    if Want_Play_Game_2 in ('yes', 'yup', 'y', 'sure', 'yeah', 'ok', 'okay'):
        Yes = 2
    else:
        print('Ok then umm... PLease dont go, please stay, I-I havent talked to anyone in a while... Please just stay.')
        quit()


#Rock Paper Scissors
while Yes == 1:
    Player_choice = input('Ok lets play. Pick R for Rock P for Paper or S for Scissors. ').lower()
    while Player_choice != 'r' or 'p' or 's':
        Player_choice = input ('I-Im sorry but thats not an option, would you mind trying again?  ')
        if Player_choice == 'r' or 'p' or 's':
            break
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
    play_again = input('Do you want to play again, please play again.  ').lower()
    if play_again in ('yes', 'yup', 'y', 'sure', 'yeah', 'ok', 'okay'):
        Yes = 1
    else:
        Yes = 2
        print('Ok Lets play tictactoe instead.  ')
        break


#Tictactoe

Player_input = None
Player_input_1 = "A"
Player_input_2 = "B"
Player_input_3 = "C"
Player_input_4 = "D"
Player_input_5 = "E"

Computer_input = None
Computer_input_1 = "F"
Computer_input_2 = "G"
Computer_input_3 = "H"
Computer_input_4 = "I"

tictactoe_win = 0

Spot_1 = '_'
Spot_2 = '_'
Spot_3 = '_'
Spot_4 = '_'
Spot_5 = '_'
Spot_6 = '_'
Spot_7 = '_'
Spot_8 = '_'
Spot_9 = '_'

def win_condition_function():
    global tictactoe_win
    if Spot_1 == 'X' and Spot_2 == 'X' and Spot_3 == 'X' or Spot_1 == 'X' and Spot_4 == 'X' and Spot_7 == 'X' or Spot_1 == 'X' and Spot_5 == 'X' and Spot_9 == 'X' or Spot_4 == 'X' and Spot_5 == 'X' and Spot_6 == 'X' or Spot_8 == 'X' and Spot_5 == 'X' and Spot_2 == 'X' or Spot_3 == 'X' and Spot_5 == 'X' and Spot_7 == 'X' or Spot_3 == 'X' and Spot_6 == 'X' and Spot_9 == 'X' or Spot_9 == 'X' and Spot_8 == 'X' and Spot_7 == 'X':
        print('You win')
        tictactoe_win = 1
        return
    if Spot_1 == 'O' and Spot_2 == 'O' and Spot_3 == 'O' or Spot_1 == 'O' and Spot_4 == 'O' and Spot_7 == 'O' or Spot_1 == 'O' and Spot_5 == 'O' and Spot_9 == 'O' or Spot_4 == 'O' and Spot_5 == 'O' and Spot_6 == 'O' or Spot_8 == 'O' and Spot_5 == 'O' and Spot_2 == 'O' or Spot_3 == 'O' and Spot_5 == 'O' and Spot_7 == 'O' or Spot_3 == 'O' and Spot_6 == 'O' and Spot_9 == 'O' or Spot_9 == 'O' and Spot_8 == 'O' and Spot_7 == 'O':
        print('You lose')
        tictactoe_win = 1
        return

def place_player_choice_function():
    global Spot_1
    global Spot_2
    global Spot_3
    global Spot_4
    global Spot_5
    global Spot_6
    global Spot_7
    global Spot_8
    global Spot_9

    global Player_input

    if Player_input == 1:
        Spot_1 = 'X'
    elif Player_input == 2:
        Spot_2 = 'X'
    elif Player_input == 3:
        Spot_3 = 'X'
    elif Player_input == 4:
        Spot_4 = 'X'
    elif Player_input == 5:
        Spot_5 = 'X'
    elif Player_input == 6:
        Spot_6 = 'X'
    elif Player_input == 7:
        Spot_7 = 'X'
    elif Player_input == 8:
        Spot_8 = 'X'
    elif Player_input == 9:
        Spot_9 = 'X'

def place_computer_choice_function():
    global Spot_1
    global Spot_2
    global Spot_3
    global Spot_4
    global Spot_5
    global Spot_6
    global Spot_7
    global Spot_8
    global Spot_9
    global Computer_input

    if Computer_input == 1:
        Spot_1 = 'O'
    elif Computer_input== 2:
        Spot_2 = 'O'
    elif Computer_input== 3:
        Spot_3 = 'O'
    elif Computer_input== 4:
        Spot_4 = 'O'
    elif Computer_input== 5:
        Spot_5 = 'O'
    elif Computer_input== 6:
        Spot_6 = 'O'
    elif Computer_input== 7:
        Spot_7 = 'O'
    elif Computer_input== 8:
        Spot_8 = 'O'
    elif Computer_input== 9:
        Spot_9 = 'O'

def detect_inputs():
    global Player_input
    global Computer_input
    while Player_input not in {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'D'}:
        Player_input = input("i'm sorry but umm, that's not one of the spots on the board, you mind trying again please?  ")
        if Player_input in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            break
    Player_input = int(Player_input)
    while Player_input in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Player_input_4, Computer_input_4}:
        Player_input = input("Sorry that spot has already been filled, i'd like it if you picked a diffrent number please.  ")
        while Player_input not in {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'D'}:
            Player_input = input("i'm sorry but umm, that's not one of the spots on the board, you mind trying again please?  ")
            if Player_input in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                break
        Player_input = int(Player_input)
        if Player_input not in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Computer_input_4}:
            break
    Computer_input = randint(1,9)
    while Computer_input in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Player_input_4,}:
        Computer_input = randint (1,9)
        if Computer_input not in {Player_input_1, Computer_input_1, Player_input_2, Computer_input_2, Player_input_3, Computer_input_3, Player_input_4,}:
            break


while Yes == 2:
    while tictactoe_win == 0:

        Spot_1 = '_'
        Spot_2 = '_'
        Spot_3 = '_'
        Spot_4 = '_'
        Spot_5 = '_'
        Spot_6 = '_'
        Spot_7 = '_'
        Spot_8 = '_'
        Spot_9 = '_'

        Player_input = input(f'You go first, pick a number 1-9 to place your choice(one is in the top right and nine in the bottom left). \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
        detect_inputs()

        place_player_choice_function()
        Player_input_1 = Player_input
        Player_input = None
        win_condition_function()
        if tictactoe_win == 1:
            break
        place_computer_choice_function()
        Computer_input_1 = Computer_input
        Computer_input = None
        win_condition_function()
        if tictactoe_win == 1:
            break

        Player_input = input(f'I went in spot {Computer_input_1}, now it is your turn, I-If you still want to p-p-play. Here is the new board \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
        detect_inputs()

        place_player_choice_function()
        Player_input_2 = Player_input
        Player_input = None
        win_condition_function()
        if tictactoe_win == 1:
            break
        place_computer_choice_function()
        Computer_input_2 = Computer_input
        Computer_input = None
        win_condition_function()
        if tictactoe_win == 1:
            break

        Player_input = input(f'I went in spot {Computer_input_2}, now it is your turn, I-If you still want to p-p-play. Here is the new board \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
        detect_inputs()

        place_player_choice_function()
        Player_input_3 = Player_input
        Player_input = None
        win_condition_function()
        if tictactoe_win == 1:
            break
        place_computer_choice_function()
        Computer_input_3 = Computer_input
        Computer_input = None
        win_condition_function()
        if tictactoe_win == 1:
            break

        Player_input = input(f'I went in spot {Computer_input_3}, now it is your turn, I-If you still want to p-p-play. Here is the new board \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
        detect_inputs()
            
        place_player_choice_function()
        Player_input_4 = Player_input
        Player_input = None
        win_condition_function()
        if tictactoe_win == 1:
            break
        place_computer_choice_function()
        Computer_input_4 = Computer_input
        Computer_input = None
        win_condition_function()
        if tictactoe_win == 1:
            break
        
        Player_input = input(f'I went in spot {Computer_input_4}, now it is your turn, I-If you still want to p-p-play. Here is the new board \n   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|      ')
        detect_inputs()

        Computer_input = None
        place_player_choice_function()
        Player_input_5 = Player_input
        Player_input = None
        win_condition_function()
        if tictactoe_win == 1:
            break

    print(f'   |{Spot_1}|{Spot_2}|{Spot_3}|\n   |{Spot_4}|{Spot_5}|{Spot_6}|\n   |{Spot_7}|{Spot_8}|{Spot_9}|')
    tictactoe_win = 0
    play_again = None
    play_again = input('Do you want to play again, please play again.  ').lower()
    if play_again in ('yes', 'yup', 'y', 'sure', 'yeah', 'ok', 'okay'):
        Yes = 2
    else:
        Yes = 3
    if Yes == 3:
        break