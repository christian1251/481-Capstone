# This file creates a pattern db based on the corner orientations
# Moves to solve corner pieces
# https://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/korfrubik.pdf

from collections import deque
import pickle 
import os
from typing import List, Dict, Callable

PDB_FILENAME = "corner_orient.pdb"

# Total num of possible corner orientations
# Missing the 8th corner because it can be derived by the other 7
NUM_STATES = 3 ** 7 


CORNER_STICKERS = [
    [  2, 18, 38 ],   # URF
    [  0, 36, 29 ],   # UFL
    [  6, 27, 47 ],   # ULB
    [  8, 45, 20 ],   # UBR
    [ 11, 44, 26 ],   # DFR
    [  9, 35, 42 ],   # DLF
    [ 15, 53, 33 ],   # DBL
    [ 17, 24, 51 ],   # DRB
]

def encode_corner_orient(orient: List[int]) -> int:
    '''
    Encode the orientation of the corners into a base 3 int (0-3^7)
    Args will be (0, 1, 2). 
        - 0 = correctly orientation
        - 1 = one twist needed
        - 2 = two twists needed 
    '''

    assert len(orient) == 8
    
    encoded = 0
    for i in range(7):
        o_value = orient[i]
        assert 0 <= o_value <= 2
        encoded = encoded * 3 + o_value


    return encoded

def decode_corner_orient(code: int) -> List[int]:
    '''
    Inverse of the encoding function
    '''

    assert 0 <= code < NUM_STATES
    decoded = [0] * 8 
    
    for i in range(6, -1, -1):
        decoded[i] = code % 3 
        code //= 3

    decoded[7] = (-sum(decoded[:7])) % 3
    return decoded




CornerMove = Callable[[List[int]], List[int]]


def make_move_function(perm: List[int], twist: List[int]) -> CornerMove:
    """
    perm[i] = index of corner that moves into position i.
    twist[i] = how much to ADD (mod 3) to the orientation of the corner
               that ends up in position i.
    """
    assert len(perm) == 8 and len(twist) == 8

    def move_func(orient: List[int]) -> List[int]:
        new = [0] * 8
        for i in range(8):
            c_from = perm[i]
            new[i] = (orient[c_from] + twist[i]) % 3
        return new

    return move_func


def build_corner_move_table() -> Dict[str, CornerMove]:
    """
    Return a dict mapping move names to functions that update corner orientation.
    """

    moves: Dict[str, CornerMove] = {}

    # Example: U / U' (Up face quarter turns)
    # U move cycles the 4 top-layer corners, but DOES NOT change their orientation.
    # Using corner indices [0,1,2,3] = [UFR, URB, UBL, ULF] as an example.
    U_perm  = [1, 2, 3, 0, 4, 5, 6, 7]   # positions 0..3 get cycled
    U_twist = [0] * 8                    # no twist change
    moves["U"] = make_move_function(U_perm, U_twist)

    # U' is the inverse cycle
    Uprime_perm  = [3, 0, 1, 2, 4, 5, 6, 7]
    Uprime_twist = [0] * 8
    moves["U'"] = make_move_function(Uprime_perm, Uprime_twist)

    # D / D' similarly: bottom layer corners cycle, no orientation change.
    D_perm  = [0, 1, 2, 3, 5, 6, 7, 4]
    D_twist = [0] * 8
    moves["D"] = make_move_function(D_perm, D_twist)

    Dprime_perm  = [0, 1, 2, 3, 7, 4, 5, 6]
    Dprime_twist = [0] * 8
    moves["D'"] = make_move_function(Dprime_perm, Dprime_twist)


    R_perm  = [3, 1, 2, 7, 0, 5, 6, 4]
    R_twist = [2, 0, 0, 1, 1, 0, 0, 2]
    moves["R"]  = make_move_function(R_perm, R_twist)
    
    Rprime_perm =  [4, 1, 2, 0, 7, 5, 6, 3]
    Rprime_twist = [1, 0, 0, 2, 2, 0, 0, 1]
    moves["R'"] = make_move_function(Rprime_perm, Rprime_twist)

    L_perm = [0, 5, 1, 3, 4, 6, 2, 7]
    L_twist = [0, 1, 2, 0, 0, 2, 1, 0]
    moves["L"]  = make_move_function(L_perm, L_twist)
    
    Lprime_perm = [0, 2, 6, 3, 4, 1, 5, 7]
    Lprime_twist = [0, 2, 1, 0, 0, 1, 2, 0]
    moves["L'"] = make_move_function(Lprime_perm, Lprime_twist)

    F_perm = [1, 5, 2, 3, 0, 4, 6, 7]
    F_twist = [1, 2, 0, 0, 2, 1, 0, 0]
    moves["F"]  = make_move_function(F_perm, F_twist)

    Fprime_perm = [4, 0, 2, 3, 5, 1, 6, 7]
    Fprime_twist = [2, 1, 0, 0, 1, 2, 0, 0]
    moves["F'"] = make_move_function(Fprime_perm, Fprime_twist)

    B_perm = [0, 1, 6, 2, 4, 5, 7, 3]
    B_twist = [0, 0, 1, 2, 0, 0, 2, 1]
    moves["B"]  = make_move_function(B_perm, B_twist)

    Bprime_perm = [0, 1, 3, 7, 4, 5, 2, 6]
    Bprime_twist = [0, 0, 2, 1, 0, 0, 1, 2]
    moves["B'"] = make_move_function(Bprime_perm, Bprime_twist)

    return moves


