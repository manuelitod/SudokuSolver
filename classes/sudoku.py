# Archivo para la clase sudoku
import numpy as np

class sudoku:
    def __init__(self, sudoku_board, size):
        self.size = int(size)
        self.size_pow = pow(self.size, 2)
        self.board = sudoku_board
        self.solution_board = np.array(sudoku_board)
        self.solved = False

    # Checkear si es posible colocar un numero
    # en el sudoku
    def possible_step(self, y, x, n):
        for i in range(0, self.size_pow):
            if self.solution_board[y][i] == n:
                return False
        for i in range(0, self.size_pow):
            if self.solution_board[i][x] == n:
                return False
        x0 = (x//self.size)*self.size
        y0 = (y//self.size)*self.size
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.solution_board[y0+i][x0+j] == n:
                    return False
        return True
    

    # Metodo para checkear si una solucion es
    # valida
    def check_solution(self):
        for i in range(self.size_pow):
            is_row_not_valid = (len(set(self.solution_board[i,:])) != self.size_pow)
            is_column_not_valid = (len(set(self.solution_board[:,i])) != self.size_pow)
            y, x = (i // self.size) * self.size, (i % self.size) * self.size
            is_section_not_valid = (len(set(self.solution_board[y:y+self.size, x:x+self.size].ravel())) != self.size_pow)
            if (is_row_not_valid or is_column_not_valid or is_section_not_valid):
                return False
        return True


    # Resolver sudoku de manera recursiva
    # Retorno al encontrar una solucion
    def solve(self):
        for y in range(self.size_pow):
            for x in range(self.size_pow):
                if self.solution_board[y][x] == 0:
                    for n in range(1, 10):
                        if self.possible_step(y, x, n):
                            self.solution_board[y][x] = n
                            self.solve()
                            if self.solved:
                                return
                            self.solution_board[y][x] = 0
                    return
        self.solved = True
        return

    # Print sudoku de manera legible
    def print(self, filename=None):
        print(np.matrix(self.board), file=filename)
