# Generate the possible moves (U, D, L, R, F, B)
from cube_state import CubeState
import numpy as np

# U = 0:9, D = 9:18, R = 18:27, L = 27:36, F = 36:45, B = 45:54
  
def U(cube):
    # Peserve copy of prev state
    faces = cube.get_faces()
    
    # Rotate U face 
    rotated_u = np.rot90(faces['U'], k=3)
    cube.state[0:9] = rotated_u.reshape(9)
    
    # Rotate neighboring faces
    temp= cube.state[36:39].copy()
    
    cube.state[36:39] = cube.state[18:21]
    cube.state[18:21] = cube.state[45:48]
    cube.state[45:48] = cube.state[27:30]
    cube.state[27:30] = temp
    
    # Reshape back into state
    
    
    