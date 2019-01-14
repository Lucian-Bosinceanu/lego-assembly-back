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
    limit = 3                                                                           # limit is the maximum number of weak points admitted in the graph
    max_attempts = 30
    attempts = 0
    graph = None

    while not done and attempts < max_attempts:                                         # while the final structure still isn't right
        if algorithm == "genetic": merge_test(shape)                                    # merge the input from file, creating a basic lego structure
        else: merge_cubes(shape)                                                        # merge the input using the greedy algorithm
        graph = graph_creation(shape)                                                   # remove weak articulation points, merge eventual subgraphs
        done = graph_validation(graph.connections, limit) or shape_has_one_level(shape) # if graph is stable or shape has only 1 level, we can stop
        attempts += 1
    
    if (attempts == max_attempts and not done):
        print("Output generation failed!")
        exit()
    else:
        write_file(shape)
        print("Output generation completed after", attempts, "attempts.")
        exit()
