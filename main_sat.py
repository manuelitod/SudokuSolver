from helpers.sat import create_sat_instances
from helpers.files_handler import read_sudoku_file
from classes.translator_txt_cnf import Translator
import sys

if __name__ == '__main__':
	dim, sudokus = read_sudoku_file(sys.argv[1])
	trans = Translator(dim, sudokus)
	trans.translate()
