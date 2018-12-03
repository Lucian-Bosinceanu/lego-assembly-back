import random
from datetime import datetime
import src.input_output.model as model
import src.input_output.cubedata as cube

DIRECTIONS = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))


def pick_random_coordinate(randrange):
    random.seed(datetime.now())

    x = random.randrange(0, randrange)
    y = random.randrange(0, randrange)
    z = random.randrange(0, randrange)

    return x, y, z


def pick_random_cube(shape: model) -> cube:
    coord = pick_random_coordinate(len(shape.cubes))

    while not shape.has_cube_at(coord[0], coord[1], coord[2]):
        coord = pick_random_coordinate(len(shape.cubes))

    return shape.cubes[coord[0]][coord[1]][coord[2]], (coord[0], coord[1], coord[2])


def can_be_merged(cube1: cube, cube2: cube) -> bool:
    return cube1.id != cube2.id and cube1.color == cube2.color


def get_neighbor_set_for_cube(cube_data: (cube, tuple), shape: model):
    neighbor_set = []
    
    data = cube_data[0]
    coord = cube_data[1]

    for direction in DIRECTIONS:
        neighbor = (coord[0] + direction[0], coord[1], coord[2] + direction[1])

        if shape.has_cube_at(neighbor[0], neighbor[1], neighbor[2]) and \
                can_be_merged(data, shape.get_cube_at([coord[0] + direction[0], coord[1], coord[2] + direction[1]])):
            neighbor_set.append(shape.get_cube_at([coord[0] + direction[0], coord[1], coord[2] + direction[1]]))

    return neighbor_set


def piece_greater_than(cube1: cube, cube2: cube, shape: model):
    return shape.piece_size[cube1.id] > shape.piece_size[cube2.id]


def find_largest_neighbor_in_set(neighbor_set: [], shape: model):
    smallest_piece = neighbor_set[0]

    for neighbor in neighbor_set:
        if piece_greater_than(smallest_piece, neighbor, shape):
            smallest_piece = neighbor

    return smallest_piece


def merge_bricks(cube1: cube, cube2: cube, shape: model):
    if piece_greater_than(cube1, cube2, shape):
        cube1.id = cube2.id
    else:
        cube2.id = cube1.id


def merge_cubes(shape: model):

    while True:
        cube_merged = False
        rand_cube = pick_random_cube(shape)
        neighbors = get_neighbor_set_for_cube(rand_cube, shape)
        while len(neighbors) > 0:
            largest_neighbor = find_largest_neighbor_in_set(neighbors, shape)
            merge_bricks(rand_cube[0], largest_neighbor, shape)
            neighbors.remove(largest_neighbor)
            cube_merged = True

        if not cube_merged:
            break

    return shape
