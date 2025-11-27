from cube_state import CubeState
from corner_orient_pdb import pdb_heuristic, load_pdb
from moves import MOVES

# Load PDB once
pdb = load_pdb()


# Count stickers not matching the majority color of each face
def misplaced_sticker_heuristic(cube: CubeState) -> int:
    faces = cube.face_slices()
    misplaced = 0
    for face, values in faces.items():
        counts = {}
        for color in values:
            counts[color] = counts.get(color, 0) + 1
        majority = max(counts.values())
        misplaced += 9 - majority
    return misplaced


# Combine corner orientation + misplaced stickers
def combined_heuristic(cube: CubeState) -> int:

    return pdb_heuristic(cube, pdb) + misplaced_sticker_heuristic(cube)


# Lower is better
def rank_moves(cube: CubeState) -> dict:

    ranking = {}
    for move_name, move_func in MOVES.items():
        # Simulate move
        new_cube = CubeState()
        new_cube.state = cube.state.copy()
        new_cube.corner_orient = cube.corner_orient.copy()
        move_func(new_cube)

        # Compute heuristic after the move
        h = combined_heuristic(new_cube)
        ranking[move_name] = h

    return dict(sorted(ranking.items(), key=lambda kv: kv[1]))


if __name__ == "__main__":
    cube = CubeState()
    print("Current heuristic:", combined_heuristic(cube))
    ranking = rank_moves(cube)
    print("Move ranking on solved cube:")
    for move, h in ranking.items():
        print(f"{move}: {h}")
