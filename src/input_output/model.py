import math
from typing import Tuple
import src.input_output.cubedata as cube


class Model:
    def __init__(self, cubes):
        self.cubes = cubes
        self.piece_size = dict()
    
    def __str__(self):
        modelToStr = ""
        for x in self.cubes:
            for y in self.cubes[x]:
                for z in self.cubes[x][y]:
                    modelToStr = modelToStr + "x=" + str(x) + " y=" + str(y) + " z=" + str(z) + " " + str(self.cubes[x][y][z]) + "\n"
        return modelToStr
    
    def __repr__(self):
        return str(self)

    def distFrom(self, x1, y1, z1, x2, y2, z2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

    def has_cube_at(self, x, y, z):
        return x in self.cubes and y in self.cubes[x] and z in self.cubes[x][y]

    def get_cube_at(self, coord: Tuple[int, int, int]) -> cube:
        return self.cubes[coord[0]][coord[1]][coord[2]]
