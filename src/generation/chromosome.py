from src.generation.level_matrix import *


class Chromosome:
    def __init__(self, matrix: LevelMatrix):
        self.matrix = matrix

    def print_chromosome(self):
        print("Fitness: ", self.fitness(), "Matrix: ", self.matrix.print_matrix())

    def fitness(self):
        shapes = self.matrix.get_shapes()
        fitness_value = 0
        for key, value in shapes.items():
            if value == 1:
                fitness_value += 1

        return fitness_value

    def get_solution(self):
        return self.matrix.get_matrix()

    def build(self):
        while self.matrix.is_merge_possible():
            cube_lin, cube_col = self.matrix.pick_random_cube()
            self.matrix.merge_cube_with_neighbor(cube_lin, cube_col)
