import random
from datetime import datetime
import src.input_output.model as model
import src.input_output.cubedata as cube
from typing import Tuple
from copy import deepcopy

DIRECTIONS = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))


def pick_random_coordinate(randrange):
    random.seed(datetime.now())

    x = random.randrange(0, randrange)
    y = random.randrange(0, randrange)
    z = random.randrange(0, randrange)

    return x, y, z


def pick_random_cube(shape: model):
    coord = pick_random_coordinate(len(shape.cubes))

    while not shape.has_cube_at(coord[0], coord[1], coord[2]):
        coord = pick_random_coordinate(len(shape.cubes))

    return shape.cubes[coord[0]][coord[1]][coord[2]], (coord[0], coord[1], coord[2])


def can_be_merged(cube1: cube, cube2: cube) -> bool:
    return cube1.id != cube2.id and cube1.color == cube2.color 


def get_neighbor_set_for_cube(cube_data, shape):
    neighbor_set = []
    
    data = cube_data[0]
    coord = cube_data[1]

    for direction in DIRECTIONS:
        neighbor = (coord[0] + direction[0], coord[1], coord[2] + direction[1])

        if shape.has_cube_at(neighbor[0], neighbor[1], neighbor[2]) and \
                can_be_merged(data, shape.cubes[neighbor[0]][neighbor[1]][neighbor[2]]):
            neighbor_set.append(neighbor)

    return neighbor_set


def piece_greater_than(cube1: tuple, cube2: tuple, shape: model):
    return shape.piece_size[shape.get_cube_at(cube1)] > shape.piece_size[shape.get_cube_at(cube2)]


def find_largest_neighbor_in_set(neighbor_set: [], shape: model):
    smallest_piece = deepcopy(neighbor_set[0])

    for it in range(1, len(neighbor_set)):
        if piece_greater_than(smallest_piece, neighbor_set[it], shape):
            smallest_piece = deepcopy(neighbor_set[it])

    return smallest_piece


def merge_bricks(cube1: tuple, cube2: tuple, shape: model):
    if piece_greater_than(cube1, cube2, shape):
        cube1.id = cube2.id
    else:
        cube2.id = cube1.id


def merge_cubes(shape: model):
    rand_cube = pick_random_cube(shape)
    neighbors = get_neighbor_set_for_cube(rand_cube, shape)
    largest_neighbor = find_largest_neighbor_in_set(neighbors, shape)
    merge_bricks(rand_cube[1], largest_neighbor, shape) 
