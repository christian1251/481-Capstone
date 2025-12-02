# Entry point
from cube_state import CubeState
import moves
from gui import Renderer

def main():
    print("hello world")

    cube = CubeState()
    
    cube.is_solved()
    cube.print_cube()
    
    cube.scramble(1, True)
    cube.print_cube()
    # graphics = Renderer(cube)
    # graphics.start()
    

if __name__ == "__main__":
    main()
