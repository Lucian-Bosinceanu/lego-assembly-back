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
    
    def addFromTo(self, matrix, destMatrix, i, j):
        p_id = matrix[i][j]
        # -1 gol
        can_add = True
        for i in range(len(matrix)):
            line = matrix[i]
            for j in range(len(line)):
                if line[j] == p_id and destMatrix[i][j] != -1: can_add = False
        
        if can_add == True:
            for i in range(len(matrix)):
                line = matrix[i]
                for j in range(len(line)):
                    if line[j] == p_id:
                        destMatrix[i][j] = p_id
        return can_add
    
    def init_matrix(self):
        chrom = self.population[0].get_solution()
        new_chrom = {}
        
        for i in range(len(chrom)):
            new_line = {}
            line = chrom[i]
            for j in range(len(line)):
                new_line[j] = -1
            new_chrom[i] = new_line

        return new_chrom
    
    def by_fitness(self, chromosome):
        return chromosome.fitness()
    
    def select_population_for_next_generation(self, MAX_POPULATION):
        self.population.sort(key=self.by_fitness)
        self.population = self.population[0:MAX_POPULATION]
    
    def cross_chromosomes(self, chrom1, chrom2):
        matrix1 = chrom1.get_solution()
        matrix2 = chrom2.get_solution()

        no_moves = 0
        new_matrix = self.init_matrix()
        while True:
            mat = random.random()
            x = random.randrange(0, len(matrix1))
            y = random.randrange(0, len(matrix1[0]))

            if mat < 0.5: copy_from = matrix1
            else: copy_from = matrix2
            
            if self.addFromTo(copy_from, new_matrix, x, y) == True:
                no_moves = 0
            else: no_moves += 1
            
            if no_moves >= 10: break
        
        max_id = 0
        for i in range(len(new_matrix)):
            line = new_matrix[i]
            for j in range(len(line)):
                if line[j] > max_id: max_id = line[j]

        for i in range(len(new_matrix)):
            line = new_matrix[i]
            for j in range(len(line)):
                if line[j] == -1:
                    max_id += 1
                    line[j] = max_id

        return Chromosome(LevelMatrix(new_matrix, self.known_shapes)) 


    def crossover_population(self):
        # 2 cate 2, avem random o sansa de a face cross intre cei 2 curenti si facem sau nu
        # 1/2 3/4 5/6
        for i in range(1, len(self.population), 2):
            current = self.population[i]
            prev = self.population[i - 1]
            prob = random.random()
            if (prob < self.pCross):
                newChrom = self.cross_chromosomes(prev, current)
                self.population.append(newChrom)
