# Logic for determining "valuable" moves
from cube_state import CubeState

def move_eval(cube):
    '''Counts the number of misplacements'''
    faces = cube.face_slices()
    misplaced = 0

    
    for face, values in faces.items():

        val_array = values

        color_count = {}

        for color in val_array:
            if color not in color_count:
                color_count[color] = 0
            color_count[color] += 1
        
        # This is too prevent hardcoded heuristic checking
        # Any face can be any color in the final solved state
        majority_count = max(color_count.values())

        misplaced += (9 - majority_count)


    return misplaced
