from .graph import Graph

# Idea for implementation:
# Based on the graph, search for weak articulation points and connectivity problems
# Solve them in the shape object
# For weak articulation points :
# 1. Create a set containing the brick that is represented by the weak node, and it's neighbours
# 2. Break all these cubes into 1x1x1 cubes again (voxels)
# 3. Merge them again using the random strategy
# 4. Go to step 1 untill no weak points can be found
# Mentions:
# After each iteration ( fix of an articulation point), the graph should be updated


def graph_optimization(graph,shape):
    pass