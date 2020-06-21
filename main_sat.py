from helpers.sat import create_sat_instances
from helpers.files_handler import read_sudoku_file
from helpers.sudoku import create_soduku_array_instances, get_sudoku_from_sat, write_sudoku_sol, write_sat_format
from classes.translator_txt_cnf import Translator
import sys


def test_sat():
	sat_instances = create_sat_instances(sys.argv[1])
	for sat_instance in sat_instances:
		sat_instance.write_solution()

def test_sodoku_sat():
	solutions = []
	sudokus = create_soduku_array_instances(sys.argv[1])
	counter = 0
	for sodoku in sudokus:
		trans = Translator(sodoku.size, sodoku)
		trans.translate(sys.argv[1], counter)
		write_sat_format(trans.preps, pow(trans.dim, 6), sys.argv[1], counter)
		sol_sat_filename = 'sol_sat_' + str(counter) + '_' + sys.argv[1].split('/')[-1]
		solution = get_sudoku_from_sat(sol_sat_filename, trans)
		solutions.append(solution)
		counter = counter + 1
	sol_filename = 'sol_' +  sys.argv[1].split('/')[-1]
	write_sudoku_sol(solution, sol_filename)
		


if __name__ == '__main__':
	test_sodoku_sat()
