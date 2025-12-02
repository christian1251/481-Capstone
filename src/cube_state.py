# Represent the cube states using NumPy
import numpy as np
import moves 
from typing import Dict, Tuple
import random
from corner_orient_pdb import load_pdb, pdb_heuristic


class CubeState:
    '''
    Rubik's Cube state representation
    Use 54 element array of ints from 0-5 for colors
    '''

    FACES = ['U', 'D', 'R', 'L', 'F', 'B']
    WHITE, YELLOW, RED, ORANGE, GREEN, BLUE = 0, 1, 2, 3, 4, 5
    COLOR_NAMES = {
        0: "WHITE", 1: "YELLOW", 2: "RED",
        3: "ORANGE", 4: "GREEN", 5: "BLUE"
    }
    HEX_COLOR = [
        '#ffffff', '#FFF700', '#ff0000', '#ff7700', '#00ff00',
        '#0000ff'
    ]   # For matplot3d rendering

    def __init__(self):
        """ Intiialize solved cube with 8 bit int for memory efficiency """
        # U = 0:9, D = 9:18, R = 18:27, L = 27:36, F = 36:45, B = 45:54
        self.state = np.array([i for i in range(6)
                              for _ in range(9)], dtype=np.int8)

        self.corner_orient = [0] * 8
        
        try:
            self.pdb = load_pdb()
        except FileNotFoundError:
            raise RuntimeError(
                "corner_orient.pdb not found. Run build_corner_orient_pdb() first."
            )

    def __repr__(self):
        return f"CubeState({self.state.tolist()})"
    
    def heuristic(self):
        return pdb_heuristic(self, self.pdb)

    def get_faces(self) -> Dict[str, np.ndarray]:
        # This is the orginal idea for the state representation
        # Returns a dict of of 6 sets of 3x3 arrays
        return {
            'U': self.state[0:9].reshape(3, 3),
            'D': self.state[9:18].reshape(3, 3),
            'R': self.state[18:27].reshape(3, 3),
            'L': self.state[27:36].reshape(3, 3),
            'F': self.state[36:45].reshape(3, 3),
            'B': self.state[45:54].reshape(3, 3),
        }

    def print_cube(self):
        """Print unfolded representation of cube"""

        faces = self.get_faces()

        # Print U face
        for row in faces['U']:
            print('      ', ' '.join(str(cell) for cell in row))
        print()

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

    
    def face_slices(self):
        return {
            'U': self.state[0:9],
            'D': self.state[9:18],
            'R': self.state[18:27],
            'L': self.state[27:36],
            'F': self.state[36:45],
            'B': self.state[45:54],
        } 
        
        
    def is_solved(self, silence = True):
        faces = self.face_slices()
        solved = True
        issues = []
        
        for face, values in faces.items():
            face_set = set(values)
            if (len(face_set) > 1):
                issues.append(face)
                solved = False
                
        if not silence:     
            if not solved:
                print(f"---NOT SOLVED---\nUnsolved Faces: {issues}")
            else:
                print("Cube Solved")
            

        return solved

    def scramble(self, length=10, silence = True):
        print("--------------SCRAMBLING CUBE--------------")
        scramble = random.choices(list(moves.MOVES.values()), k=length)
        for move in scramble:
            move(self)
            if not silence:
                 print(f"Applying Move:  {move.__name__} ...")
                 self.print_cube()
               
        print("--------------SCRAMBLE DONE--------------")

