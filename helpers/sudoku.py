# Modulo de funciones de utilidad para la clase soduku

from classes.sudoku import Soduku

# Dada una representacion en string del soduku
# devuelve una instancia de soduku
def create_soduku_instance(soduku_string):
	size, board = soduku_string.split(' ')
	board = board.split('\n')[0]
	size_pow = pow(int(size), 2)
	board = [list(map(int,board[i:i+size_pow])) for i in range(0, len(board), size_pow)]
	return Soduku(board, size)

# Dado un archivo soduku se crea una lista
# de instancias de sodoku
def create_soduku_array_instances(soduku_filename):
	soduku_file = open(soduku_filename, 'r')
	soduku_array_instances = []
	for soduku_line in soduku_file:
		# To-do Checkear si la linea es valida
		soduku_array_instances.append(create_soduku_instance(soduku_line))
	return soduku_array_instances
