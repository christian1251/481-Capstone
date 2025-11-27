from copy import deepcopy
from cube_state import CubeState
import moves

move_pairs = [
    ("U", moves.U, "U'", moves.U_prime),
    ("D", moves.D, "D'", moves.D_prime),
    ("L", moves.L, "L'", moves.L_prime),
    ("R", moves.R, "R'", moves.R_prime),
    ("F", moves.F, "F'", moves.F_prime),
    ("B", moves.B, "B'", moves.B_prime),
]


def identical_cube(c1, c2):
    return (
        c1.state.tolist() == c2.state.tolist() and c1.corner_orient == c2.corner_orient
    )


def run_inverse_test():
    print("== Inverse-move tests (move then inverse should restore solved cube) ==")
    errors = []
    for name, move, inv_name, inv in move_pairs:
        cube = CubeState()
        before = deepcopy(cube)
        move(cube)
        inv(cube)
        if not identical_cube(before, cube):
            errors.append(name)
            print(f"[FAIL] {name} then {inv_name} did NOT restore solved cube.")
        else:
            print(f"[OK]   {name} then {inv_name} restored solved cube.")
    if not errors:
        print("All inverse tests passed!")
    else:
        print("Failing moves:", errors)


def run_single_move_inspect():
    print("\n== Single-move inspection: shows affected slices before/after ==")
    for name, move, _, _ in move_pairs:
        cube = CubeState()
        print(f"\n--- {name} ---")
        print("Before (face slices):")
        for k, v in cube.face_slices().items():
            print(f"{k}: {v.tolist()}")
        move(cube)
        print("After (face slices):")
        for k, v in cube.face_slices().items():
            print(f"{k}: {v.tolist()}")
        # reset for next move


if __name__ == "__main__":
    run_inverse_test()
    run_single_move_inspect()
