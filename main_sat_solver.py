from helpers.sat import create_sat_instances
from helpers.files_handler import read_sudoku_file
from helpers.sudoku import (create_sudoku_array_instances, 
							get_sudoku_from_sat, write_sudoku_sol,
							write_sat_format)
from classes.translator_txt_cnf import Translator
import sys

def run_sat_solver():
	solutions = []
	sudokus = create_sudoku_array_instances(sys.argv[1])
	counter = 0

	for sudoku in sudokus:
		trans = Translator(sudoku.size, sudoku)
		trans.translate(sys.argv[1], counter)
		write_sat_format(trans.preps, pow(trans.dim, 6), sys.argv[1], counter)
		sol_sat_filename = '../scripts/SatOutput/sol_sat_' + str(counter) + '_' + sys.argv[1].split('/')[-1]
		solution = get_sudoku_from_sat(sol_sat_filename, trans)
		solutions.append(solution)
		counter = counter + 1
	sol_filename = 'sol_' +  sys.argv[1].split('/')[-1]
	write_sudoku_sol(sudokus, solutions, sol_filename)
		
if __name__ == '__main__':
	run_sat_solver()
