from helpers.sat import create_sat_instances
from helpers.files_handler import read_sudoku_file
from helpers.sudoku import (create_sudoku_array_instances, 
							get_sudoku_from_sat, write_sudoku_sol)
from classes.translator_txt_cnf import Translator
import sys
import subprocess
import os
import time

def run_zchaff_solver():
	sudoku_instances_file = sys.argv[1]
	instances_time_limit = sys.argv[2]
	sudokus = create_sudoku_array_instances(sudoku_instances_file)
	sol_sudoku_filename = 'sol_sat_zchaff_' +  sudoku_instances_file.split('/')[-1]
	counter = 0

	for sudoku in sudokus:
		print("Solucionando con zchaff sudoku número ", counter + 1)
		trans = Translator(sudoku.size, sudoku)
		file = trans.write_sat_format(sudoku_instances_file, counter)
		solution_file = './SatOutput/sol_sat_zchaff_' + str(counter) + '_' + sudoku_instances_file.split('/')[-1]
		command =  './zchaff64/zchaff ' + file + ' ' +  instances_time_limit + ' >> ' + solution_file
		tiempo_inicio = time.time()
		os.system(command)
		trans.total_exec_time = round((time.time() - tiempo_inicio)*1000,2)
		solution = get_sudoku_from_sat(solution_file, trans, True)
		write_sudoku_sol(sudoku, solution, sol_sudoku_filename, counter, True)
		counter += 1

if __name__ == '__main__':
	run_zchaff_solver()
