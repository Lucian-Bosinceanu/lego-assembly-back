# from .graph import Graph

# The graph is considered valid if :
# It is fully connnected
# It has no weak articulation point ( two components of 2 or more nodes each connected only by one node)
# Mentions:
# This function is not really necessary, as optimization phase removes all these issues.
# Therefore, this should be just an additional check, using function calls from #Graph module,
# where the logic for finding weak articulation points and such should be implemented


def graph_validation(connections, limit):
    if (len(connections.items()) == 0): return False      # we don't accept empty graphs
    connectionsKeys = list(connections)

    def DFS(startingNode, ignore = -1):
        visitedNodes = {}

        def recursive_DFS(currentNode):
            visitedNodes[currentNode] = True
            for node in connections[currentNode]:
                if node == ignore: continue
                if (node not in visitedNodes):
                    recursive_DFS(node)
        
        recursive_DFS(startingNode)
        return visitedNodes

    def connected_graph():
        firstNode = connectionsKeys[0]
        visitedNodes = DFS(firstNode)
        #if number of visited nodes after DFS not equal
        # number of nodes in graph ==> Disconnected graph
        if (len(visitedNodes) != len(connectionsKeys)):
           return False
        return True

    def weak_articulation_points():
        weakPoints = []

        visitedNodes = DFS(connectionsKeys[1], connectionsKeys[0])
        if len(visitedNodes) != len(connectionsKeys) - 1:
            weakPoints.append(connectionsKeys[0])

        currentNode = 1
        while currentNode < len(connectionsKeys):
            visitedNodes = DFS(connectionsKeys[0], connectionsKeys[currentNode])
            if len(visitedNodes) != len(connectionsKeys) - 1:
                weakPoints.append(connectionsKeys[currentNode])
            currentNode += 1

        print(weakPoints)
        if len(weakPoints) > limit:
            return False
        return True

    if connected_graph() == True and weak_articulation_points() == True:
        return True
    return False

def shape_has_one_level(shape) -> bool:
    return True if len(shape.get_levels()) == 1 else False

# modelGraph = {
#     1: {1, 2, 3, 9},
#     2: {1, 4, 9},
#     3: {1, 4, 5},
#     4: {2, 3},
#     5: {3, 6, 7, 8},
#     6: {5},
#     7: {5},
#     8: {5},
#     9: {
#         1, 2
#     }
# }
# print(graph_validation(modelGraph, 3))
# python src/graphs/graph_validation.py
