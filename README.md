# Memory Game

A two-player terminal-based memory matching game written in Python. Test your memory skills by matching pairs of symbols on a 4x5 grid and compete to score the most points.

## Features

- Two-player gameplay
- Randomized symbol placement
- Score tracking
- Input validation
- Cross-platform support (Windows, macOS, and Linux)
- No external dependencies required

## How to Play

The game board is a 4x5 grid of coordinates (A1–D5), each hiding a symbol:

```text
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

- Python 3.6 or higher

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

## Example Menu

```text
Welcome to Memory!

1. How to Play
2. Start Game
3. Exit
```

## Technical Details

- **Language**: Python 3
- **Dependencies**: Python Standard Library only (no external packages required)
- **Grid Size**: 4 rows × 5 columns = 20 cells (10 pairs)
- **Symbols**: `! @ # $ % & ? = + ~`

## Project Structure

```
memory-game/
├── .gitattributes          # Git attributes configuration
├── .gitignore              # Git ignore rules
├── LICENSE                 # Project license
├── README.md               # Project documentation
├── memory-game.py          # Main game script
└── requirements.txt        # Python dependencies
```

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available for personal and educational use.
