import sys
<<<<<<< HEAD
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
    
=======

visited = dict()

def checkIfConex(cubes, poz):
    if poz in visited:
        return 0
    visited[poz] = True
    visitedCubes = 1
    for i in range (0, len(cubes)):
        print(cubes[poz].distFrom(cubes[i].x, cubes[i].y, cubes[i].z))
        if i != poz and cubes[poz].distFrom(cubes[i].x, cubes[i].y, cubes[i].z) == 1:
            visitedCubes += checkIfConex(cubes, i)
    return visitedCubes


def input_validation(shape):
    if len(shape.cubes) > 5000:
        sys.exit("The amount of cubes must be <= 5000")
    if checkIfConex(shape.cubes, 0) != len(shape.cubes):
        sys.exit("The input doesn't have all its blocks conex")
    for i in range(0, len(shape.cubes)):
        if shape.cubes[i].y < 0:
            sys.exit("The Y of a cube must always be > 0")
>>>>>>> c15c5771970befcbf58be89a7ec2034daef851d0
    return True

    
