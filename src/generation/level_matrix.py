import random
from datetime import datetime
import src.generation.shape_template


class LevelMatrix:
    def __init__(self, matrix, known_shapes):
        self.matrix = matrix.copy()
        self.directions = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
        self.known_shapes = known_shapes

    def print_matrix(self):
        print(self.matrix)

    def get_matrix(self):
        return self.matrix

    def get_shapes(self):
        shapes = dict()
        for i in self.matrix:
            for j in self.matrix[i]:
                if self.matrix[i][j] not in shapes:
                    shapes[self.matrix[i][j]] = 1
                else:
                    shapes[self.matrix[i][j]] += 1

        return shapes

    def pick_random_cube(self):
        random.seed(datetime.now())

        pos_x = random.randrange(0, len(self.matrix))
        pos_y = random.randrange(0, len(self.matrix[0]))
        return pos_x, pos_y

    def at(self, x, y):
        return self.matrix[x][y]

    def in_matrix(self, lin, col):
        return lin in self.matrix and col in self.matrix[lin]

    def can_be_merged(self, cube_lin, cube_col):
        for i in range(0, len(self.directions)):
            nx, ny = self.get_neighbor_in_direction(self.directions[i], cube_lin, cube_col)
            if self.can_merge(cube_lin, cube_col, nx, ny):
                return True

        return False

    def get_neighbor_in_direction(self, dir_pos, cube_lin, cube_col):
        neighbor_lin = dir_pos[0] + cube_lin
        neighbor_col = dir_pos[1] + cube_col

        if self.in_matrix(neighbor_lin, neighbor_col):
            return neighbor_lin, neighbor_col

        return cube_lin, cube_col

    def is_merge_possible(self):
        for i in self.matrix:
            for j in self.matrix:
                if self.can_be_merged(i, j):
                    return True

        return False

    def chose_neighbor(self, cube_lin, cube_col):
        directions = [0] * 8
        while 0 in directions:
            index, n_lin, n_col = self.pick_random_neighbor_to_merge(cube_lin, cube_col)

            if self.can_merge(cube_lin, cube_col, n_lin, n_col):
                return n_lin, n_col

            directions[index] = 1

        return cube_lin, cube_col

    def pick_random_neighbor_to_merge(self, cube_lin, cube_col):
        index = random.randrange(0, len(self.directions))
        neighbor_x, neighbor_y = \
            self.get_neighbor_in_direction(self.directions[index], cube_lin, cube_col)
        return index, neighbor_x, neighbor_y

    def merge_cube_with_neighbor(self, cube_lin, cube_col):
        neighbor_lin, neighbor_col = self.chose_neighbor(cube_lin, cube_col)

        if self.in_matrix(neighbor_lin, neighbor_col):
            self.merge_all_with_same_id(cube_lin, cube_col, neighbor_lin, neighbor_col)

    def merge_all_with_same_id(self, cube_lin, cube_col, n_lin, n_col):
        list1 = self.get_pieces_with_same_id(cube_lin, cube_col)

        for element in list1:
            self.matrix[element[0]][element[1]] = self.matrix[n_lin][n_col]

    def get_pieces_with_same_id(self, cube_lin, cube_col):
        cube_id = self.matrix[cube_lin][cube_col]
        rez = [(cube_lin, cube_col)]

        for i in self.matrix:
            for j in self.matrix[i]:
                if self.matrix[i][j] == cube_id:
                    rez.append((i, j))

        return rez

    def can_merge(self, cube_lin, cube_col, n_lin, n_col):
        if not self.in_matrix(cube_lin, cube_col) or not self.in_matrix(n_lin, n_col):
            return False

        cube_id = self.matrix[cube_lin][cube_col]
        n_id = self.matrix[n_lin][n_col]

        if cube_id == n_id:
            return False

        cube_list = self.get_pieces_with_same_id(cube_lin, cube_col)
        cube_list += self.get_pieces_with_same_id(n_lin, n_col)

        for shape in self.known_shapes:
            if shape.respects_template(cube_list, [cube_id, n_id], self.matrix):
                return True

        return False
