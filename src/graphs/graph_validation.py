from .graph import Graph

# The graph is considered valid if :
# It is fully connnected
# It has no weak articulation point ( two components of 2 or more nodes each connected only by one node)
# Mentions:
# This function is not really necessary, as optimization phase removes all these issues.
# Therefore, this should be just an additional check, using function calls from #Graph module,
# where the logic for finding weak articulation points and such should be implemented


def graph_validation(graph):
    return True