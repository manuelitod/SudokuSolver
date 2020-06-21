import matplotlib.pyplot as plt
import sys

def compare_sat_solvers():
	fd_sat = open('./SatOutputTimes/' + sys.argv[2], 'r')
	fd_zchaff = open('./SatOutputTimes/' + sys.argv[3], 'r')
	sat_times = []
	zchaff_times = []
	x = []

	for line in fd_sat:
		sat_times.append(float(line.split('\n')[0]))

	for line in fd_zchaff:
		zchaff_times.append(float(line.split('\n')[0]))

	for num in range(1, (len(sat_times) + 1)):
		x.append(num)

	plt.plot(x, sat_times, 'o', color='green', label='Sat propio')
	plt.plot(x, zchaff_times, 'o', color='blue', label='Zchaff')
	plt.legend()
	plt.xlabel('Instancias de sudoku')
	plt.ylabel('Tiempos (ms)')
	plt.title("Análisis de tiempos de resolución")
	plt.show()

	fd_sat.close()
	fd_zchaff.close()

if __name__ == '__main__':
	compare_sat_solvers()