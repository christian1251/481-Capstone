# Algorithms: 
#   - IDDFS algorithm
#   - IDA* algorithm

# Could make our own or use AIMA from prev hw
import time
from moves import INVERSE

class Solver:
    
    def __init__(self, cube):
        self.cube = cube
        
    
    def IDA_STAR(self, max_depth):
        print("Solving...")
        INF = float('inf')

        h_func = getattr(self.cube, "heuristic", None)
        if h_func is None:
            def h_func(_): return 0

        bound = self.cube.heuristic()
        path = []

        def search(state, g, bound, last_move=None):
            f = g + state.heuristic()
            if f > bound:
                return f
            if state.is_solved():
                return True
            if (max_depth is not None) and (g >= max_depth):
                return INF

            min_t = INF
            for move in state.get_moves():
                
                if last_move is not None and INVERSE.get(move) == last_move:
                    continue
                
                if last_move is not None and move[0] == last_move[0]:
                    continue

                
                state.do_move(move)
                path.append(move)
                
                t = search(state, g + 1, bound)
                
                if t is True:
                    return True
                
                if t < min_t:
                    min_t = t
                    
                path.pop()
                state.undo_move(move)
            return min_t

        while True:
            start = time.time()
            t = search(self.cube, 0, bound)
            if t is True:
                end = time.time()
                length = end - start
                print(f"Total Time to Solve: {length}")
                return list(path)
            if t == INF:
                return None
            bound = t

    def IDDFS(self, max_depth, goal_state):
        path = []

        def dls(state, depth):
            if state == goal_state:
                return True
            if (max_depth is not None) and (depth <= 0):
                return False

            for move in state.get_moves():
                state.do_move(move)
                path.append(move)
                if dls(state, depth - 1):
                    return True
                path.pop()
                state.undo_move(move)
            return False
        for depth in range(max_depth + 1):
            if dls(self.cube, depth):
                return list(path)
        return None