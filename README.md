# 481-Capstone: Brief Description

Rubix Tutor is a program used to solve and recommend valuable moves for a 3x3x3 Rubix cube using a set algorithm. States such as U, D, L, R, F, and B will be defined and stored locally. This project focuses on defining and manipulating cube states with the assistance of libraries such as NumPy and Matplotlib in order to express the cube states visually. Efficient moves are recommended to the player as the player progresses through the puzzle.

# Build and Run Instructions

Clone the Repo:

```sh
 git clone https://github.com/christian1251/481-Capstone.git
```

Ensure that external libraries are installed:

```sh
 pip install matplotlib
 pip install numpy
```

Run program:

```sh
python src/main.py
```

## Team Members

-   Christian Carrillo
-   Adrian Diaz
-   Tommy Le

## Files

### Cube State Representation (cube_state.py)
- Defines all six faces and store cube state
- Added scramble, rotate, and heuristic evaluation functions.

### Cube Moves (moves.py)
- Implemented all basic and inverse moves (U, U', D, D', L, L', R, R', F, F', B, B').
- Moves correctly update corner orientation and can be undone.

### Solving Algorithms (algo.py)
- Implemented IDA* to find optimal move sequences.
- Integrated a heuristic for efficient searching and timing.

### Move Evaluation (move_eval.py)
- Combined misplaced stickers and corner orientation heuristics.
- Ranked possible moves to recommend the most efficient ones.

### Graphical User Interface (gui.py)
- 3D cube visualization with Matplotlib: Buttons for all moves, scramble, and solve functionality.
- Solver integrated to print solution steps with move evaluation

### Corner Orientation Pattern Database (corner_orient_pdb.py)
- Precomputed all corner orientations for faster heuristics.

### /tests
- Set of tests for moves, scrambles, heuristics, move_eval

## Language(s)

-   Python

## Datasets
- No datasets were used for this project
## Libraries / Existing Code

## Algorithm/Approach

IDDFS algorithm and IDA\* algorithm

## Roles and Responsibilities
- Christian: Rendering and GUI, heuristic
- Adrian: Moves, Move Evaluation
- Tommy: Algorithm
