from time import perf_counter
from scipy.linalg import inv, solve, eigh
from laplaciana import laplaciana
from numpy import single, double, ones


Ns = [2, 3, 4, 5, 10, 15, 20, 30, 40, 50, 80, 90, 100, 110, 120, 150, 170, 200, 250, 300, 400, 500, 1000, 2500]





#problema A : solve

##caso I: 

print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_A_I_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=single)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		x = inv(A)@b
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_A_I_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=double)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		x = inv(A)@b
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

	

##caso II: 

print("*** CASO 2 ***")
print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_A_II_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=single)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		x = solve(A, b)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_A_II_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=double)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		x = solve(A, b)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()


##Caso III

print("*** CASO 3 ***")
print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_A_III_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=single)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		x = solve(A, b, assume_a='pos')
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_A_III_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=double)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		x = solve(A, b, assume_a='pos')
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()


##Caso IV

print("*** CASO 4 ***")
print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_A_IV_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=single)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		x = solve(A, b, assume_a='sym')
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_A_IV_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=double)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		x = solve(A, b, assume_a='sym')
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()


##Caso V

print("*** CASO 5 ***")
print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_A_V_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=single)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		x = solve(A, b, overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_A_V_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=double)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		x = solve(A, b, overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()


##Caso VI

print("*** CASO 6 ***")
print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_A_VI_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=single)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		x = solve(A, b, overwrite_b=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_A_VI_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=double)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		x = solve(A, b, overwrite_b=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()


##Caso VII

print("*** CASO 7 ***")
print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_A_VII_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=single)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		x = solve(A, b, overwrite_a=True, overwrite_b=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_A_VII_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		b = ones(N, dtype=double)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		x = solve(A, b, overwrite_a=True, overwrite_b=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = b.nbytes + A.nbytes + x.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()


#Problema B : eigh

##caso I: 

print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_B_I_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		w, v = eigh(A)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_B_I_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		w, v = eigh(A)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()



##caso II: 

print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_B_II_overwrite_a_False_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		w, v = eigh(A, driver="ev", overwrite_a=False)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

	file = open("FLOAT_Caso_B_II_overwrite_a_True_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		w, v = eigh(A, driver="ev", overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_B_II_overwrite_a_False_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		w, v = eigh(A, driver="ev", overwrite_a=False)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

	file = open("DOUBLE_Caso_B_II_overwrite_a_True_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		w, v = eigh(A, driver="ev", overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()


##caso III: 

print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_B_III_overwrite_a_False_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		w, v = eigh(A, driver="evd", overwrite_a=False)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

	file = open("FLOAT_Caso_B_III_overwrite_a_True_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		w, v = eigh(A, driver="evd", overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_B_III_overwrite_a_False_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		w, v = eigh(A, driver="evd", overwrite_a=False)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

	file = open("DOUBLE_Caso_B_III_overwrite_a_True_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		w, v = eigh(A, driver="evd", overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()


##caso IV: 

print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_B_IV_overwrite_a_False_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		w, v = eigh(A, driver="evr", overwrite_a=False)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

	file = open("FLOAT_Caso_B_IV_overwrite_a_True_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		w, v = eigh(A, driver="evr", overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_B_IV_overwrite_a_False_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		w, v = eigh(A, driver="evr", overwrite_a=False)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

	file = open("DOUBLE_Caso_B_IV_overwrite_a_True_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		w, v = eigh(A, driver="evr", overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()


##caso V: 

print("\nFLOAT\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("FLOAT_Caso_B_V_overwrite_a_False_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		w, v = eigh(A, driver="evx", overwrite_a=False)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

	file = open("FLOAT_Caso_B_V_overwrite_a_True_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=single)
		t1 = perf_counter()
		w, v = eigh(A, driver="evx", overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

print("\nDOUBLE\n")

for corrida in range(1, 11):
	print(f"corrida {corrida}...")
	file = open("DOUBLE_Caso_B_V_overwrite_a_False_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		w, v = eigh(A, driver="evx", overwrite_a=False)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()

	file = open("DOUBLE_Caso_B_V_overwrite_a_True_corrida_N°{:0>2d}.txt".format(corrida), 'w')

	for N in Ns:
		print("N = ", N)
		A = laplaciana(N, dtype=double)
		t1 = perf_counter()
		w, v = eigh(A, driver="evx", overwrite_a=True)
		t2 = perf_counter()
		Tt = t2 - t1
		memoria = A.nbytes + v.nbytes + w.nbytes
		file.write(f"{N};{Tt};{memoria}\n")
	file.close()