from helpers.sat import create_sat_instances
from helpers.files_handler import read_sudoku_file
from helpers.sudoku import (create_sudoku_array_instances, 
							get_sudoku_from_sat, write_sudoku_sol,
							write_sat_format)
from classes.translator_txt_cnf import Translator
import sys
import subprocess
import os
import time

def run_zchaff_solver():
	solutions = []
	sudokus = create_sudoku_array_instances(sys.argv[1])
	counter = 0

	for sudoku in sudokus:
		trans = Translator(sudoku.size, sudoku)
		file = write_sat_format(trans.preps, pow(trans.dim, 6), sys.argv[1], counter)
		solution_file = './SatOutput/sol_sat_zchaff_' + str(counter) + '_' + sys.argv[1].split('/')[-1]
		command =  './zchaff64/zchaff ' + file + ' >> ' + solution_file
		tiempo_inicio = time.time()
		# Codea lo de tomar tiempo de inicio, tiempo final y escribir en el la carpeta de output time. Ok
		os.system(command)
		trans.total_exec_time = round((time.time() - tiempo_inicio)*1000,2)
		solution = get_sudoku_from_sat(solution_file, trans)
		solutions.append(solution)
		counter += 1
	sol_filename = 'sol_zchaff_' +  sys.argv[1].split('/')[-1]
	write_sudoku_sol(sudokus, solutions, sol_filename, True)

if __name__ == '__main__':
	run_zchaff_solver()
