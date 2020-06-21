from classes.sudoku import sudoku
from helpers.sudoku import create_sudoku_instance, create_sudoku_array_instances
import sys
import traceback


# Main de prueba para una instancia de sudoku
if __name__ == '__main__':
	try:
		sudoku_file = open(sys.argv[1], 'r')
		sudoku_instances = create_sudoku_array_instances(sudoku_file)
		print('Entrada del sudoku')
		sudoku_instances[0].print()
		print('-------------------')
		print('Salida del sudoku')
		sudoku_instances[0].print_solution()
		sudoku_file.close()
	except:
		traceback.print_exc()
		print("Error al leer archivo de sudoku")
