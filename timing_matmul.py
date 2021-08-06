from numpy import zeros
from time import perf_counter




Ns = [2, 3, 4, 5, 10, 15, 20, 30, 40, 50, 80, 90, 100, 110, 120, 150, 170, 200, 250, 300, 400, 500, 1000,1500, 2000, 5000, 10000]
NCorrida = 1

while NCorrida <= 10:

	nombre = "Corrida N°" + str(NCorrida)
	file = open(nombre + ".txt", 'w')

	for N in Ns:

		A = zeros((N, N))+1
		B = zeros((N, N))+2

		t1 = perf_counter()
		C = A@B
		t2 = perf_counter()

		dt = t2 - t1
		memoria = A.nbytes + B.nbytes + C.nbytes

		#(Tamaño de matriz N);(Tiempo transcurrido);(uso de memoria)
		
		file.write(f"{N};{dt};{memoria}\n")

	file.close
	NCorrida += 1
