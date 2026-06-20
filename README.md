# Memory Game 🎮

A two-player terminal-based memory card matching game written in Python. Test your memory skills by matching pairs of symbols on a 4x5 grid!

## How to Play

The game board is a 4x5 grid of coordinates (A1–D5), each hiding a unique symbol:

```
  1 2 3 4 5
A * * * * *
B * * * * *
C * * * * *
D * * * * *
```

### Game Rules

- **10 Pairs**: There are 10 pairs of matching symbols hidden on the board
- **Take Turns**: Players alternate turns
- **Make Matches**: On each turn, select two coordinates to reveal symbols
  - If they match, you earn 1 point and take another turn
  - If they don't match, it becomes the other player's turn
- **Remove Matched Pairs**: Successfully matched pairs are removed from the board
- **Win Condition**: The player with the most matches when all pairs are found wins!

## Installation

### Requirements
- Python 3.x

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/charliecleere/memory-game.git
   cd memory-game
   ```

2. Run the game:
   ```bash
   python memory-game.py
   ```

## Usage

When you start the game, you'll see a menu with three options:

```
Welcome to Memory!

1. How to Play
2. Start Game
3. Exit
```

- **Option 1**: View detailed instructions
- **Option 2**: Start a new two-player game
- **Option 3**: Exit the game

### During Gameplay

1. Player 1 and Player 2 take turns
2. When prompted, enter a coordinate (e.g., `A1`, `B4`, `D5`)
3. The game will reveal your two selections
4. If they match, you keep your turn and earn a point
5. If they don't match, control passes to the other player
6. The game ends when all 10 pairs are matched

## Features

- ✨ Cross-platform support (Windows, macOS, Linux)
- 🎯 Score tracking for both players
- 🎲 Randomized symbol placement
- 🎪 Visual grid display
- ⏱️ Pause between turns for fairness
- 🧹 Input buffer clearing to prevent accidental entries during pauses

## Technical Details

- **Language**: Python 3
- **Dependencies**: Standard library only (no external packages required)
- **Grid Size**: 4 rows × 5 columns = 20 cells (10 pairs)
- **Symbols**: `!`, `@`, `#`, `$`, `%`, `&`, `?`, `=`, `+`, `~`

## Project Structure

```
memory-game/
├── memory-game.py          # Main game script
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
└── .gitattributes          # Git attributes configuration
```

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes!

## License

This project is open source and available for personal and educational use.

---

**Enjoy the game!** 🎉
