from .graph import Graph
from collections import defaultdict

# Idea for creation :
# Iterate through the shape, for each node (different cube id) define :
#   - A list of neighbours (by index)
#   - coordinates and color (model)

def graph_creation(merged):

    connections = defaultdict(list)

    for i in merged.cubes:
        for j in merged.cubes[i]:
            for k in merged.cubes[i][j]:
                id = merged.cubes[i][j][k].id
                if id not in connections.keys():
                    k1 = 0
                    while k1 < k:
                        k1 += 1
                        try:
                            connections[id].append(merged.cubes[i][j][k1].id)
                        except:
                            pass
                    

                            
                
    print(str(connections.keys()) + " " + str(connections.items()))