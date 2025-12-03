import numpy as np
from corner_orient_pdb import build_corner_move_table

_corner_moves = build_corner_move_table()

# Face indices in cube.state
# U = 0:9, D = 9:18, R = 18:27, L = 27:36, F = 36:45, B = 45:54


def U(cube):
    cube.state[0:9] = np.rot90(cube.state[0:9].reshape(3, 3), k=3).reshape(9)
    f_row = cube.state[36:39].copy()
    r_row = cube.state[18:21].copy()
    b_row = cube.state[45:48].copy()
    l_row = cube.state[27:30].copy()
    cube.state[36:39] = l_row
    cube.state[18:21] = f_row
    cube.state[45:48] = r_row
    cube.state[27:30] = b_row
    cube.corner_orient = _corner_moves["U"](cube.corner_orient)


def Uprime(cube):
    for _ in range(3):
        U(cube)


def D(cube):
    cube.state[9:18] = np.rot90(cube.state[9:18].reshape(3, 3), k=3).reshape(9)
    f_row = cube.state[42:45].copy()
    r_row = cube.state[24:27].copy()
    b_row = cube.state[51:54].copy()
    l_row = cube.state[33:36].copy()
    cube.state[42:45] = r_row
    cube.state[24:27] = b_row
    cube.state[51:54] = l_row
    cube.state[33:36] = f_row
    cube.corner_orient = _corner_moves["D"](cube.corner_orient)


def Dprime(cube):
    for _ in range(3):
        D(cube)


def L(cube):
    cube.state[27:36] = np.rot90(cube.state[27:36].reshape(3, 3), k=3).reshape(9)
    u_col = cube.state[[0, 3, 6]].copy()
    f_col = cube.state[[36, 39, 42]].copy()
    d_col = cube.state[[9, 12, 15]].copy()
    b_col = cube.state[[47, 50, 53]].copy()

    cube.state[[0, 3, 6]] = b_col[::-1]
    cube.state[[36, 39, 42]] = u_col
    cube.state[[9, 12, 15]] = f_col
    cube.state[[47, 50, 53]] = d_col[::-1]

    cube.corner_orient = _corner_moves["L"](cube.corner_orient)


def Lprime(cube):
    for _ in range(3):
        L(cube)


def R(cube):
    cube.state[18:27] = np.rot90(cube.state[18:27].reshape(3, 3), k=3).reshape(9)
    u_col = cube.state[[2, 5, 8]].copy()
    f_col = cube.state[[38, 41, 44]].copy()
    d_col = cube.state[[11, 14, 17]].copy()
    b_col = cube.state[[45, 48, 51]].copy() 

    cube.state[[2, 5, 8]]    = f_col
    cube.state[[38, 41, 44]] = d_col
    cube.state[[11, 14, 17]] = b_col[::-1]
    cube.state[[45, 48, 51]] = u_col[::-1]

    cube.corner_orient = _corner_moves["R"](cube.corner_orient)


def Rprime(cube):
    for _ in range(3):
        R(cube)


def F(cube):
    cube.state[36:45] = np.rot90(cube.state[36:45].reshape(3, 3), k=3).reshape(9)
    u_row = cube.state[6:9].copy()
    l_col = cube.state[[29, 32, 35]].copy()
    d_row = cube.state[9:12].copy()
    r_col = cube.state[[18, 21, 24]].copy()

    cube.state[6:9] = l_col[::-1]
    cube.state[[18, 21, 24]] = u_row
    cube.state[9:12] = r_col[::-1]
    cube.state[[29, 32, 35]] = d_row

    cube.corner_orient = _corner_moves["F"](cube.corner_orient)


def Fprime(cube):
    for _ in range(3):
        F(cube)


def B(cube):
    cube.state[45:54] = np.rot90(cube.state[45:54].reshape(3, 3), k=3).reshape(9)
    u_row = cube.state[0:3].copy()
    r_col = cube.state[[20, 23, 26]].copy()
    d_row = cube.state[15:18].copy()
    l_col = cube.state[[27, 30, 33]].copy()

    cube.state[0:3] = r_col[::-1]
    cube.state[[27, 30, 33]] = u_row
    cube.state[15:18] = l_col[::-1]
    cube.state[[20, 23, 26]] = d_row

    cube.corner_orient = _corner_moves["B"](cube.corner_orient)


def Bprime(cube):
    for _ in range(3):
        B(cube)


# Aliases
U_prime = Uprime
D_prime = Dprime
L_prime = Lprime
R_prime = Rprime
F_prime = Fprime
B_prime = Bprime

MOVES = {
    "U": U,
    "U'": U_prime,
    "D": D,
    "D'": D_prime,
    "L": L,
    "L'": L_prime,
    "R": R,
    "R'": R_prime,
    "F": F,
    "F'": F_prime,
    "B": B,
    "B'": B_prime,
}

# Inverse lookup table for undo_move()
INVERSE = {
    "U": "U'", "U'": "U",
    "D": "D'", "D'": "D",
    "L": "L'", "L'": "L",
    "R": "R'", "R'": "R",
    "F": "F'", "F'": "F",
    "B": "B'", "B'": "B",
}