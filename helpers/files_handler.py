import re

def read_sudoku_file(file_name):

	dim = []
	sudokus = []
	fd = open(file_name, 'r')

	for line in fd:

		aux = re.split("\\s+", line)
		dim.append(aux[0])
		sudokus.append(aux[1])

	fd.close()
	return [dim, sudokus]