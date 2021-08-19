from time import perf_counter
from numpy.linalg import inv
from laplaciana import laplaciana
from numpy import double
Ns = [2, 3, 4, 5, 10, 15, 20, 30, 40, 50, 80, 90, 100, 110, 120, 150, 170, 200, 250, 300, 400, 500, 1000,1500, 2000, 2500]


NCorrida = 1

while NCorrida <= 10:

	nombre = "Corrida N°" + str(NCorrida)
	file = open(nombre + ".txt", 'w')

	for N in Ns:

		t1 = perf_counter()
		A = laplaciana(N, dtype=double)
		t2 = perf_counter()
		Am1 = inv(A)
		t3 = perf_counter()

		dt_inversion = t3 - t2

		bytes_total = A.nbytes + Am1.nbytes

		file.write(f"{N};{dt_inversion};{bytes_total}\n")

	file.close()
	NCorrida += 1