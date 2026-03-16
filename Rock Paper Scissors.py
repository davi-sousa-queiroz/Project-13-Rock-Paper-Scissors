# ------------ IMPORTS --------------
import random
import time
# --------- GAME VARIABLES ----------
symbol_values = {
    'rock' : 1,
    'paper' : 2,
    'scissors' : 3
}
your_hand = []

opponent_hand = []

wins = 0

loses = 0

ties = 0

score = 0
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
# ----------- MAIN LOOP -------------