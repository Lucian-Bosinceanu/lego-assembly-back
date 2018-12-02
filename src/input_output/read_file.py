import json
import sys
import os
from collections import defaultdict

from .cubedata import *

def read_file():
    path = sys.argv[1]
    cubes = defaultdict(lambda: defaultdict(dict))
    try:
        with open(path, 'r') as file:
            jsonData = json.load(file)
        if len(jsonData) > 1:
            sys.exit("The input doesn't respect the json format")
        if "cubes" not in jsonData:
            sys.exit("Incorrect name of array")
        cubesLen = len(jsonData["cubes"])
        #cubes = [[[0 for x in range(cubesLen)] for y in range(cubesLen)] for z in range(cubesLen)]
        minX = float("inf")
        minZ = float("inf")
        for cube in jsonData["cubes"]:
            if "x" not in cube:
                sys.exit("X coordinate missing from cube")
            if "y" not in cube:
                sys.exit("Y coordinate missing from cube")
            if "z" not in cube:
                sys.exit("Z coordinate missing from cube")
            if cube["x"] < 0 and cube["x"] < minX:
                minX = cube["x"]
            if cube["z"] < 0 and cube["z"] < minZ:
                minZ = cube["z"]
        id = 0
        for cube in jsonData["cubes"]:
            if minX < 0:
                cube["x"] = cube["x"] + (-minX)
            if minZ < 0:
                cube["z"] = cube["z"] + (-minZ)
            if "color" not in cube:
                sys.exit("Oops, a cube doesn't have the color field. Each cube must have it")
            color = cube["color"]
            if cube["color"] is None:
                color = "#FFFFFF"
            if cube["x"] in cubes and cube["y"] in cubes[cube["x"]] and cube["z"] in cubes[cube["x"]][cube["y"]]:
                sys.exit("Oops, duplicate elements in array have been found")
            cubes[cube["x"]][cube["y"]][cube["z"]] = CubeData(color, id)
            id = id + 1
    except IOError as err:
        sys.exit(err.args)
    return cubes
