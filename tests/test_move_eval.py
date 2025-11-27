from move_eval import CubeState, combined_heuristic, rank_moves
from moves import MOVES


def test_solved_cube_heuristic():
    cube = CubeState()
    h = combined_heuristic(cube)
    assert h >= 0, f"Heuristic should be non-negative, got {h}"
    ranking = rank_moves(cube)
    assert isinstance(ranking, dict), "Move ranking should return a dict"
    print(f"[OK] Solved cube heuristic = {h}")
    print(f"[OK] Move ranking keys = {list(ranking.keys())}")


def test_heuristic_after_move():
    cube = CubeState()
    MOVES["U"](cube)
    h = combined_heuristic(cube)
    assert h > 0, f"Heuristic should increase after U move, got {h}"
    ranking = rank_moves(cube)
    best_move = next(iter(ranking))
    print(f"[OK] Heuristic after U = {h}, best move suggested = {best_move}")


def test_small_scramble():
    cube = CubeState()
    scramble = ["U", "R", "F"]
    for move in scramble:
        MOVES[move](cube)
    h = combined_heuristic(cube)
    ranking = rank_moves(cube)
    print(f"[OK] Heuristic after scramble {scramble} = {h}")
    print("Move ranking after scramble:")
    for move, score in ranking.items():
        print(f"{move}: {score}")


if __name__ == "__main__":
    test_solved_cube_heuristic()
    test_heuristic_after_move()
    test_small_scramble()
