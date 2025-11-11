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
        r = [-10, 10]
        for s, e in combinations(np.array(list(product(r, r, r))), 2):
            if np.sum(np.abs(s-e)) == r[1]-r[0]:
                ax.plot3D(*zip(s, e), color="w")
                
        
        # TODO: Make this properly display each cube in the Rubiks Cube
        for i, (z, zdir) in enumerate(product([-2, 2], ['x', 'y', 'z'])):
            side = Rectangle((-2, -2), 4, 4, facecolor=self.cube.colors[i])
            ax.add_patch(side)
            art3d.pathpatch_2d_to_3d(side, z=z, zdir=zdir)
            
        plt.axis("off")
        plt.show()
