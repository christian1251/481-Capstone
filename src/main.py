# Entry point
from cube_state import CubeState
import moves
import numpy as np
from gui import Renderer
from algo import Solver
from corner_orient_pdb import build_corner_orient_pdb, save_pdb
from splash import print_rubixtutortext


def main():

    print_rubixtutortext()
    print("Building PDB")
    pdb = build_corner_orient_pdb()
    save_pdb(pdb)
    print(f"Done.")

    cube = CubeState()

    cube.print_cube()

    graphics = Renderer(cube)
    graphics.start()

    # moves.F(cube)
    # moves.U(cube) 
    # moves.R(cube)
    # moves.Bprime(cube)
    # moves.U(cube)
    # moves.L(cube)

    # solver = Solver(cube)
    # solution = solver.IDA_STAR(10)
    # print("Solution:", solution)


if __name__ == "__main__":
    main()
