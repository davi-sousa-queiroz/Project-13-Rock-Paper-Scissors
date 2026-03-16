# ------------ IMPORTS --------------
import random
import time
# --------- GAME VARIABLES ----------
symbol_values = {
    'rock' : 1,
    'paper' : 2,
    'scissors' : 3
}

wins = 0

loses = 0

ties = 0
# ----------- FUNCTIONS -------------
def welcome():
    print("=================================")
    print("===== ROCK  PAPER  SCISSORS =====")
    print("=================================\n")
    
    time.sleep(1)

    print("Welcome to Rock Paper Scissors!\n")
    time.sleep(1)
    print("Reach 10 wins to become the rock paper scissors champion! 🏆\n")
    time.sleep(2)
    print("Reach 10 losses, and your eliminated! 😵\n")
    time.sleep(2)
    print("Good Luck!\n")
    time.sleep(1)
def player_hand():
    player_move = input("What's your move: (r)ock, (p)aper, or (s)cissors?\n>>")
def computer_hand():
    hands = ['r', 'p', 's']
    computer_move = random.choice(hands)
def win():
    global wins
    print("You won!")
    wins += 1
def lose():
    global loses
    print("You lost!")
    loses += 1
def tie():
    global ties
    print("You tied!")
    ties += 1
def calculate_winner(player_move, computer_move):
    global wins
    global loses
    global ties
    if player_move == computer_move:
        tie()
    elif player_move == 'r' and computer_move == 'p':
        lose()
    elif player_move == 'r' and computer_move == 's':
        win()
    elif player_move == 'p' and computer_move == 'r':
        win()
    elif player_move == 'p' and computer_move == 's':
        lose()
    elif player_move == 's' and computer_move == 'p':
        win()
    elif player_move == 's' and computer_move == 'r':
        lose()
    else:
        print('GAME BUG IN CALCULATE WINNER FUNCTION')

# ----------- MAIN LOOP -------------