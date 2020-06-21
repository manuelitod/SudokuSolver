# Modulo de funciones de utilidad para la clase sudoku

from classes.sudoku import sudoku
from classes.translator_txt_cnf import Literal

# Dada una representacion en string del sudoku
# devuelve una instancia de sudoku
def create_sudoku_instance(sudoku_string):
	size, board = sudoku_string.split(' ')
	board = board.split('\n')[0]
	size_pow = pow(int(size), 2)
	board = [list(map(int,board[i:i+size_pow])) for i in range(0, len(board), size_pow)]
	return sudoku(board, size)

# Dado un archivo sudoku se crea una lista
# de instancias de sudoku
def create_sudoku_array_instances(sudoku_filename):
	sudoku_file = open(sudoku_filename, 'r')
	sudoku_array_instances = []
	for sudoku_line in sudoku_file:
		# To-do Checkear si la linea es valida
		sudoku_array_instances.append(create_sudoku_instance(sudoku_line))
	return sudoku_array_instances

# Método que lee un fichero que contiene la salida de un resolvedor de SAT y
# lo traduce a un string que contenga la solución del sudoku.

def get_sudoku_from_sat(sol_filename, translator):

	sudoku = ''
	literals = translator.literals
	fd = open(sol_filename, 'r')
	counter = 0

	for line in fd:

		if counter == 0:

			counter = 1
			satisfy = line.split(' ')[2]

			if int(satisfy) != 1: return line
			sudoku = str(translator.dim) + ' '
			continue

		literal = line.split(' ')[1]

		if int(literal) > 0:

			sudoku = sudoku + str(literals[int(literal)-1].sudoku_value)

	fd.close()
	return sudoku

# Método que escribe el fichero que contiene la solución del sudoku.

def write_sudoku_sol(solutions, filename):

	fd = open(filename, 'a')

	for i in solutions:
		fd.write(i + '\n')

	fd.close()

def write_sat_format(preps, lits, filename, counter):

	file = 'sat_' + str(counter) + '_' + filename.split('/')[-1]
	fd = open(file, 'a')
	prologue = 'p cnf ' + str(lits) + ' ' + str(len(preps)) + '\n'

	fd.write(prologue)

	for i in range(0, len(preps)):

		line = ''

		for j in preps[i]:
			line = line + str(j) + ' '

		line = line + '0\n'
		fd.write(line)

	fd.close()