# Main gui implementation

from matplotlib.widgets import Button
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import mpl_toolkits.mplot3d.art3d as art3d
from cube_state import CubeState
import moves
from algo import Solver
import threading
import copy
from move_eval import evaluate_move

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
        # Regular Moves
        axes_btn = plt.axes([0.80, 0.01, 0.1, 0.075])
        bU = Button(axes_btn, 'U')
        bU.on_clicked(self._on_U)
        
        axes_btn = plt.axes([0.70, 0.01, 0.1, 0.075])
        bD = Button(axes_btn, 'D')
        bD.on_clicked(self._on_D)

        axes_btn = plt.axes([0.60, 0.01, 0.1, 0.075])
        bL = Button(axes_btn, 'L')
        bL.on_clicked(self._on_L)

        axes_btn = plt.axes([0.50, 0.01, 0.1, 0.075])
        bR = Button(axes_btn, 'R')
        bR.on_clicked(self._on_R)

        axes_btn = plt.axes([0.40, 0.01, 0.1, 0.075])
        bF = Button(axes_btn, 'F')
        bF.on_clicked(self._on_F)
        
        axes_btn = plt.axes([0.30, 0.01, 0.1, 0.075])
        bB = Button(axes_btn, 'B')
        bB.on_clicked(self._on_B)
        
        # Inverse Buttons
        axes_btn = plt.axes([0.80, 0.09, 0.1, 0.075])
        bUPrime = Button(axes_btn, "U'")
        bUPrime.on_clicked(self._on_UPrime)
        
        axes_btn = plt.axes([0.70, 0.09, 0.1, 0.075])
        bDPrime = Button(axes_btn, "D'")
        bDPrime.on_clicked(self._on_DPrime)

        axes_btn = plt.axes([0.60, 0.09, 0.1, 0.075])
        bLPrime = Button(axes_btn, "L'")
        bLPrime.on_clicked(self._on_LPrime)

        axes_btn = plt.axes([0.50, 0.09, 0.1, 0.075])
        bRPrime = Button(axes_btn, "R'")
        bRPrime.on_clicked(self._on_RPrime)

        axes_btn = plt.axes([0.40, 0.09, 0.1, 0.075])
        bFPrime = Button(axes_btn, "F'")
        bFPrime.on_clicked(self._on_FPrime)
        
        axes_btn = plt.axes([0.30, 0.09, 0.1, 0.075])
        bBPrime = Button(axes_btn, "B'")
        bBPrime.on_clicked(self._on_BPrime)
        
        
        axes_btn = plt.axes([0.10, 0.01, 0.1, 0.075])
        bScramble = Button(axes_btn, 'Scramble')
        bScramble.on_clicked(self._on_Scramble)
        
        axes_btn = plt.axes([0.0, 0.01, 0.1, 0.075])
        bSolve = Button(axes_btn, 'Solve')
        bSolve.on_clicked(self._on_Solve)
    
        plt.show()
    # button callbacks
    def _on_U(self, event):
        evaluate_move(self.cube, "U")
        moves.U(self.cube)
        self._redraw()

    def _on_D(self, event):
        evaluate_move(self.cube, "D")
        moves.D(self.cube)
        self._redraw()

    def _on_R(self, event):
        evaluate_move(self.cube, "R")
        moves.R(self.cube)
        self._redraw()

    def _on_L(self, event):
        evaluate_move(self.cube, "L")
        moves.L(self.cube)
        self._redraw()

    def _on_F(self, event):
        evaluate_move(self.cube, "F")
        moves.F(self.cube)
        self._redraw()

    def _on_B(self, event):
        evaluate_move(self.cube, "B")
        moves.B(self.cube)
        self._redraw()
        
    def _on_UPrime(self, event):
        evaluate_move(self.cube, "U'")
        moves.Uprime(self.cube)
        self._redraw()

    def _on_DPrime(self, event):
        evaluate_move(self.cube, "D'")
        moves.Dprime(self.cube)
        self._redraw()

    def _on_RPrime(self, event):
        evaluate_move(self.cube, "R'")
        moves.Rprime(self.cube)
        self._redraw()

    def _on_LPrime(self, event):
        evaluate_move(self.cube, "L'")
        moves.Lprime(self.cube)
        self._redraw()

    def _on_FPrime(self, event):
        evaluate_move(self.cube, "F'")
        moves.Fprime(self.cube)
        self._redraw()

    def _on_BPrime(self, event):
        evaluate_move(self.cube, "B'")
        moves.Bprime(self.cube)
        self._redraw()
        
    def _on_Scramble(self, event):
        self.cube.scramble(5, False)
        self._redraw()
        
    def _on_Solve(self, event):
        threading.Thread(target=self._solve_thread).start()

    def _solve_thread(self):
        cube_copy = copy.deepcopy(self.cube)
        solver = Solver(cube_copy)
        solution = solver.IDA_STAR(10)
        print("Solution:", solution)

    def _redraw(self):
        """Clear and redraw cube"""
        print(20 * "-")
        self.ax.cla()
        self._draw_cube(self.ax)
        self.fig.canvas.draw_idle()
        self.cube.print_cube()
        print(20 * "-")
        

    def _draw_cube(self, ax):

        faces = self.cube.get_faces()

        # camera wireframe cube
        r = [-1.5, 1.5]
        for s, e in combinations(np.array(list(product(r, r, r))), 2):
            if np.sum(np.abs(s - e)) == r[1] - r[0]:
                ax.plot3D(*zip(s, e), color="w")

        # Face origins and movement vectors
            face_vectors = {
            
            'U': (np.array([-1.5,  1.5,  1.5], dtype=float),
                  np.array([1.0,  0.0,  0.0], dtype=float),   
                  np.array([0.0,  0.0, -1.0], dtype=float)), 

         
            'D': (np.array([-1.5, -1.5, -1.5], dtype=float),
                  np.array([1.0,  0.0,  0.0], dtype=float),   
                  np.array([0.0,  0.0,  1.0], dtype=float)), 

           
            'F': (np.array([-1.5, -1.5,  1.5], dtype=float),
                  np.array([1.0,  0.0,  0.0], dtype=float),   
                  np.array([0.0,  1.0,  0.0], dtype=float)), 

           
            'B': (np.array([ 1.5, -1.5, -1.5], dtype=float),
                  np.array([-1.0,  0.0,  0.0], dtype=float), 
                  np.array([ 0.0,  1.0,  0.0], dtype=float)),

            'R': (np.array([ 1.5, -1.5,  1.5], dtype=float),
                  np.array([0.0,  0.0, -1.0], dtype=float),  
                  np.array([0.0,  1.0,  0.0], dtype=float)),  

            
            'L': (np.array([-1.5, -1.5, -1.5], dtype=float),
                  np.array([0.0,  0.0,  1.0], dtype=float),   
                  np.array([0.0,  1.0,  0.0], dtype=float)),  
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


        ax.set_aspect("auto")
        ax.set_autoscale_on(True)