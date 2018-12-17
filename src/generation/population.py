from src.generation.chromosome import Chromosome
from src.generation.level_matrix import LevelMatrix
import copy
import random

class Population:
    def __init__(self, size, matrix, known_shapes):
        self.level_matrix = matrix
        self.known_shapes = known_shapes
        self.population = self.init_population(size)

    def init_population(self, size):
        pop = []
        for i in range(0, size):
            matrix_copy = copy.deepcopy(self.level_matrix)
            pop.append(Chromosome(LevelMatrix(matrix_copy, self.known_shapes)))
            pop[i].build()

        return pop

    def print_population(self):
        for chromosome in self.population:
            chromosome.print_chromosome()

    def best_solution(self):
        best = 10000000
        best_index = -1
        for i in range(0, len(self.population)):
            if self.population[i].fitness() < best:
                best = self.population[i].fitness()
                best_index = i

        return self.population[best_index]

    def crossover_population(self):
        pass
