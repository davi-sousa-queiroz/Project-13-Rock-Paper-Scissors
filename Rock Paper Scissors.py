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

def player_move():
    your_move = input("What's your move: (r)ock (p)aper or (s)cissors\n>>").lower()
    if your_move == 'r':
        your_hand.append(your_move)
    elif your_move == 'p':
        your_hand.append(your_move)
    elif your_move == 's':
        your_hand.append(your_move)
    else:
        print("Invalid move! Try again.")

def computer_move():
    computer_move = random.choice(your_hand)
    if computer_move == 'r':
        opponent_hand.append(computer_move)
    elif computer_move == 'p':
        opponent_hand.append(computer_move)
    elif computer_move == 's':
        opponent_hand.append(computer_move)
    else:
        print("ERROR: COMPUTER MOVE BUG")

# ----------- MAIN LOOP -------------