def build_corner_orient_pdb() -> List[int]:
    """
    Build the corner-orientation PDB as a list of length NUM_STATES.
    pdb[code] = minimum number of moves to orient all corners 
    Uses bfs
    """
    moves = build_corner_move_table()

    # Initialize PDB with -1 = unknown
    pdb = [-1] * NUM_STATES

    # Start from the solved orientation: all corners orientation 0
    solved_orient = [0] * 8
    root_code = encode_corner_orient(solved_orient)
    pdb[root_code] = 0

    queue = deque([root_code])

    while queue:
        code = queue.popleft()
        orient = decode_corner_orient(code)
        depth = pdb[code]

        # Expand all moves
        for move_name, move_func in moves.items():
            new_orient = move_func(orient)
            new_code = encode_corner_orient(new_orient)

            if pdb[new_code] == -1:
                pdb[new_code] = depth + 1
                queue.append(new_code)

    return pdb


# Save and load pdb
def save_pdb(pdb: List[int], filename: str = PDB_FILENAME) -> None:
    with open(filename, "wb") as f:
        pickle.dump(pdb, f)

def load_pdb(filename: str = PDB_FILENAME) -> List[int]:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"PDB File '{filename}' not found. Build it")
    
    with open(filename, "rb") as f:
        return pickle.load(f)



# Hueristic wrapper
def get_corner_orient_from_cube(cube):
    orient = [0]*8

    for corner_idx, stickers in enumerate(CORNER_STICKERS):
        ref = stickers[0]           # index of reference sticker
        ref_color = cube.state[ref] # actual color currently on that sticker

        # What face is this sticker sitting on
        # Determine by which center color it matches.

        if ref_color == cube.WHITE or ref_color == cube.YELLOW:
            orient[corner_idx] = 0
        elif ref_color == cube.RED or ref_color == cube.ORANGE:
            orient[corner_idx] = 1
        else:  # GREEN or BLUE
            orient[corner_idx] = 2

    return orient


def pdb_heuristic(cube, pdb: List[int]) -> int:
    orientation = get_corner_orient_from_cube(cube)
    code = encode_corner_orient(orientation)
    return pdb[code]


if __name__ == "__main__":
    print("Building PDB")
    pdb = build_corner_orient_pdb()
    save_pdb(pdb)
    print(f"Done. Saved to {PDB_FILENAME}")
    
