# Battleship

**Language:** English · [Русский](README_RU.md)

Complete the three TODOs directly in `game.py`. Run the game and focused checks after each change.

**Input:** Enter row column (1–10). Fleet: 4 singles, 3 doubles, 2 triples, 1 quadruple. Ships cannot touch, even diagonally.

## How to play

### Battleship: find every hidden ship

Play against a hidden fleet on a 10×10 board. Choose a cell to fire at it. The program remembers your shots and reports miss, hit or sunk. There is no opponent shooting back in this project.

| Ship length | Number of ships | Occupied cells |
| --- | --- | --- |
| 1 | 4 | 4 |
| 2 | 3 | 6 |
| 3 | 2 | 6 |
| 4 | 1 | 4 |

That is 10 ships occupying 20 cells. Each ship is a straight horizontal or vertical segment. Ships cannot overlap or touch, including diagonally.

### A two-cell ship is not sunk after one hit

| Shot | Result |
| --- | --- |
| Ship occupies (2,2) and (2,3). Fire 2 2. | Hit: one cell remains unhit. |
| Fire 2 2 again. | Rejected: this shot was already made. |
| Fire 2 3. | Sunk: both cells are now hit. |

Win by sinking all ten ships. A hit on one ship does not reveal the others. Enter row column; rows and columns run from 1 to 10.

## Before coding
Choose a simple data representation, then write the solution order before coding.

### Data representation

| What we represent | Python type | Why it fits |
|---|---|---|
| Coordinate | `tuple[int, int]` | A shot and every ship cell use the same row/column representation. |
| Ship | `set[tuple[int, int]]` | A ship is the unique set of cells it occupies. |
| Fleet | `list[set[tuple[int, int]]]` | Keeps the ships separate so each one can be tested for sinking. |
| Accepted shots | `set[tuple[int, int]]` | Prevents repeated accepted shots and supports membership/subset checks. |

### Solution workflow

1. Reject shots outside the board and coordinates already in the shot set.
2. Add an accepted shot exactly once.
3. Classify it as hit or miss by checking membership in the ship sets.
4. A ship is sunk when all of its cells are in the accepted-shot set; finish when this is true for every ship.

## Implementation

Open `game.py` and complete the three TODOs in order. The exact contract is written beside each TODO; keep the rest of the game unchanged unless the task requires it.

## Run and check

```bash
python main.py
python practice_checks.py
python tests.py
python submission_check.py
```

`practice_checks.py` supports incremental work. `tests.py` checks the full game after all three TODOs are complete.
