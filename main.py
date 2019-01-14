#!/usr/bin/env python3
from src.ui import *
from src.input_output import *
from src.conversion import *
from src.graphs import *
from src.generation import *
from src.generation.new_merge import *

if __name__ == "__main__":
    algorithm = arguments()
    shape = Model(read_file())
    input_validation(shape)
    print(shape)

    done = False
    limit = 3                                               # limit is the maximum number of weak points admitted in the graph
    graph = None

    while not done:                                         # while the final structure still isn't right
        if algorithm == "genetic": merge_test(shape)       # merge the input from file, creating a basic lego structure
        else: merge_cubes(shape)                            # merge the input using the greedy algorithm
        graph = graph_creation(shape)                       # remove weak articulation points, merge eventual subgraphs
        done = graph_validation(graph.connections, limit)   # if graph is stable, we can stop

    write_file(shape)
    print("Output generation completed")
    exit()
