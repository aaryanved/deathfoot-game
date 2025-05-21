# Deathfoot Game

Deathfoot is a simple turn-based Python game where you play against the computer in a race to reach 5 points first. The game involves a coin flip to decide who starts, and then alternates between attack and defend moves.

## How to Play

1. **Start the Game**  
   Run the game using:
   ```
   python main.py
   ```

2. **Coin Flip**  
   Guess 1 or 2 to see who starts first.

3. **Turns**  
   - If you start, you attack first; otherwise, the bot defends.
   - Each turn, either you attack or the bot defends, and points are updated.

4. **Winning**  
   - The first to cross 5 points wins.
   - If neither crosses 5 after 10 rounds, the player with more points wins.
   - If both reach 5, it's a draw.

## Files

- `main.py` - Main game logic.
- `Sequences/attack.py` - Attack sequence logic.
- `Sequences/defend.py` - Defend sequence logic.

## Requirements

- Python 3.6 or higher

## Example Output

```
Welcome to Deathfoot!
You are the player, and the computer is the opponent.
You will take turns to play, and the first player to reach 5 points wins.
Time to do a Coin flip! Guess 1 or 2 to see who starts.

Your guess: 1

You guessed correctly! You start first.
After 2 rounds: Player Points = 1, BOT Points = 0

...
```

Enjoy playing Deathfoot!