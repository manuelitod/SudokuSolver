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

def get_sudoku_from_sat(sol_filename, translator, is_zchaff=False):

	sudoku = ''
	literals = translator.literals
	fd = open(sol_filename, 'r')
	counter = 0

	for line in fd:
		# El zchaff es magico e imprime un \n en la linea 0
		if line == '\n': continue
		if counter == 0:

			counter = 1
			satisfy = line
			if not is_zchaff: 
				satisfy = satisfy.split(' ')[2]
				if int(satisfy) == 0: return ('Instance Unsatisfiable', translator.total_exec_time, 0)
				if int(satisfy) == -1: return ('Instance Timeout', translator.total_exec_time, -1)
			else:
				satisfy = satisfy.split('\n')[0]
				if satisfy == 'Instance Unsatisfiable':
					return ('Instance Unsatisfiable', translator.total_exec_time, 0)
				elif satisfy == 'Instance Timeout':
					return ('Instance Timeout', translator.total_exec_time, -1)

			sudoku = str(translator.dim) + ' '
			continue

		literal = line.split(' ')[1]

		if int(literal) > 0:

			sudoku = sudoku + str(literals[int(literal)-1].sudoku_value)

	fd.close()
	return (sudoku, translator.total_exec_time, 1)

# Método que escribe el fichero que contiene la solución del sudoku.

def write_sudoku_sol(sudoku, solution, filename, counter, is_zchaff=False):

	fd = open('../scripts/SatSols/' + filename, 'a')
	fd_times = open('../scripts/SatOutputTimes/' + filename, 'a')
	if is_zchaff:
		fd_report = open('../scripts/Reports/' + filename, 'a')
		if counter == 0: fd_report.write("Reporte de ejecución de implementación SAT zchaff \n")
	else:
		fd_report = open('../scripts/Reports/' + filename, 'a')
		if counter == 0: fd_report.write("Reporte de ejecución de implementación SAT propia \n")	
	fd.write(solution[0] + '\n')
	fd_times.write(str(solution[1]) + '\n')

	# Generamos el informe
	fd_report.write("Instancia número " + str(counter + 1) + '\n')
	fd_report.write('Entrada: \n')
	sudoku.print(fd_report)
	fd_report.write('Salida: \n')
	if solution[2] == -1:
		fd_report.write("Se agoto el tiempo para solucionarlo \n")
	elif solution[2] == 0:
		fd_report.write("No tiene solución \n")
	else:
		create_sudoku_instance(solution[0]).print(fd_report)
	fd_report.write("Tiempo de ejecución: " + str(solution[1]) + 'ms \n')

	fd.close()
	fd_times.close()
	fd_report.close()
