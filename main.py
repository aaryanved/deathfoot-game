import random

pp = 0
bp = 0
print("Welcome to Deathfoot!")
print("You are the player, and the computer is the opponent.")
print("You will take turns to play, and the first player to reach 5 points wins.")
print("Time to do a Coin flip! Guess 1 or 2 to see who starts.")
try:
    ip = int(input("Your guess: "))
except ValueError:
    print("Invalid input. Exiting.")
    exit(0)
coin = random.randint(1, 2)
if ip == coin:
    print("You guessed correctly! You start first.")
    turn = True
else:
    print("Bot starts first!")
    turn = False