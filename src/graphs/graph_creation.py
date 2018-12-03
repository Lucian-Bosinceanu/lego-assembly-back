from .graph import Graph
from collections import defaultdict

# Idea for creation :
# Iterate through the shape, for each node (different cube id):
#   - check neighbours for all cubes (position i j k-1 in merged object for each cube of each piece)
#   - add neighbours to list (by id)

def graph_creation(merged):

    connections = defaultdict(list)

    # for i in merged.cubes:
    #     for j in merged.cubes[i]:
    #         for k in merged.cubes[i][j]:
    #             id = merged.cubes[i][j][k].id
    #             if id not in connections.keys():
    #                 try:
    #                     connections[id].append(merged.cubes[i][j][k - 1].id)
    #                 except:
    #                     pass

    for piece in merged.pieces:
        for i in piece.cubes:
            for j in piece.cubes[i]:
                for k in piece.cubes[i][j]:
                    id = piece.cubes[i][j][k].id
                    if id not in connections.keys():
                        try:
                            connections[id].append(piece.cubes[i][j][k - 1].id)
                        except:
                            pass

    # print(str(connections.keys()) + " " + str(connections.items()))

    return Graph(merged.cubes, connections)