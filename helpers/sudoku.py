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
	sudoku_file.close()
	return sudoku_array_instances

# Método que lee un fichero que contiene la salida de un resolvedor de SAT y
# lo traduce a un string que contenga la solución del sudoku.

def get_sudoku_from_sat(sol_filename, translator):

	sudoku = ''
	literals = translator.literals
	fd = open(sol_filename, 'r')
	counter = 0

	for line in fd:
		if line == '\n': continue
		if counter == 0:

			counter = 1
			satisfy = line.split(' ')[2]

			if int(satisfy) == 0: return ('Instance Unsatisfiable', translator.total_exec_time, 0)
			if int(satisfy) == -1: return ('Instance Timeout', translator.total_exec_time, -1)
			sudoku = str(translator.dim) + ' '
			continue

		literal = line.split(' ')[1]

		if int(literal) > 0:

			sudoku = sudoku + str(literals[int(literal)-1].sudoku_value)

	fd.close()
	return (sudoku, translator.total_exec_time, 1)

# Método que escribe el fichero que contiene la solución del sudoku.

def write_sudoku_sol(sudokus, solutions, filename, is_zchaff=False):

	# Escribimos el sudoku
	fd = open(filename, 'a')
	fd_times = open('../scripts/SatOutputTimes/' + filename, 'a')
	if is_zchaff:
		fd_report = open('Reporte de ejecucion Sat Zchaff.txt', 'a')
		fd_report.write("Reporte de ejecución de implementación SAT zchaff \n")
	else:
		fd_report = open('Reporte de ejecucion Sat propio.txt', 'a')
		fd_report.write("Reporte de ejecución de implementación SAT propia \n")

	for index, solution in enumerate(solutions):
		fd.write(solution[0] + '\n')
		fd_times.write(str(solution[1]) + '\n')

		# Generamos el informe
		fd_report.write("Instancia número " + str(index) + '\n')
		fd_report.write('Entrada: \n')
		sudokus[index].print(fd_report)
		fd_report.write('Salida: \n')
		if solution[2] == 0 or solution[2] == -1:
			fd_report.write("No tiene solución o se agoto el tiempo para solucionarlo \n")
		else:
			create_sudoku_instance(solution[0]).print(fd_report)
		fd_report.write("Tiempo de ejecución: " + str(solution[1]) + 'ms \n')

	fd.close()
	fd_times.close()
	fd_report.close()

def write_sat_format(preps, lits, filename, counter):

	file = '../scripts/SatInput/sat_' + str(counter) + '_' + filename.split('/')[-1]
	file_input = './SatInput/sat_' + str(counter) + '_' + filename.split('/')[-1]
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
	return file_input
