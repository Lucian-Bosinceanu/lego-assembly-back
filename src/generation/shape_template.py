class ShapeTemplate:
    def __init__(self, template):
        self.template = template

    def respects_template(self, cube_list, ids, matrix):
        if len(self.template) != len(cube_list):
            return False

        for start_cube in cube_list:
            if self.is_shape(start_cube, matrix, ids):
                return True

        return False

    def is_shape(self, start_cube, matrix, ids):
        for template in self.template:
            new_lin = template[0] + start_cube[0]
            new_col = template[1] + start_cube[1]

            if new_lin not in matrix:
                return False

            if new_col not in matrix[new_lin]:
                return False

            if matrix[new_lin][new_col] not in ids:
                return False

        return True
