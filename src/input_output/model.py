class Model:
    def __init__(self, cubes):
        self.cubes = cubes
    def __str__(self):
        for cube in cubes:
            print(cube)
    def __repr__(self):
        return str(self)
    
