import json
import sys
import os

from cubedata import CubeData

def write_file():
  #import the standard pieces  
  path= r"C:\Users\Roxana\Desktop\scLego.json"  
  with open(path, 'r') as file:
    standardPieces = json.load(file)
  #print(standardPieces)
  cubes = {'1': {'1':  {'1':  CubeData('red',1)}},'2':{ '1': { '1': CubeData('red',1)} }} #a example of dictionary
  #create a new dictionary where the key is the id + color and the value is a tuple of coordinates
  dictionary= dict()
  for x in cubes:
     for y in cubes[x]:
        for z in cubes[x][y]:
          if(str(cubes[x][y][z].id)+'-'+cubes[x][y][z].color in dictionary):
              dictionary[str(cubes[x][y][z].id)+'-'+cubes[x][y][z].color].append((x,y,z))  
          else:
              dictionary[str(cubes[x][y][z].id)+'-'+cubes[x][y][z].color]=[(x,y,z)]
  #sort the tuples by y,x,z            
  for key in dictionary:
    dictionary[key].sort(key=lambda x: (x[2],x[0],x[1]))
  usedPieces= dict()
  usedPieces['pieces']=[]
  #iterate through the dictionary and find the standard pieces we use in the sculpture
  for key in dictionary:
      v=key.split('-')
      if len(v)==2:
       x,y,z=dictionary[key][0]
       dic= {'x': 0, 'y':0,'z':0}
       coord= list()
       coord.append(dic)
       for i in range(1,len(dictionary[key])):
          a=abs(int(x)-int(dictionary[key][i][0]))
          b=abs(int(y)-int(dictionary[key][i][1]))
          c=abs(int(z)-int(dictionary[key][i][2]))
          dic={'x':a,'y':b,'z':c}
          coord.append(dic)
       for piece in range(0,len(standardPieces["pieces"])):
           if(coord == standardPieces["pieces"][piece]["structure"]):
              if(standardPieces["pieces"][piece] not in usedPieces["pieces"]):
                usedPieces['pieces'].append(standardPieces["pieces"][piece])   
              dictionary[key+'-'+standardPieces["pieces"][piece]["name"]] = dictionary.pop(key)
              
  print(usedPieces)
  print(dictionary) 
  
  orderPieces= dict()
  orderPieces['order']=[]

write_file()