
class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []

        for row in self._extract_rows(matrix_string):
            self.matrix.append(self._extract_columns(row))

    @staticmethod
    def _extract_columns(row):
        return [int(num) for num in row.split()]

    @staticmethod
    def _extract_rows(matrix_string):
        return matrix_string.splitlines()

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]

