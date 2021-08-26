from numpy import eye, double
from time import perf_counter
import scipy.sparse as sparse

def matriz_laplaciana(N, t=double):
	e =  eye(N, dtype=t)-eye(N,N,1, dtype=t)
	return e+e.T

def matriz_laplaciana_sparse(N, t=double):
	return sparse.eye(N, format="csr", dtype=t)*2 - sparse.eye(N, k=1, format="csr", dtype=t) - sparse.eye(N, k=-1, format="csr", dtype=t)


Ns = [2, 3, 4, 5, 10, 15, 20, 30, 40, 50, 80, 90, 100, 110, 120, 150, 170, 200, 250, 300, 400, 500, 1000,1500, 2000, 2500, 3000, 5000, 8000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 50000, 100000, 500000, 1000000, 1500000, 2000000, 5000000, 10000000, 50000000]
#Ns = [2, 3, 4, 5, 10, 15, 20, 30, 40, 50, 80, 90, 100, 110, 120, 150, 170, 200, 250, 300, 400, 500, 1000,1500, 2000, 2500, 3000, 5000, 8000, 9000, 10000, 12000]

corrida = 1


#Matriz llena

while corrida <= 10:

	file = open("corrida N°{:0>2d} matriz llena.txt".format(corrida), "w")
	print(f"\nCORRIDA N°{corrida}\n")
	for N in Ns:
		print(N)
		t1 = perf_counter()
		A = matriz_laplaciana(N)
		B = A
		t2 = perf_counter()
		c = A@B
		t3 = perf_counter()
	
		file.write(f"{N};{t2-t1};{t3-t2}\n")
	file.close()
	corrida += 1

#matriz dispersa

while corrida <= 10:

	file = open("corrida N°{:0>2d} matriz dispersa.txt".format(corrida), "w")
	print(f"\nCORRIDA N°{corrida}\n")
	for N in Ns:
		print(N)
		t1 = perf_counter()
		A = matriz_laplaciana_sparse(N)
		B = A
		t2 = perf_counter()
		c = A@B
		t3 = perf_counter()
	
		file.write(f"{N};{t2-t1};{t3-t2}\n")
	file.close()
	corrida += 1

