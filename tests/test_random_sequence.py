import numpy as np
import random
from cube_state import CubeState
from moves import MOVES

# Proper inverse mapping
INVERSE_MOVES = {m: (m[:-1] if m.endswith("'") else m + "'") for m in MOVES.keys()}


def random_sequence_test(length: int = 10):
    cube = CubeState()
    original_state = cube.state.copy()
    original_orient = cube.corner_orient.copy()

    move_names = list(MOVES.keys())
    sequence = [random.choice(move_names) for _ in range(length)]
    inverse_sequence = []

    # Apply random moves
    for move in sequence:
        MOVES[move](cube)
        inverse_sequence.insert(0, INVERSE_MOVES[move])

    # Apply inverse moves
    for move in inverse_sequence:
        MOVES[move](cube)

    # Check if fully restored
    state_restored = np.array_equal(cube.state, original_state)
    orient_restored = np.array_equal(cube.corner_orient, original_orient)

    assert state_restored, f"Cube state not restored after {length} moves!"
    assert orient_restored, f"Corner orientation not restored after {length} moves!"

    print(f"[PASS] Cube restored correctly after {length} random moves.")


if __name__ == "__main__":
    for test_len in [5, 10, 20, 50]:
        random_sequence_test(test_len)
