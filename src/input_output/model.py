class Model:
    def __init__(self, cubes):
        self.cubes = cubes
    def __str__(self):
        modelToStr = ""
        for cube in self.cubes:
            modelToStr = modelToStr + str(cube) + "\n"
        return modelToStr
    def __repr__(self):
        return str(self)
    
