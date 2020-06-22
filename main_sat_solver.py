from helpers.sat import create_sat_instances
from helpers.files_handler import read_sudoku_file
from helpers.sudoku import (create_sudoku_array_instances, 
							get_sudoku_from_sat, write_sudoku_sol)
from classes.translator_txt_cnf import Translator
import sys

def run_sat_solver():
	sudoku_instances_file = sys.argv[1]
	instances_time_limit = float(sys.argv[2])
	sudokus = create_sudoku_array_instances(sudoku_instances_file)
	sol_sudoku_filename = 'sol_sat_' +  sudoku_instances_file.split('/')[-1]
	counter = 0

	for sudoku in sudokus:
		print("Solucionando con sat propio sudoku número ", counter + 1)
		trans = Translator(sudoku.size, sudoku)
		trans.translate(sudoku_instances_file, counter, instances_time_limit)
		trans.write_sat_format(sudoku_instances_file, counter)
		sol_sat_filename = '../scripts/SatOutput/sol_sat_' + str(counter) + '_' + sudoku_instances_file.split('/')[-1]
		solution = get_sudoku_from_sat(sol_sat_filename, trans)
		write_sudoku_sol(sudoku, solution, sol_sudoku_filename, counter)
		counter = counter + 1
		
if __name__ == '__main__':
	run_sat_solver()
