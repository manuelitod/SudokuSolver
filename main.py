from classes.sudoku import Soduku
from helpers.sudoku import create_soduku_instance, create_soduku_array_instances
import sys
import traceback


# Main de prueba para una instancia de soduku
if __name__ == '__main__':
	try:
		soduku_file = open(sys.argv[1], 'r')
		soduku_instances = create_soduku_array_instances(soduku_file)
		print('Entrada del soduku')
		soduku_instances[0].print()
		print('-------------------')
		print('Salida del soduku')
		soduku_instances[0].print_solution()
		soduku_file.close()
	except:
		traceback.print_exc()
		print("Error al leer archivo de soduku")
