# Entry point
from cube_state import CubeState
import moves
from gui import Renderer
from algo import Solver

def main():
    print("hello world")

    cube = CubeState()
    
    cube.is_solved()
    cube.print_cube()
    
    # graphics = Renderer(cube)
    # graphics.start()
    
    # moves.F(cube)
    # moves.U(cube)
    # moves.R(cube)

    # solver = Solver(cube)
    # solution = solver.IDA_STAR(10)
    # print("Solution:", solution)
    
if __name__ == "__main__":
    main()
