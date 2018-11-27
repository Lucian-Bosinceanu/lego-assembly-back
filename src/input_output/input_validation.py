import sys

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
    return True

    
