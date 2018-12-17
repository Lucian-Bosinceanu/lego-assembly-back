#2 Repeat for T iterations
    # evaluate population
    # crossover population
    # mutate population
    # select individuals for next iteration

from src.generation.chromosome import *
from src.generation.level_matrix import *
from src.generation.shape_template import *
from src.generation.population import *


def merge_test(shapes):
    levels = shapes.get_levels()

    known_shapes = [
        ShapeTemplate([(0, 0), (1, 0)]),
        ShapeTemplate([(0, 0), (0, 1)]),
        ShapeTemplate([(0, 1), (0, 0)]),
        ShapeTemplate([(1, 0), (0, 0)]),
    ]

    POPULATION_SIZE = 7
    GENERATION_COUNT = 10

    for level in levels:
        matrix = shapes.get_level_matrix(level)
        level_matrix = LevelMatrix(matrix, known_shapes)
        pop = Population(POPULATION_SIZE, level_matrix)

        for generation in range(0, GENERATION_COUNT):
            print("\n\n", "GENERATION: ", generation)
            pop.print_population()
            # TO DO:
            # new chromosomes creation
            # chromosomes mutation
            # evaluate population
            # select for next generation (iteration)

        best = pop.best_solution().get_solution()
        for i in best:
            for j in best:
                shapes.cubes[i][level][j].id = best[i][j]
                print(shapes.cubes[i][level][j].id)
