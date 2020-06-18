# Funciones de ayuda para la implementacion del SAT
from classes.sat import Sat

# Create sat instances
def create_sat_instances(file_name):

	sat_array_instances = []
	clauses = []
	actual_clause = []
	counter = 0
	fd = open(file_name, 'r')

	for line in fd:

		if line.startswith('c'): continue
		if line.startswith('p'):

			metadata = line.split(' ')
			if metadata[1] != 'cnf': raise Exception("La formula debe ser cnf")
			try:
				# Se creo una instancia de SAT, se debe actualizar
				if counter != 0: # Si el contador es cero se hace referencia al primer prólogo
					
					clauses.append(actual_clause.copy())
					sat_instance.set_clauses(clauses)
					sat_array_instances.append(sat_instance)
					actual_clause = []
					clauses = []

				sat_instance = Sat(metadata[2],metadata[3])
				counter += 1
			except:
				print('Numero de variables y clausulas no definidas')

		else:
			# Registro de clausulas
			# Si se encuentra un 0 tenemos una clausula completa
			# Si no seguimos construyendo la misma
			for var in line.split(' '):
				var = var.split('\n')[0]
				if var == '0':
					clauses.append(actual_clause.copy())
					actual_clause = []
				else:
					actual_clause.append(int(var))

	clauses.append(actual_clause.copy())
	sat_instance.set_clauses(clauses)
	sat_array_instances.append(sat_instance)
	fd.close()

	return sat_array_instances
