#  Tic-Tac-Toe with Minimax AI

A terminal-based Tic-Tac-Toe game where the player competes against an unbeatable AI opponent powered by the Minimax algorithm.

## Features

- Clear board display with position guide for easy input
- Human plays as 'X', AI plays as 'O'
- AI uses the Minimax algorithm (plays perfectly — unbeatable)
- Accurate win, loss, and draw detection
- Input validation (rejects invalid and occupied moves)
- Option to replay after game ends

## How the AI Works (Minimax Algorithm)

The Minimax algorithm recursively explores all possible future game states and assumes both players play optimally:

- **Maximizing player (AI - 'O'):** Picks moves that maximize its score.
- **Minimizing player (Human - 'X'):** Assumed to pick moves that minimize the AI's score.
- **Scoring:** +10 for AI win, -10 for human win, 0 for draw.
- **Depth factor:** Prefers winning sooner and losing later.

Since Minimax explores every possibility, the AI is unbeatable. The best outcome a human can achieve is a draw.

## How to Run

```bash
python tictactoe.py
```

No external dependencies required — uses only Python standard library.

## Board Layout

```
  0 | 1 | 2
  ---------
  3 | 4 | 5
  ---------
  6 | 7 | 8
```

Enter a number (0-8) to place your mark on the corresponding cell.

## Example Gameplay

```
  TIC-TAC-TOE with MINIMAX AI

  You are 'X' and the AI is 'O'.
  You go first! Enter a position number (0-8).

--- Your Turn (X) ---
Your move (0-8): 4

   |   |          |   |
  -----------     -----------
   | X |          | X |
  -----------     -----------
   |   |          |   |

--- AI's Turn (O) ---
AI is thinking...
AI plays at position 0

 O |   |        O |   |
  -----------     -----------
   | X |          | X |
  -----------     -----------
   |   |          |   |
```

## Technologies

- Python 3.x
- Minimax algorithm with backtracking

github repo : https://github.com/iittjjee2024/TIC-TAC-TOE.git