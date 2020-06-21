# Clase encargada de leer el fichero que contiene la información del sudoku,
# traducirlo a cnf y producir el fichero de entrada para SAT
from classes.sat import Sat
import time

class Literal:
	def __init__(self, y,x,value, literal):
		self.y = y
		self.x = x
		self.sudoku_value = value
		self.literal_value = literal

class Translator:

	def __init__(self, dim, sudokus):
		self.sudoku = sudokus
		self.dim = int(dim)
		self.dim_pow = pow(self.dim,2)
		self.literals = []
		self.literals_values = []
		self.preps = []
		self.total_exec_time = 0
	
	# Funcion para generar los literales
	# y las clausulas del sudoku
	def translate(self, filename, counter):
		self.generate_literals()
		self.build_preps()
		sat_instance = Sat(len(self.literals), len(self.preps), filename, counter)
		sat_instance.set_clauses(self.preps)
		start_time = time.time()
		sat_instance.write_solution()
		self.total_exec_time = round((time.time() - start_time)*1000,2)

	# Funcion para generar los literales
	# utilizando la biyeccion a [1, N ** 6]	
	def generate_literals(self):
		literals = []
		for y in range(self.dim_pow):
			for x in range(self.dim_pow):
				for d in range(1,self.dim_pow+1):
					y_literal = int(y)*pow(self.dim, 4)
					x_literal = int(x)*self.dim_pow
					literal = y_literal+x_literal+d
					literals.append(Literal(y_literal, x_literal, d, literal))
		self.literals = literals
		return
	
	# Funcion que genera las clausulas
	# de las casillas activadas del sudoku
	def gen_sudoku_cells_preps(self):
		clauses = []
		for y in range(self.dim_pow):
			for x in range(self.dim_pow):
				if self.sudoku.board[y][x] != 0:
					y_literal = int(y)*pow(self.dim, 4)
					x_literal = int(x)*self.dim_pow
					literal = y_literal+x_literal+self.sudoku.board[y][x]
					clauses.append([literal])
		self.preps = self.preps + clauses
		return clauses

	# Funcion para generar todas las clausulas
	# del sudoku
	def build_preps(self):
		self.gen_completeness_preps()
		completitud = len(self.preps)
		self.gen_uniqueness_preps()
		unicidad = len(self.preps) - completitud
		self.gen_validity_preps()
		validez = len(self.preps) - completitud - unicidad
		self.gen_sudoku_cells_preps()
		return

	# Funcion para generar las clausulas de completitud
	def gen_completeness_preps(self):
		self.literals_values = list(map(lambda literal: literal.literal_value, self.literals))
		literal_preps = [self.literals_values[i * self.dim_pow:(i + 1) * self.dim_pow] \
					for i in range((len(self.literals) + self.dim_pow - 1) // self.dim_pow )]
		self.preps = literal_preps
		return

	# Dado una lista de clausulas de completitud
	# se generan las clausulas de unicidad
	# self.preps debe contener las clausulas de completitud
	def gen_uniqueness_preps(self):
		unique_preps = []
		for prep in self.preps:
			unique_preps = unique_preps + self.gen_not_prep(prep)
		self.preps = self.preps + unique_preps
		return

	# Dado un conjunto de literales
	# se devuelve clasulas de unicidad
	# El flag only values construye la de validez
	def gen_not_prep(self, literals, only_values=False):
		no_preps_literals = []
		for index, literal in enumerate(literals):
			for next_index in range(index+1, len(literals)):
				if only_values:
					if literal.sudoku_value == literals[next_index].sudoku_value:
						no_preps_literals.append([-literal.literal_value, -(literals[next_index].literal_value)])	
					continue
				else:
					no_preps_literals.append([-literal, -(literals[next_index])])
		return no_preps_literals

	# Dada la coordenada inicial de una subseccion 
	# se devuelve un arreglo de coordenadas de esa coordenada
	def get_sudoku_section(self, coordinates):
		x = coordinates[0]
		y = coordinates[1]
		section_coordinates = []
		for i in range(0, self.dim):
			for j in range(0, self.dim):
				section_coordinates.append([x + i, y + j])
		return section_coordinates

	# Funcion para obtener los literales
	# de una fila, columna o seccion
	def get_sudoku_literals(self, index, index_type):
		literals = []
		if index_type == 'section':
			section_indexes = self.get_sudoku_section(index)
			for section_index in section_indexes:
				for d in range(1,self.dim_pow+1):
					y_literal = int(section_index[0])*pow(self.dim, 4)
					x_literal = int(section_index[1])*self.dim_pow
					literal = y_literal+x_literal+d
					literals.append(Literal(y_literal, x_literal, d, literal))
		else:
			for aux_index in range(self.dim_pow):
				for d in range(1,self.dim_pow+1):
					if index_type == 'row':
						y_literal = int(index)*pow(self.dim, 4)
						x_literal = int(aux_index)*self.dim_pow
						literal = y_literal+x_literal+d
						literals.append(Literal(y_literal, x_literal, d, literal))
					elif index_type == 'col': 
						y_literal = int(aux_index)*pow(self.dim, 4)
						x_literal = int(index)*self.dim_pow
						literal = y_literal+x_literal+d
						literals.append(Literal(y_literal, x_literal, d, literal))
		return literals

	def gen_validity_preps(self):
		for y in range(self.dim_pow):
			row_literals = self.get_sudoku_literals(y, 'row')
			row_preps = self.gen_not_prep(row_literals, True)
			self.preps = self.preps + row_preps
		for x in range(self.dim_pow):
			col_literals = self.get_sudoku_literals(x, 'col')
			col_preps = self.gen_not_prep(col_literals, True)
			self.preps = self.preps + col_preps
		start_section_index = self.get_start_index()
		for start_index in start_section_index:
			section_literals = self.get_sudoku_literals(start_index, 'section')
			section_preps = self.gen_not_prep(section_literals, True)
			self.preps = self.preps + section_preps
		return
	
	def get_start_index(self):
		index = []
		for i in range(0, self.dim):
			for j in range(0, self.dim):
				index.append((i*self.dim, j*self.dim))
		return index
