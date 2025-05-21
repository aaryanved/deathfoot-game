import random

pp = 0  # Player points
bp = 0  # Bot points

print("Welcome to Deathfoot!")

# Coin flip to decide who starts
print("Coin flip! Guess 1 or 2 to see who starts.")
try:
    user_guess = int(input("Your guess (1 or 2): "))
except ValueError:
    print("Invalid input. Exiting.")
    exit(0)

coin = random.randint(1, 2)
if user_guess == coin:
    print("You guessed correctly! You start first.")
    turn = "player"
else:
    print("Bot starts first!")
    turn = "bot"

def player_turn():
    global pp
    try:
        n = int(input("Enter a number (1-3): "))
    except ValueError:
        print("Invalid input.")
        return False
    if n < 1 or n > 3:
        print("Game crash because of your foolishness.")
        exit(0)
    m = random.randint(1, 3)
    if n == m:
        print("You Scored!")
        pp += 1
        return True
    else:
        print("You didn't score.")
        return False

def bot_turn():
    global bp
    n = random.randint(1, 3)
    m = random.randint(1, 3)
    print(f"Bot chooses {n}.")
    if n == m:
        print("Bot Scored!")
        bp += 1
        return True
    else:
        print("Bot didn't score.")
        return False

# Main game loop
while True:
    print(f"\nScore: Player {pp} - Bot {bp}")
    if pp > 5:
        print("Player wins!")
        break
    if bp > 5:
        print("Bot wins!")
        break
    if pp == 5 and bp == 5:
        print("Sudden death! First to score wins.")
        while True:
            if turn == "player":
                scored = player_turn()
                if scored:
                    print("Player wins in sudden death!")
                    break
                turn = "bot"
            else:
                scored = bot_turn()
                if scored:
                    print("Bot wins in sudden death!")
                    break
                turn = "player"
        break
    if turn == "player":
        player_turn()
        turn = "bot"
    else:
        bot_turn()
        turn = "player"