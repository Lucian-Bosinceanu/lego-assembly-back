import json
import sys
import os

from cubedata import CubeData

#import the standard pieces
def write_file():
  path= r"C:\Users\Roxana\Desktop\scLego.json"  
  with open(path, 'r') as file:
    standardPieces = json.load(file)
  #print(standardPieces)
  cubes = {'1': {'1':  {'1':  CubeData('red',1)}, '2': { '2': CubeData('blue',2)} }}
  #create a new dictionary where the key is the id + color and the value is a tuple of coordinates
  dictionary= dict()
  for x in cubes:
     for y in cubes[x]:
        for z in cubes[x][y]:
          if(str(cubes[x][y][z].id)+'-'+cubes[x][y][z].color in dictionary):
              dictionary[str(cubes[x][y][z].id)+'-'+cubes[x][y][z].color].append((x,y,z))  
          else:
              dictionary[str(cubes[x][y][z].id)+'-'+cubes[x][y][z].color]=[(x,y,z)]
  
write_file()