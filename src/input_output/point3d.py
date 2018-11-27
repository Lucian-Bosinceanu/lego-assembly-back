class Point3D( object ):
    def __init__( self, x, y, z, color ):
        self.x, self.y, self.z = x, y, z
        self.color = color
        if self.color == 'null' :
            self.color = '#FFFFFF'
    def __str__(self):
       return str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(self.color)
    def __repr__(self):
        return str(self)
    def distFrom( self, x, y, z ):
        return math.sqrt( (self.x-x)**2 + (self.y-y)**2 + (self.z-z)**2 )