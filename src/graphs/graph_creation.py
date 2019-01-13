from .graph import Graph
from collections import defaultdict

# Idea for creation :
# Iterate through the shape, for each node (different cube id):
#   - check neighbours for all cubes (position i j k-1 in merged object for each cube of each piece)
#   - add neighbours to list (by id)


def graph_creation(merged):
    connections = defaultdict(set)

    for x in merged.cubes:
        for y in merged.cubes[x]:
            if y - 1 in merged.cubes[x]:
                for z in merged.cubes[x][y]:
                    if z not in merged.cubes[x][y-1]:
                        continue
                    cube_id = merged.cubes[x][y][z].id
                    adjacent_id = merged.cubes[x][y-1][z].id
                    connections[cube_id].add(adjacent_id)
                    connections[adjacent_id].add(cube_id)

    for key in connections.keys():
        print(key, ":", connections[key])

    return Graph(merged.cubes, connections)
