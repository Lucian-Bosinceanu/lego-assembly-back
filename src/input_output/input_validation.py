import sys
import string

def input_validation(shape):
    if len(shape.cubes) == 0:
        sys.exit("Please provide at least 1 cube")
    if len(shape.cubes) > 5000:
        sys.exit("The amount of cubes must be <= 5000")
    if 0 not in shape.cubes and 0 not in shape.cubes[0] and 0 not in shape.cubes[0][0]:
        sys.exit("No cube with x=0, y=0, z=0 has been found")
    for x in shape.cubes:
            for y in shape.cubes[x]:
                if y < 0:
                    sys.exit("Y must always be > 0")
                for z in shape.cubes[x][y]:
                    if not(all(c in string.hexdigits for c in shape.cubes[x][y][z].color[1:])):
                      sys.exit("A cube's color field is not in HEXA")  
    
    return True

    
