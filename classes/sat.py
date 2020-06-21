# Clase SAT
import random
import time

class Sat:
	def __init__(self, number_vars, number_clauses, file_name, counter):
		self.number_vars = int(number_vars)
		self.number_clauses = int(number_clauses)
		self.clauses = []
		self.solution = []
		self.start_time = 0
		self.file_name = file_name
		self.counter = counter

	def set_clauses(self, clauses):
		self.clauses = clauses.copy()
	
	def set_assignment(self, assignment):
		self.assignment = assignment.copy()

	# Método que retorna las cláusulas que no poseen literales puros en el caso del método pure_literal
	# En el caso de unit_propagation retorna una lista con las cláusulas modificadas.
	# Dicha modificación consiste en eliminar de las cláusulas los literales negados de los literales unitarios.

	def reduce_preposition(self, preposition, var):
		modified = []
		for clause in preposition:
			if var in clause: continue
			if -var in clause:
				c = [x for x in clause if x != -var]
				if len(c) == 0: return -1
				modified.append(c)
			else:
				modified.append(clause)
		return modified
	
	# Método que retorna un diccionario cuyas claves son las variables utilizadas 
	# y su valor es el número de apariciones de dicha variable en las cláusulas.
	
	def literal_counter(self, preposition):
		counter = {}
		for clause in preposition:
			for literal in clause:
				if literal in list(counter.keys()):
					counter[literal] += 1
				else:
					counter[literal] = 1
		return counter


	# Método que retorna como primer parámetro un arreglo con las cláusulas que no
	# poseen ningún literal puro y como segundo parámetro los literales puros.

	def pure_literal(self, preposition):
		literal_counter = self.literal_counter(preposition)
		assigment = []
		pures = []

		for literal, times in literal_counter.items():
			if -literal not in literal_counter: pures.append(literal)
		for pure in pures:
			preposition = self.reduce_preposition(preposition, pure)
		assigment += pures
		return preposition, assigment

	# Método que retorna las cláusulas modificadas, habiendo eliminado los literales unitarios negados de ellas,
	# como primer parámetro y añade al arreglo "assignment" los literales unitarios.

	def unit_propagation(self, preposition):
		assignment = []
		unit_clauses = [c for c in preposition if len(c) == 1]
		while len(unit_clauses) > 0:
			unit = unit_clauses[0]
			preposition = self.reduce_preposition(preposition, unit[0])
			assignment += [unit[0]]
			if preposition == -1:
				return -1, []
			if not preposition:
				return preposition, assignment
			unit_clauses = [c for c in preposition if len(c) == 1]
		return preposition, assignment

	# Método que selecciona de forma aleatoria un literal presente en la preposición.
	
	def random_variable_selection(self, preposition):
		counter = self.literal_counter(preposition)
		return random.choice(list(counter.keys()))
	
	def solve(self, preposition, assignment):

		# Filtramos la preposición, para eliminar cláusulas o literales que no nos aporten información.
		# A su vez almacenamos los literales

		preposition, pure_assignment = self.pure_literal(preposition)
		preposition, unit_assignment = self.unit_propagation(preposition)
		assignment = assignment + pure_assignment + unit_assignment

		exec_time = (time.time() - self.start_time)

		# Revisamos si la búsqueda por la solución ha durado más de 300 segundos
		if (exec_time > 300):
			solution = ['time out']
			self.solution = solution
			return solution

		# Si el valor de preposition es "-1" se tiene que se encontró algún problema y el problema es insatisfacible.
		if preposition == - 1:
			return []
		if not preposition:
			self.solution = assignment
			return assignment
		
		variable = self.random_variable_selection(preposition)
		solution = self.solve(self.reduce_preposition(preposition, variable), assignment + [variable])
		if not solution:
			solution = self.solve(self.reduce_preposition(preposition, -variable), assignment + [-variable])
		return solution
	
	def write_solution(self):

		output_file_name = self.file_name.split('/')[-1]
		fd = open('sol_sat_' + str(self.counter) + '_' + output_file_name, 'a')
		self.start_time = time.time()
		self.solve(self.clauses, [])

		if len(self.solution) != 0 :
			if self.solution[0] == 'time out': 
				fd.write('s cnf -1 {:d}'.format(self.number_vars) + '\n')
			else:
				self.solution += [x for x in range(1, self.number_vars + 1) if x not in self.solution and -x not in self.solution]
				self.solution.sort(key=lambda x: abs(x))
				fd.write('s cnf 1 {:d} \n'.format(self.number_vars))
				[fd.write('v ' + str(x) + '\n') for x in self.solution]
		else:
			fd.write('s cnf 0 {:d}'.format(self.number_vars) + '\n')
		fd.close()
