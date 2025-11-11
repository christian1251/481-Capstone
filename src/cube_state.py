# Represent the cube states using NumPy
import numpy as np
from typing import Dict, Tuple

class CubeState:
   
    RED, WHITE, BLUE, GREEN, YELLOW, ORANGE = 0, 1, 2, 3, 4, 5
    
    COLOR_NAMES = {
        0 : "RED", 1 : "WHITE", 2 : "BLUE", 3 : "GREEN", 4 : "YELLOW", 5 : "ORANGE"
    }
    
    def __init__(self):
        """ 
        Intiialize solved cube with 8 bit int for memory efficiency
        """
        self.faces = {
            'U' : np.full((3,3), self.RED, np.int8),      # 0 - Red
            'D' : np.full((3,3), self.WHITE, np.int8),      # 1 - White
            'L' : np.full((3,3), self.BLUE, np.int8),      # 2 - Blue
            'R' : np.full((3,3), self.GREEN, np.int8),      # 3 - Green
            'F' : np.full((3,3), self.YELLOW, np.int8),      # 4 - Yellow
            'B' : np.full((3,3), self.ORANGE, np.int8)       # 5 - Orange
        }
        
    def print_cube(self):
        """Print unfolded representation of cube"""
        def face_to_str(face):
            return '\n'.join(' '.join(str(cell) for cell in row) for row in face)
        
        # Print U face
        for row in self.faces['U']:
            print('      ', ' '.join(str(cell) for cell in row))
        print()
        
        # Print L, F, R, B faces side by side
        for i in range(3):
            print(
                ' '.join(str(cell) for cell in self.faces['L'][i]),
                ' '.join(str(cell) for cell in self.faces['F'][i]),
                ' '.join(str(cell) for cell in self.faces['R'][i]),
                ' '.join(str(cell) for cell in self.faces['B'][i])
            )
        print()
        
        # Print D face
        for row in self.faces['D']:
            print('      ', ' '.join(str(cell) for cell in row))