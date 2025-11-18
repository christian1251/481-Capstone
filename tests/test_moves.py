from cube_state import CubeState
import moves
import numpy as np
import random


# ------------------- Basic helpers -------------------
def test_inverse(move, inv):
    cube = CubeState()
    before = cube.state.copy()
    move(cube)
    inv(cube)
    after = cube.state.copy()
    return np.array_equal(before, after)


def test_four_cycles(move):
    cube = CubeState()
    before = cube.state.copy()
    for _ in range(4):
        move(cube)
    after = cube.state.copy()
    return np.array_equal(before, after)


def test_random_scramble(num_moves=50):
    moves_list = [
        (moves.U, moves.U_prime),
        (moves.D, moves.D_prime),
        (moves.L, moves.L_prime),
        (moves.R, moves.R_prime),
        (moves.F, moves.F_prime),
        (moves.B, moves.B_prime),
    ]

    cube = CubeState()
    before = cube.state.copy()

    # Random sequence
    seq = [random.choice(moves_list) for _ in range(num_moves)]

    # Apply moves
    for m, _ in seq:
        m(cube)

    # Undo moves in reverse
    for _, inv in reversed(seq):
        inv(cube)

    after = cube.state.copy()
    return np.array_equal(before, after)


# ------------------- Run tests -------------------
if __name__ == "__main__":
    move_pairs = [
        ("U", moves.U, moves.U_prime),
        ("D", moves.D, moves.D_prime),
        ("L", moves.L, moves.L_prime),
        ("R", moves.R, moves.R_prime),
        ("F", moves.F, moves.F_prime),
        ("B", moves.B, moves.B_prime),
    ]

    print("=== Inverse move tests ===")
    for name, m, inv in move_pairs:
        print(f"{name} / {name}'", "PASS" if test_inverse(m, inv) else "FAIL")

    print("\n=== Four-turn tests ===")
    for name, m, _ in move_pairs:
        print(f"{name}^4", "PASS" if test_four_cycles(m) else "FAIL")

    print("\n=== Random scramble test ===")
    print("Random scramble 50 moves:", "PASS" if test_random_scramble() else "FAIL")
