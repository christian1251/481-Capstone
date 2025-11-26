# Main gui implementation

from matplotlib.widgets import Button
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import mpl_toolkits.mplot3d.art3d as art3d
from cube_state import CubeState
import moves

class Renderer:
    def __init__(self, cube):
        self.cube = cube
        self.fig = None
        self.ax = None

    def start(self):
        """Create env"""
        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(projection='3d')

        self._draw_cube(self.ax)

        # Buttons
        axes_btn = plt.axes([0.81, 0.01, 0.1, 0.075])
        bU = Button(axes_btn, 'U')
        bU.on_clicked(self._on_U)
        
        axes_btn = plt.axes([0.60, 0.01, 0.1, 0.075])
        bL = Button(axes_btn, 'L')
        bL.on_clicked(self._on_L)

        plt.show()

    # button callbacks
    def _on_U(self, event):
        moves.U(self.cube)
        self._redraw()

    # button callbacks
    def _on_L(self, event):
        moves.L(self.cube)
        self._redraw()

    def _redraw(self):
        """Clear and redraw cube"""
        self.ax.cla()
        self._draw_cube(self.ax)
        self.fig.canvas.draw_idle()
        self.cube.print_cube()


    def _draw_cube(self, ax):

        faces = self.cube.get_faces()

        # camera wireframe cube
        r = [0, 2]
        for s, e in combinations(np.array(list(product(r, r, r))), 2):
            if np.sum(np.abs(s - e)) == r[1] - r[0]:
                ax.plot3D(*zip(s, e), color="w")

        # Face origins and movement vectors
        face_vectors = {
            'U': (np.array([0, 3, 0], dtype=float),
                  np.array([1, 0, 0], dtype=float),
                  np.array([0, 0, 1], dtype=float)),
            'D': (np.array([0, 0, 0], dtype=float),
                  np.array([1, 0, 0], dtype=float),
                  np.array([0, 0, 1], dtype=float)),
            'F': (np.array([0, 0, 3], dtype=float),
                  np.array([1, 0, 0], dtype=float),
                  np.array([0, 1, 0], dtype=float)),
            'B': (np.array([3, 0, 0], dtype=float),
                  np.array([-1, 0, 0], dtype=float),
                  np.array([0, 1, 0], dtype=float)),
            'R': (np.array([3, 0, 3], dtype=float),
                  np.array([0, 0, -1], dtype=float),
                  np.array([0, 1, 0], dtype=float)),
            'L': (np.array([0, 0, 0], dtype=float),
                  np.array([0, 0, 1], dtype=float),
                  np.array([0, 1, 0], dtype=float)),
        }

        # draw helper
        def draw_face(key, origin, u_vec, v_vec):
            face = faces[key]
            for row in range(3):
                for col in range(3):

                    # bottom-left corner of tile
                    base = origin + u_vec * col + v_vec * (2 - row)

                    square = [
                        base,
                        base + u_vec,
                        base + u_vec + v_vec,
                        base + v_vec
                    ]

                    poly = art3d.Poly3DCollection([square])
                    poly.set_facecolor(CubeState.HEX_COLOR[face[row, col]])
                    poly.set_edgecolor("k")
                    ax.add_collection3d(poly)

        # draw all faces
        for face_key, vecs in face_vectors.items():
            draw_face(face_key, *vecs)

        # nice camera
        ax.set_aspect("auto")
        ax.set_autoscale_on(True)