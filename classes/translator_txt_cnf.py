# Clase encargada de leer el fichero que contiene la información del sudoku,
# traducirlo a cnf y producir el fichero de entrada para SAT

class Translator:

	def __init__(self, dim, sudokus):
		self.sudokus_list = sudokus
		self.dim = int(dim[0])

	def translate(self):

		literals = self.translate_sudoku_to_lit()
		preps = self.build_preps()

	def translate_sudoku_to_lit(self):

		cnf_list = []
		for i in self.sudokus_list:

			cnf = []
			for j in i:

				d = []
				for k in range(1, 10):
					if(str(k) == j):
						d.append(1)
					else:
						d.append(0)

				cnf = cnf + d
			cnf_list.append(cnf)

		return cnf_list

	def build_preps(self):

		preps = []

		preps = preps + self.gen_completeness_preps()
		preps = preps + self.gen_uniqueness_preps()
		preps = preps + self.gen_validity_preps()

		return preps

	def gen_completeness_preps(self):

		preps = []
		counter = 1

		for i in range(0,self.dim*self.dim):
			for j in range(0,self.dim*self.dim):
				prep = []
				for k in range(1, (self.dim*self.dim + 1)):
					prep.append(counter)
					counter += 1
				preps = preps + prep

		return preps

	def gen_uniqueness_preps(self):

		preps = []

		for i in range(0,self.dim*self.dim):
			for j in range(0,self.dim*self.dim):
				prep = []
				for k in range(1, (self.dim*self.dim + 1)):
					for w in range(1,(self.dim*self.dim + 1)):
						if k == w:
							break
						else:
							prep.append([-1*(i*self.dim*self.dim*self.dim*self.dim + self.dim*self.dim*j + k), 
								-1*(i*self.dim*self.dim*self.dim*self.dim + self.dim*self.dim*j + w)])
				preps = preps + prep
		
		return preps

	def row_preps(self):

		preps = []

		for i in range(0,self.dim*self.dim):
			for k in range(1, (self.dim*self.dim + 1)):

				candidates = []
				prep = []

				for j in range(0,self.dim*self.dim):

					candidates.append(i*self.dim*self.dim*self.dim*self.dim + self.dim*self.dim*j + k)

				for x in candidates:
					for y in candidates:

						if x == y:
							break
						else:
							prep.append([-1*x, -1*y])
				preps = preps + prep

		return preps

	def column_preps(self):

		preps = []

		return preps

	def section_preps(self):

		preps = []

		return preps

	def gen_validity_preps(self):

		preps = []

		preps = preps + self.row_preps()

		preps = preps + self.column_preps()

		preps = preps + self.section_preps()

		return preps
