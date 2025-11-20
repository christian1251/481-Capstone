# Main gui implementation

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import mpl_toolkits.mplot3d.art3d as art3d
from cube_state import CubeState
from matplotlib.patches import Rectangle, Circle, PathPatch

class Renderer:
    
    
    def __init__(self, cube):
        self.cube = cube
        
    def render_cube(self):
        '''
        Use Matplotlib3d to display the in 3d
        '''
        fig = plt.figure()
        
        ax = fig.add_subplot(projection = '3d')
        
        ax.set_aspect("auto")
        ax.set_autoscale_on(True)
        
        # Render Camera zoom
        r = [0, 2]
        for s, e in combinations(np.array(list(product(r, r, r))), 2):
            if np.sum(np.abs(s-e)) == r[1]-r[0]:
                ax.plot3D(*zip(s, e), color="w")
                
        
        faces = self.cube.get_faces()

        # origin = starting corner of the face
        # u_vec = direction to move when increasing column index
        # v_vec  = direction to move when increasing row index 
        face_vectors = {
            # matplot wants floats 
            'U': (np.array([0, 3, 0], dtype=float), np.array([1, 0, 0], dtype=float), np.array([0, 0, 1], dtype=float)),
            'D': (np.array([0, 0, 0], dtype=float), np.array([1, 0, 0], dtype=float), np.array([0, 0, 1], dtype=float)),
            'F': (np.array([0, 0, 3], dtype=float), np.array([1, 0, 0], dtype=float), np.array([0, 1, 0], dtype=float)),
            'B': (np.array([3, 0, 0], dtype=float), np.array([-1, 0, 0], dtype=float), np.array([0, 1, 0], dtype=float)),
            'R': (np.array([3, 0, 3], dtype=float), np.array([0, 0, -1], dtype=float), np.array([0, 1, 0], dtype=float)),
            'L': (np.array([0, 0, 0], dtype=float), np.array([0, 0, 1], dtype=float), np.array([0, 1, 0], dtype=float)),
        }

        def draw_face(key, origin, u_vec, v_vec):
            # 3×3 array of colors for the face
            face = faces[key]

            for row in range(3):
                for col in range(3):

                    # this computes the bottom left coord of the quare
                    base = origin + u_vec * col + v_vec * (2 - row)

                    # 4 vertices of sqaure
                    square = [base,
                        base + u_vec,
                        base + u_vec + v_vec,
                        base + v_vec
                    ]

                    # create square
                    poly = art3d.Poly3DCollection([square])
                    poly.set_facecolor(CubeState.HEX_COLOR[face[row, col]])
                    poly.set_edgecolor("k") 

                    # add tile to the plot
                    ax.add_collection3d(poly)

        # draw each face
        for face_key, vectors in face_vectors.items():
            draw_face(face_key, *vectors)
            
        plt.show()