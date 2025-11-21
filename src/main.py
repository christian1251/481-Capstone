# Entry point
from cube_state import CubeState
import moves
from gui import Renderer

def main():
    print("hello world")

    cube = CubeState()
    
    cube.is_solved()
    cube.print_cube()
    moves.U(cube)
    cube.is_solved()
    # # cube.print_cube()
    # # moves.U_prime(cube)
    # # cube.print_cube()
    # graphics = Renderer(cube)
    # graphics.render_cube()
    

if __name__ == "__main__":
    main()
