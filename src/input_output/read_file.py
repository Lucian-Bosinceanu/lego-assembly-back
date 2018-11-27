import json
import sys
import os

from .point3d import *

def read_file():
    path = sys.argv[1]
    cubes = []
    try:
        with open(path, 'r') as file:
            jsonData = json.load(file)
        for point in jsonData["cubes"]:
            color = point["color"]
            if point["color"] is None:
                color = "#FFFFFF"
            cubes.append(Point3D(point["x"], point["y"], point["z"], point["color"]))
    except IOError as err:
        print(err.args)
    return cubes
