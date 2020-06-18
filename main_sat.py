from helpers.sat import create_sat_instances
import sys

if __name__ == '__main__':
	sat_instances = create_sat_instances(sys.argv[1])
	for sat_instance in sat_instances:
		sat_instance.write_solution()
