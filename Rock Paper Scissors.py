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
    print("Reach 5 wins to become the rock paper scissors champion! 🏆\n")
    time.sleep(2)
    print("Reach 5 losses, and your eliminated! 😵\n")
    time.sleep(2)
    print("Good Luck!\n")
    time.sleep(1)
def player_hand():
    player_move = input("What's your move: (r)ock, (p)aper, or (s)cissors?\n>>  ")
    if player_move == 'r':
        return "Rock"
    elif player_move == 'p':
        return "Paper"
    elif player_move == 's':
        return "Scissors"
    else:
        return "invalid move."
def computer_hand():
    hands = ['r', 'p', 's']
    computer_move = random.choice(hands)
    if computer_move == 'r':
        return "Rock"
    elif computer_move == 'p':
        return "Paper"
    elif computer_move == 's':
        return "Scissors"
    else:
        return "COMPUTER MOVE BUG IN COMPUTER HAND FUNCTION"
def win():
    global wins
    print("You won!")
    wins += 1
    print(f"\nTotal wins: {wins}")
    print(f"Total loses: {loses}")
    print(f"Total ties: {ties}")
    time.sleep(1)
def lose():
    global loses
    print("You lost!")
    loses += 1
    print(f"\nTotal wins: {wins}")
    print(f"Total loses: {loses}")
    print(f"Total ties: {ties}")
    time.sleep(1)
def tie():
    global ties
    print("You tied!")
    ties += 1
    print(f"\nTotal wins: {wins}")
    print(f"Total loses: {loses}")
    print(f"Total ties: {ties}")
    time.sleep(1)
def calculate_winner(player_move, computer_move):
    global wins
    global loses
    global ties
    if player_move == computer_move:
        tie()
    elif player_move == 'Rock' and computer_move == 'Paper':
        lose()
    elif player_move == 'Rock' and computer_move == 'Scissors':
        win()
    elif player_move == 'Paper' and computer_move == 'Rock':
        win()
    elif player_move == 'Paper' and computer_move == 'Scissors':
        lose()
    elif player_move == 'Scissors' and computer_move == 'Paper':
        win()
    elif player_move == 's' and computer_move == 'r':
        lose()
    else:
        print('GAME BUG IN CALCULATE WINNER FUNCTION')
# ----------- MAIN LOOP -------------