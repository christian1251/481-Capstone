# Generate the possible moves (U, D, L, R, F, B, U', D', L', R', F', B'. No wide moves / slice moves for now due to notation.)
from cube_state import CubeState
import numpy as np
from corner_orient_pdb import build_corner_move_table

_corner_moves = build_corner_move_table()

# U = 0:9, D = 9:18, R = 18:27, L = 27:36, F = 36:45, B = 45:54


# ------------------- U -------------------
def U(cube):
    # Peserve copy of prev state
    faces = cube.get_faces()

    # Rotate U face
    rotated_u = np.rot90(faces["U"], k=3)
    cube.state[0:9] = rotated_u.reshape(9)

    # Rotate neighboring faces
    temp = cube.state[36:39].copy()

    cube.state[36:39] = cube.state[18:21]
    cube.state[18:21] = cube.state[45:48]
    cube.state[45:48] = cube.state[27:30]
    cube.state[27:30] = temp

    cube.corner_orient = _corner_moves["U"](cube.corner_orient)


    # Reshape back into state


def U_prime(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["U"], k=1)
    cube.state[0:9] = rotated.reshape(9)

    temp = cube.state[36:39].copy()
    cube.state[36:39] = cube.state[27:30]
    cube.state[27:30] = cube.state[45:48]
    cube.state[45:48] = cube.state[18:21]
    cube.state[18:21] = temp

    cube.corner_orient = _corner_moves["U'"](cube.corner_orient)


# ------------------- D -------------------
def D(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["D"], k=3)
    cube.state[9:18] = rotated.reshape(9)

    temp = cube.state[42:45].copy()  # F bottom row
    cube.state[42:45] = cube.state[33:36]  # F = L
    cube.state[33:36] = cube.state[48:51]  # L = B
    cube.state[48:51] = cube.state[24:27]  # B = R
    cube.state[24:27] = temp  # R = old F

    cube.corner_orient = _corner_moves["D"](cube.corner_orient)

def D_prime(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["D"], k=1)
    cube.state[9:18] = rotated.reshape(9)

    temp = cube.state[42:45].copy()
    cube.state[42:45] = cube.state[24:27]
    cube.state[24:27] = cube.state[48:51]
    cube.state[48:51] = cube.state[33:36]
    cube.state[33:36] = temp

    cube.corner_orient = _corner_moves["D'"](cube.corner_orient)
# ------------------- L -------------------
def L(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["L"], k=3)
    cube.state[27:36] = rotated.reshape(9)

    temp = cube.state[0:9:3].copy()  # U left column
    cube.state[0:9:3] = cube.state[45:54:3]  # U = B (right col reversed later)
    cube.state[45:54:3] = cube.state[9:18:3]  # B = D
    cube.state[9:18:3] = cube.state[36:45:3]  # D = F
    cube.state[36:45:3] = temp  # F = old U
    cube.corner_orient = _corner_moves["L"](cube.corner_orient)

def L_prime(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["L"], k=1)
    cube.state[27:36] = rotated.reshape(9)

    temp = cube.state[0:9:3].copy()
    cube.state[0:9:3] = cube.state[36:45:3]
    cube.state[36:45:3] = cube.state[9:18:3]
    cube.state[9:18:3] = cube.state[45:54:3]
    cube.state[45:54:3] = temp

    cube.corner_orient = _corner_moves["L'"](cube.corner_orient)
# ------------------- R -------------------
def R(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["R"], k=3)
    cube.state[18:27] = rotated.reshape(9)

    temp = cube.state[2:9:3].copy()  # U right column
    cube.state[2:9:3] = cube.state[36 + 2 : 45 : 3]  # U = F
    cube.state[36 + 2 : 45 : 3] = cube.state[11:18:3]  # F = D
    cube.state[11:18:3] = cube.state[47:54:3]  # D = B
    cube.state[47:54:3] = temp  # B = old U
    cube.corner_orient = _corner_moves["R"](cube.corner_orient)

def R_prime(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["R"], k=1)
    cube.state[18:27] = rotated.reshape(9)

    temp = cube.state[2:9:3].copy()
    cube.state[2:9:3] = cube.state[47:54:3]
    cube.state[47:54:3] = cube.state[11:18:3]
    cube.state[11:18:3] = cube.state[38:45:3]
    cube.state[38:45:3] = temp
    cube.corner_orient = _corner_moves["R'"](cube.corner_orient)

# ------------------- F -------------------
def F(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["F"], k=3)
    cube.state[36:45] = rotated.reshape(9)

    temp = cube.state[6:9].copy()  # U bottom row
    cube.state[6:9] = cube.state[27:36:3][
        ::-1
    ]  # U bottom row = L right column reversed
    cube.state[27:36:3] = cube.state[9:12]  # L right column = D top row
    cube.state[9:12] = cube.state[18:27:3][::-1]  # D top row = R left column reversed
    cube.state[18:27:3] = temp  # R left column = old U bottom row
    cube.corner_orient = _corner_moves["F"](cube.corner_orient)

def F_prime(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["F"], k=1)
    cube.state[36:45] = rotated.reshape(9)

    temp = cube.state[6:9].copy()  # U bottom row
    cube.state[6:9] = cube.state[18:27:3]  # U bottom row = R left column
    cube.state[18:27:3] = cube.state[9:12][::-1]  # R left column = D top row reversed
    cube.state[9:12] = cube.state[27:36:3]  # D top row = L right column
    cube.state[27:36:3] = temp[::-1]  # L right column = old U bottom row reversed
    cube.corner_orient = _corner_moves["F'"](cube.corner_orient)

# ------------------- B -------------------
def B(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["B"], k=3)
    cube.state[45:54] = rotated.reshape(9)

    temp = cube.state[0:3].copy()  # U top row
    cube.state[0:3] = cube.state[18:27:3][::-1]  # U = R right col reversed
    cube.state[18:27:3] = cube.state[15:18]  # R = D bottom row
    cube.state[15:18] = cube.state[27:36:3][::-1]  # D = L left col reversed
    cube.state[27:36:3] = temp  # L = old U

    cube.corner_orient = _corner_moves["B"](cube.corner_orient)

def B_prime(cube):
    faces = cube.get_faces()

    rotated = np.rot90(faces["B"], k=1)
    cube.state[45:54] = rotated.reshape(9)

    temp = cube.state[0:3].copy()
    cube.state[0:3] = cube.state[27:36:3]  # U = L left col
    cube.state[27:36:3] = cube.state[15:18][::-1]  # L = D bottom row reversed
    cube.state[15:18] = cube.state[18:27:3]  # D = R right col
    cube.state[18:27:3] = temp[::-1]  # R = old U reversed
    
    cube.corner_orient = _corner_moves["B'"](cube.corner_orient)

