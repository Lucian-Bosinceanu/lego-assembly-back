#!/usr/bin/env python3
from src.ui import *
from src.input_output import *
from src.conversion import *
from src.graphs import *
from src.generation import *

if __name__ == "__main__":
    # UI()
    shape = Model(read_file())
    print(shape)
    input_validation(shape)
    #
    # done = False
    # graph = None
    # while not done:
    #     generated = generate()
    #     graph = graph_creation(generated)
    #     done = graph_validation(graph)
    #
    # output = convert_graph(graph)
    # write_file(output)
    exit()
