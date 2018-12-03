# from .graph import Graph

# The graph is considered valid if :
# It is fully connnected
# It has no weak articulation point ( two components of 2 or more nodes each connected only by one node)
# Mentions:
# This function is not really necessary, as optimization phase removes all these issues.
# Therefore, this should be just an additional check, using function calls from #Graph module,
# where the logic for finding weak articulation points and such should be implemented


def graph_validation(connections):

    def connected_graph():
        visitedNodes = {}

        def recursive_DFS(currentNode):
            visitedNodes[currentNode] = True
            for node in connections[currentNode]:
                if (str(node) not in visitedNodes):
                    recursive_DFS(str(node))

        firstNode = connections.keys()[0]
        recursive_DFS(firstNode)
        #if number of visited nodes after DFS not equal
        # number of nodes in graph ==> Disconnected graph
        if (len(visitedNodes) != len(connections.keys())):
           return False
        return True

    def weak_articulation_points():
        return False

    if connected_graph() == True and weak_articulation_points() == False:
        return True
    return False

modelGraph = {
    "1": {1, 2, 3},
    "2": {1, 4},
    "3": {1, 4, 5},
    "4": {2, 3},
    "5": {3, 6, 7, 8},
    "6": {5},
    "7": {5},
    "8": {5}
}
print(graph_validation(modelGraph))
# python src/graphs/graph_validation.py
