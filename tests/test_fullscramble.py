from cube_state import CubeState
from moves import MOVES
import random
import numpy as np


def test_full_shuffle(length=20):
    cube = CubeState()
    scramble = random.choices(list(MOVES.values()), k=length)
    for move in scramble:
        move(cube)

    # Validate all colors 0-5
    assert set(cube.state) <= set(range(6)), "Invalid color values in cube state!"
    print(f"[OK] Cube valid after {length} random moves.")


if __name__ == "__main__":
    test_full_shuffle()
