from src.generation.shape_template import *
from src.generation.population import *


def merge_test(shapes):
    levels = shapes.get_levels()

    known_shapes = [
        ShapeTemplate([(0, 0), (1, 0)]),
        ShapeTemplate([(0, 0), (0, 1)]),
        ShapeTemplate([(0, 1), (0, 0)]),
        ShapeTemplate([(1, 0), (0, 0)]),
        ShapeTemplate([(0, 0), (1, 0), (2, 0)]),
        ShapeTemplate([(1, 0), (0, 0), (2, 0)]),
        ShapeTemplate([(0, 0), (2, 0), (1, 0)]),
        ShapeTemplate([(1, 0), (2, 0), (0, 0)]),
        ShapeTemplate([(2, 0), (0, 0), (1, 0)]),
        ShapeTemplate([(0, 2), (0, 1), (0, 0)]),
        ShapeTemplate([(0, 0), (0, 1), (0, 2)]),
        ShapeTemplate([(0, 1), (0, 0), (0, 2)]),
        ShapeTemplate([(0, 0), (0, 2), (0, 1)]),
        ShapeTemplate([(0, 1), (0, 2), (0, 0)]),
        ShapeTemplate([(0, 2), (0, 0), (0, 1)]),
        ShapeTemplate([(0, 2), (0, 1), (0, 0)]),
        ShapeTemplate([(0, 0), (1, 0), (0, 1), (1, 1)]),
        ShapeTemplate([(0, 0), (1, 0), (1, 1), (0, 1)]),
        ShapeTemplate([(1, 1), (1, 0), (0, 0), (0, 1)]),
        ShapeTemplate([(0, 1), (1, 0), (0, 0), (1, 1)]),
        ShapeTemplate([(1, 1), (1, 0), (0, 1), (0, 0)]),
        ShapeTemplate([(0, 1), (1, 0), (1, 1), (0, 0)]),
        ShapeTemplate([(0, 0), (0, 1), (1, 0), (1, 1)]),
        ShapeTemplate([(0, 0), (0, 1), (1, 1), (1, 0)]),
        ShapeTemplate([(1, 1), (0, 1), (0, 0), (1, 0)]),
        ShapeTemplate([(1, 0), (0, 1), (0, 0), (1, 1)]),
        ShapeTemplate([(1, 1), (0, 1), (1, 0), (0, 0)]),
        ShapeTemplate([(1, 0), (0, 1), (1, 1), (0, 0)]),
        ShapeTemplate([(0, 0), (1, 1), (0, 1), (1, 0)]),
        ShapeTemplate([(0, 0), (1, 1), (1, 0), (0, 1)]),
        ShapeTemplate([(1, 0), (1, 1), (0, 0), (0, 1)]),
        ShapeTemplate([(0, 1), (1, 1), (0, 0), (1, 0)]),
        ShapeTemplate([(1, 0), (1, 1), (0, 1), (0, 0)]),
        ShapeTemplate([(0, 1), (1, 1), (1, 0), (0, 0)]),
        ShapeTemplate([(1, 1), (0, 0), (0, 1), (1, 0)]),
        ShapeTemplate([(1, 1), (0, 0), (1, 0), (0, 1)]),
        ShapeTemplate([(1, 0), (0, 0), (1, 1), (0, 1)]),
        ShapeTemplate([(0, 1), (0, 0), (1, 1), (1, 0)]),
        ShapeTemplate([(1, 0), (0, 0), (0, 1), (1, 1)]),
        ShapeTemplate([(0, 1), (0, 0), (1, 0), (1, 1)])
    ]

    POPULATION_SIZE = 10
    GENERATION_COUNT = 10

    for level in levels:
        matrix = shapes.get_level_matrix(level)
        pop = Population(POPULATION_SIZE, matrix, known_shapes)
        if len(matrix) == 1:
            continue

        for generation in range(0, GENERATION_COUNT):
            print("\n\n", "GENERATION: ", generation)

            pop.crossover_population()
            pop.select_population_for_next_generation(POPULATION_SIZE)
            pop.print_population()
            # TO DO:
            # new chromosomes creation
            # chromosomes mutation
            # evaluate population
            # select for next generation (iteration)

        best = pop.best_solution().get_solution()
        for i in best:
            for j in best[i]:
                shapes.cubes[j][level][i].id = best[i][j]
