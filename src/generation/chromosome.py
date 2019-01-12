from src.generation.level_matrix import *


class Chromosome:
    def __init__(self, matrix: LevelMatrix):
        self.matrix = matrix

    def print_chromosome(self):
        print("Fitness:", self.fitness(), "Matrix:")
        self.matrix.print_matrix()

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
            for lin in self.matrix.matrix:
                for col in self.matrix.matrix[lin]:
                    self.matrix.try_merge(lin, col)
