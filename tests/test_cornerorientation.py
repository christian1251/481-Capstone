from cube_state import CubeState
from corner_orient_pdb import build_corner_orient_pdb, pdb_heuristic
from moves import U, Uprime, D, Dprime, L, Lprime, R, Rprime, F, Fprime, B, Bprime


def test_heuristic():
    pdb = build_corner_orient_pdb()
    cube = CubeState()

    # Solved cube should have heuristic 0
    h = pdb_heuristic(cube, pdb)
    assert h == 0, f"Heuristic for solved cube should be 0, got {h}"

    # Apply moves that twist corners
    for move, inv in [(R, Rprime), (L, Lprime), (F, Fprime), (B, Bprime)]:
        move(cube)
        h2 = pdb_heuristic(cube, pdb)
        assert h2 > 0, f"Heuristic should increase after {move.__name__}, got {h2}"

        # Undo move should restore heuristic
        inv(cube)
        h3 = pdb_heuristic(cube, pdb)
        assert h3 == 0, f"Heuristic after undoing {move.__name__} should be 0, got {h3}"

    print("[OK] Corner orientation heuristic consistent for all twisting moves.")


if __name__ == "__main__":
    test_heuristic()
