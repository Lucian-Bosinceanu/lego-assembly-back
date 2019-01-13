from src.generation.chromosome import Chromosome
from src.generation.level_matrix import LevelMatrix
import copy
import random

class Population:
    def __init__(self, size, matrix, known_shapes):
        self.pCross = 0.5
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
        min_fitness = self.population[0].fitness()
        for chromosome in self.population:
            fitness = chromosome.fitness()
            if fitness < min_fitness:
                min_fitness = fitness
        print('chromosomes: ', len(self.population))
        print('min fitness: ', min_fitness)

    def best_solution(self):
        best = 10000000
        best_index = -1
        for i in range(0, len(self.population)):
            if self.population[i].fitness() < best:
                best = self.population[i].fitness()
                best_index = i

        return self.population[best_index]
    
    @staticmethod
    def add_from_to(matrix, dest_matrix, i, j):
        p_id = matrix[i][j]
        # -1 gol
        can_add = True
        for i in matrix:
            for j in matrix[i]:
                if matrix[i][j] == p_id and dest_matrix[i][j] != -1:
                    can_add = False
        
        if can_add:
            for i in matrix:
                for j in matrix[i]:
                    if matrix[i][j] == p_id:
                        dest_matrix[i][j] = p_id
        return can_add
    
    def init_matrix(self):
        chromosome = self.population[0].get_solution()
        new_chromosome = {}
        
        for i in chromosome:
            new_line = {}
            for j in chromosome[i]:
                new_line[j] = -1
            new_chromosome[i] = new_line

        return new_chromosome
    
    @staticmethod
    def by_fitness(chromosome):
        return chromosome.fitness()
    
    def select_population_for_next_generation(self, max_population):
        self.population.sort(key=self.by_fitness)
        self.population = self.population[0:max_population]
    
    def cross_chromosomes(self, chromosome_1, chromosome_2):
        matrix1 = chromosome_1.get_solution()
        matrix2 = chromosome_2.get_solution()

        no_moves = 0
        new_matrix = self.init_matrix()
        while True:
            mat = random.random()

            x = random.choice(list(matrix1.keys()))
            y = random.randrange(0, len(matrix1[x]))

            if mat < 0.5:
                copy_from = matrix1
            else:
                copy_from = matrix2

            if x not in copy_from or y not in copy_from[x]:
                continue

            if self.add_from_to(copy_from, new_matrix, x, y):
                no_moves = 0
            else:
                no_moves += 1
            
            if no_moves >= 10:
                break
        
        max_id = 0
        for i in new_matrix:
            for j in new_matrix[i]:
                if new_matrix[i][j] > max_id:
                    max_id = new_matrix[i][j]

        for i in new_matrix:
            for j in new_matrix[i]:
                if new_matrix[i][j] == -1:
                    max_id += 1
                    new_matrix[i][j] = max_id

        return Chromosome(LevelMatrix(new_matrix, self.known_shapes)) 

    def crossover_population(self):
        # 2 cate 2, avem random o sansa de a face cross intre cei 2 curenti si facem sau nu
        # 1/2 3/4 5/6
        for i in range(1, len(self.population), 2):
            current = self.population[i]
            prev = self.population[i - 1]
            prob = random.random()
            if prob < self.pCross:
                new_chromosome = self.cross_chromosomes(prev, current)
                self.population.append(new_chromosome)
