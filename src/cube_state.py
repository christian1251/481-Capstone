# Represent the cube states using NumPy
import numpy as np
from typing import Dict, Tuple


class CubeState:
    '''
    Rubik's Cube state representation
    Use 54 element array of ints from 0-5 for colors
    '''

    FACES = ['U', 'R', 'F', 'D', 'L', 'B']
    RED, WHITE, BLUE, GREEN, YELLOW, ORANGE = 0, 1, 2, 3, 4, 5
    COLOR_NAMES = {0: "RED", 1: "WHITE", 2: "BLUE",
                   3: "GREEN", 4: "YELLOW", 5: "ORANGE"}
    HEX_COLOR = ['#ff0000', '#ffffff', '#0000ff', '#00ff00',
                 "#FFF700", "#ff7700"]  # For matplot3d rendering

    def __init__(self):
        """ Intiialize solved cube with 8 bit int for memory efficiency """
        # U = 0:8 , R = 9:17, F = 18:26, D = 27:35, L = 36:44, B = 45:53
        self.state = np.array([i for i in range(6)
                              for _ in range(9)], dtype=np.int8)

    def repr(self):
        return f"CubeState({self.state.tolist()})"

    def get_faces(self) -> Dict[str, np.ndarray]:
        # This is the orginal idea for the state representation
        # Returns a dict of of 6 sets of 3x3 arrays
        return {
            'U': self.state[0:9].reshape(3, 3),
            'R': self.state[9:18].reshape(3, 3),
            'F': self.state[18:27].reshape(3, 3),
            'D': self.state[27:36].reshape(3, 3),
            'L': self.state[36:45].reshape(3, 3),
            'B': self.state[45:54].reshape(3, 3),
        }

    def print_cube(self):
        """Print unfolded representation of cube"""

        faces = self.get_faces()
        # Print U face
        for row in faces['U']:
            print('      ', ' '.join(str(cell) for cell in row))
        print()

        # Print L, F, R, B faces side by side
        for i in range(3):
            print(
                ' '.join(str(cell) for cell in faces['L'][i]),
                ' '.join(str(cell) for cell in faces['F'][i]),
                ' '.join(str(cell) for cell in faces['R'][i]),
                ' '.join(str(cell) for cell in faces['B'][i])
            )
        print()

        # Print D face
        for row in faces['D']:
            print('      ', ' '.join(str(cell) for cell in row))
