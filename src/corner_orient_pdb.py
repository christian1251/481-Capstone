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

    assert 0 <= code <= NUM_STATES
    decoded = [0] * 8 
    
    for i in range(6, -1, -1):
        decoded[i] = code % 3 
        code //= 3

    decoded[7] = (-sum(decoded[:7])) % 3
    return decoded




