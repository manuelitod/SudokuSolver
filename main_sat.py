from helpers.sat import create_sat_instances
from helpers.files_handler import read_sudoku_file
from helpers.sudoku import create_soduku_array_instances
from classes.translator_txt_cnf import Translator
import sys


def test_sat():
	sat_instances = create_sat_instances(sys.argv[1])
	for sat_instance in sat_instances:
		sat_instance.write_solution()

def test_sodoku_sat():
	sudokus = create_soduku_array_instances(sys.argv[1])
	for sodoku in sudokus:
		trans = Translator(sodoku.size, sodoku)
		trans.translate()

if __name__ == '__main__':
	test_sodoku_sat()
