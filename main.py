#!/usr/bin/env python3
from src.ui import *
from src.input_output import *
from src.conversion import *
from src.graphs import *
from src.generation import *

if __name__ == "__main__":
    # UI()
    shape = Model(read_file())
    input_validation(shape)
    print(shape)

    # done = False
    # graph = None
    # while not done:                       # while the final structure still isn't right
    #     merged = merge_cubes(shape)       # merge the input from file, creating a basic lego structure
    #     graph = graph_creation(merged)    # create the graph based on the merged structure
    #     graph_optimization(graph,shape)   # remove weak articulation points, merge eventual subgraphs
    #     done = graph_validation(graph)    # if graph is stable, we can stop
    #
    # output = convert_graph(graph)
    # write_file(output)
    exit()
