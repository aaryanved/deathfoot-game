import random
from Sequences.attack import attack
from Sequences.defend import defend

pp = 0
bp = 0

print("Welcome to Deathfoot!")
print("You are the player, and the computer is the opponent.")
print("You will take turns to play, and the first player to reach 5 points wins.")
print("Time to do a Coin flip! Guess 1 or 2 to see who starts.")
print("")
try:
    ip = int(input("Your guess: "))
    print("")
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

for i in range(10):
    if turn:
        pp = attack(pp)
    else:
        bp = defend(bp)
    # Display points after every 2 rounds
    if (i + 1) % 2 == 0:
        print(f"After {i + 1} rounds: Player Points = {pp}, BOT Points = {bp}")
        print("")
    if pp > 5:
        print("Player wins by a Clean Swipe!")
        break
    elif bp > 5:
        print("Bot wins by a Clean Swipe!")
        break
    turn = not turn
else:
    if pp == 5 and bp == 5:
        print("It's a perfect split! (0.2461 probability!)")
    elif pp > bp:
        print("Player wins with higher points!")
    elif bp > pp:
        print("BOT wins with higher points!")
    else:
        print("It's a draw!")