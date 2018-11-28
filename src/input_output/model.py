class Model:
    def __init__(self, cubes):
        self.cubes = cubes
    def __str__(self):
        modelToStr = ""
<<<<<<< HEAD
        for x in self.cubes:
            for y in self.cubes[x]:
                for z in self.cubes[x][y]:
                    modelToStr = modelToStr + "x=" + str(x) + " y=" + str(y) + " z=" + str(z) + " " + str(self.cubes[x][y][z]) + "\n"
=======
        for cube in self.cubes:
            modelToStr = modelToStr + str(cube) + "\n"
>>>>>>> c15c5771970befcbf58be89a7ec2034daef851d0
        return modelToStr
    def __repr__(self):
        return str(self)
    def distFrom(x1, y1, z1, x2, y2, z2):
        return sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    
