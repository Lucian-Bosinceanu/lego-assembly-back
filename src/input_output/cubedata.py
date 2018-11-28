from math import sqrt

class CubeData( object ):
    def __init__(self, color, id):
        self.color = color
        self.id = id
        if self.color is None :
            self.color = '#FFFFFF'
    def __str__(self):
       return str(self.color) + " " + str(self.id)
    def __repr__(self):
        return str(self)
