from helpers.sat import create_sat_instances
import sys

if __name__ == '__main__':
	sat_array_instances = create_sat_instances(sys.argv[1])
	for sat in sat_array_instances:
		print(sat.clauses)
