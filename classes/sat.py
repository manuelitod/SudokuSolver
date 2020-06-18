# Clase SAT

class Sat:
	def __init__(self, number_vars, number_clauses):
		self.number_vars = number_vars
		self.number_clauses = number_clauses
		self.clauses = []

	def set_clauses(self, clauses):
		self.clauses = clauses.copy()
