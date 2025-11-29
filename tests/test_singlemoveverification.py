from moves import U, Uprime, D, Dprime, L, Lprime, R, Rprime, F, Fprime, B, Bprime
from cube_state import CubeState

MOVES = [U, D, L, R, F, B]
INVERSES = [Uprime, Dprime, Lprime, Rprime, Fprime, Bprime]


def single_move_test():
    for move, inv in zip(MOVES, INVERSES):
        cube = CubeState()
        before = cube.state.copy()
        move(cube)
        inv(cube)
        assert (
            cube.state == before
        ).all(), f"Move {move.__name__} then inverse did NOT restore cube!"
        print(f"[OK] {move.__name__} then {inv.__name__} restores cube.")


if __name__ == "__main__":
    single_move_test()
