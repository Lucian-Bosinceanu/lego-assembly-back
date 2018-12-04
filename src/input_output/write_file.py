import json
import sys
import os

from collections import OrderedDict
from cubedata import CubeData

def write_file(cubes):
  #import the standard pieces  
  with open("scLego.json", 'r') as file:
    standardPieces = json.load(file)
  #create a new dictionary where the key is the id + color and the value is a tuple of coordinates
  dictionary= dict()
  for x in cubes:
     for y in cubes[x]:
        for z in cubes[x][y]:
          if(str(cubes[x][y][z].id)+'-'+cubes[x][y][z].color in dictionary):
              dictionary[str(cubes[x][y][z].id)+'-'+cubes[x][y][z].color].append((x,y,z))  
          else:
              dictionary[str(cubes[x][y][z].id)+'-'+cubes[x][y][z].color]=[(x,y,z)]
  #sort the tuples by y,z,x            
  for key in dictionary:
    dictionary[key].sort(key=lambda x: (x[1],x[2],x[0]))
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
       rotation=''
       for i in range(1,len(dictionary[key])):
          a=abs(int(x)-int(dictionary[key][i][0]))
          b=abs(int(y)-int(dictionary[key][i][1]))
          c=abs(int(z)-int(dictionary[key][i][2]))
          dic={'x':a,'y':b,'z':c}
          coord.append(dic)
       if(a<c):
         rotation="90"
       else:
         rotation="0"
       for piece in range(0,len(standardPieces["pieces"])):
           if(coord == standardPieces["pieces"][piece]["structure"]):
              if(standardPieces["pieces"][piece] not in usedPieces["pieces"]):
                usedPieces['pieces'].append(standardPieces["pieces"][piece])   
              dictionary[key+'-'+standardPieces["pieces"][piece]["name"]+'-'+rotation] = dictionary.pop(key)
              
 #sort the tuples by y,x,z to get the coordonates of the piece 
  for key in dictionary:
    dictionary[key].sort(key=lambda x: (x[1],x[0],x[2]))

 #sort the dictionary to build the sculpture bottom-up
  newDictionary= OrderedDict(sorted(dictionary.items(), key=lambda x: x[1][0]))
  dictionary=dict(newDictionary)  
  
  orderPieces= dict()
  orderPieces['order']=[]

#getting the assembling order of pieces 
  for key in dictionary:
      v=key.split('-')
      output=dict()
      output["piece-name"]=v[2]
      poz=dict()
      poz["x"]=dictionary[key][0][0]
      poz["y"]=dictionary[key][0][1]
      poz["z"]=dictionary[key][0][2]
      output["position"]=poz
      orderPieces['order'].append(output)
      output["rotation"]=v[3]
      output["color"]=v[1]

 #union of the first two dictionaries 
  usedPieces.update(orderPieces)

  json_string = json.dumps(usedPieces)
  JsonOutput = open("JsonOutput.json","w+") 
  JsonOutput.write(json_string) 
  JsonOutput.close() 
