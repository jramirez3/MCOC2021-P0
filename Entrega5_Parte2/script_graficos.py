import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


#SOLVE

#Matriz Llena
	  	 
NCorrida = 1

min_tde = 0.001
min_tds = 0.001
max_tde = [0, 0]
max_tds = [0, 0]

fig = plt.figure("Solve Matriz Llena")
spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
f_ax1 = fig.add_subplot(spec2[0, 0])
f_ax2 = fig.add_subplot(spec2[1, 0])

f_ax1.set_xlabel("Tamaño matriz N")
f_ax1.set_ylabel("Tiempo de ensamblado (s)")
f_ax2.set_xlabel("Tamaño matriz N")
f_ax2.set_ylabel("Tiempo de solucion (s)")
f_ax1.set_ylim([10**-6, 10])
f_ax2.set_ylim([10**-6, 100])
fig.suptitle("Solve Matriz Llena")


while NCorrida <= 10:

	file = open("SOLVE corrida N°{:0>2d} matriz llena.txt".format(NCorrida))
	Ns = []
	Tdes = []
	Tdss = []
	
	for linea in file:

		Ni = linea.strip().split(";")
		Ns.append(int(Ni[0]))
		Tdes.append(float(Ni[1]))
		Tdss.append(float(Ni[2]))


		if max_tde[0] < int(Ni[0]):
			max_tde[0] = int(Ni[0])

		if max_tds[0] < int(Ni[0]):
			max_tds[0] = int(Ni[0])

		if max_tde[1] < float(Ni[1]):
			max_tde[1] = float(Ni[1])

		if max_tds[1] < float(Ni[2]):
			max_tds[1] = float(Ni[2])


	f_ax1.loglog(Ns, Tdes, 'o-', color="grey")
	f_ax2.loglog(Ns, Tdss, 'o-', color="grey")
	file.close()
	NCorrida += 1


tde = max_tde[1] / min_tde
tds = max_tds[1] / min_tds

#O(1)

f_ax1.loglog([2, max_tde[0]], [max_tde[1], max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1], max_tds[1]], '--', label="O(1)")

#O(N)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds, max_tds[1]], '--', label="O(N)")

#O(N²)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**2, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**2, max_tds[1]], '--', label="O(N²)")

#O(N³)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**3, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**3, max_tds[1]], '--', label="O(N³)")

#O(N⁴)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**4, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**4, max_tds[1]], '--', label="O(N⁴)")

f_ax2.legend(loc="best")
plt.show()



#Matriz dispersa
	  	 
NCorrida = 1

min_tde = 0.01
min_tds = 0.001
max_tde = [0, 0]
max_tds = [0, 0]

fig = plt.figure("Solve Matriz dispersa")
spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
f_ax1 = fig.add_subplot(spec2[0, 0])
f_ax2 = fig.add_subplot(spec2[1, 0])

f_ax1.set_xlabel("Tamaño matriz N")
f_ax1.set_ylabel("Tiempo de ensamblado (s)")
f_ax2.set_xlabel("Tamaño matriz N")
f_ax2.set_ylabel("Tiempo de solucion (s)")
f_ax1.set_ylim([10**-4, 100])
f_ax2.set_ylim([10**-6, 100])
fig.suptitle("Solve Matriz dispersa")


while NCorrida <= 10:

	file = open("SOLVE corrida N°{:0>2d} matriz dispersa.txt".format(NCorrida))
	Ns = []
	Tdes = []
	Tdss = []
	
	for linea in file:

		Ni = linea.strip().split(";")
		Ns.append(int(Ni[0]))
		Tdes.append(float(Ni[1]))
		Tdss.append(float(Ni[2]))


		if max_tde[0] < int(Ni[0]):
			max_tde[0] = int(Ni[0])

		if max_tds[0] < int(Ni[0]):
			max_tds[0] = int(Ni[0])

		if max_tde[1] < float(Ni[1]):
			max_tde[1] = float(Ni[1])

		if max_tds[1] < float(Ni[2]):
			max_tds[1] = float(Ni[2])


	f_ax1.loglog(Ns, Tdes, 'o-', color="grey")
	f_ax2.loglog(Ns, Tdss, 'o-', color="grey")
	file.close()
	NCorrida += 1


tde = max_tde[1] / min_tde
tds = max_tds[1] / min_tds

#O(1)

f_ax1.loglog([2, max_tde[0]], [max_tde[1], max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1], max_tds[1]], '--', label="O(1)")

#O(N)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds, max_tds[1]], '--', label="O(N)")

#O(N²)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**2, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**2, max_tds[1]], '--', label="O(N²)")

#O(N³)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**3, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**3, max_tds[1]], '--', label="O(N³)")

#O(N⁴)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**4, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**4, max_tds[1]], '--', label="O(N⁴)")

f_ax2.legend(loc="best")
plt.show()






#INV

#Matriz Llena
	  	 
NCorrida = 1

min_tde = 0.0005
min_tds = 0.0005
max_tde = [0, 0]
max_tds = [0, 0]

fig = plt.figure("Inv Matriz Llena")
spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
f_ax1 = fig.add_subplot(spec2[0, 0])
f_ax2 = fig.add_subplot(spec2[1, 0])

f_ax1.set_xlabel("Tamaño matriz N")
f_ax1.set_ylabel("Tiempo de ensamblado (s)")
f_ax2.set_xlabel("Tamaño matriz N")
f_ax2.set_ylabel("Tiempo de solucion (s)")
f_ax1.set_ylim([10**-6, 10])
f_ax2.set_ylim([10**-6, 100])
fig.suptitle("Inv Matriz Llena")


while NCorrida <= 10:

	file = open("INV corrida N°{:0>2d} matriz llena.txt".format(NCorrida))
	Ns = []
	Tdes = []
	Tdss = []
	
	for linea in file:

		Ni = linea.strip().split(";")
		Ns.append(int(Ni[0]))
		Tdes.append(float(Ni[1]))
		Tdss.append(float(Ni[2]))


		if max_tde[0] < int(Ni[0]):
			max_tde[0] = int(Ni[0])

		if max_tds[0] < int(Ni[0]):
			max_tds[0] = int(Ni[0])

		if max_tde[1] < float(Ni[1]):
			max_tde[1] = float(Ni[1])

		if max_tds[1] < float(Ni[2]):
			max_tds[1] = float(Ni[2])


	f_ax1.loglog(Ns, Tdes, 'o-', color="grey")
	f_ax2.loglog(Ns, Tdss, 'o-', color="grey")
	file.close()
	NCorrida += 1


tde = max_tde[1] / min_tde
tds = max_tds[1] / min_tds

#O(1)

f_ax1.loglog([2, max_tde[0]], [max_tde[1], max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1], max_tds[1]], '--', label="O(1)")

#O(N)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds, max_tds[1]], '--', label="O(N)")

#O(N²)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**2, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**2, max_tds[1]], '--', label="O(N²)")

#O(N³)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**3, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**3, max_tds[1]], '--', label="O(N³)")

#O(N⁴)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**4, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**4, max_tds[1]], '--', label="O(N⁴)")

f_ax2.legend(loc="best")
plt.show()


#Matriz dispersa
	  	 
NCorrida = 1

min_tde = 0.01
min_tds = 0.001
max_tde = [0, 0]
max_tds = [0, 0]

fig = plt.figure("Inv Matriz dispersa")
spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
f_ax1 = fig.add_subplot(spec2[0, 0])
f_ax2 = fig.add_subplot(spec2[1, 0])

f_ax1.set_xlabel("Tamaño matriz N")
f_ax1.set_ylabel("Tiempo de ensamblado (s)")
f_ax2.set_xlabel("Tamaño matriz N")
f_ax2.set_ylabel("Tiempo de solucion (s)")
f_ax1.set_ylim([10**-4, 10])
f_ax2.set_ylim([10**-4, 100])
fig.suptitle("Inv Matriz dispersa")


while NCorrida <= 10:

	file = open("INV corrida N°{:0>2d} matriz dispersa.txt".format(NCorrida))
	Ns = []
	Tdes = []
	Tdss = []
	
	for linea in file:

		Ni = linea.strip().split(";")
		Ns.append(int(Ni[0]))
		Tdes.append(float(Ni[1]))
		Tdss.append(float(Ni[2]))

		if max_tde[0] < int(Ni[0]):
			max_tde[0] = int(Ni[0])

		if max_tds[0] < int(Ni[0]):
			max_tds[0] = int(Ni[0])

		if max_tde[1] < float(Ni[1]):
			max_tde[1] = float(Ni[1])

		if max_tds[1] < float(Ni[2]):
			max_tds[1] = float(Ni[2])

	f_ax1.loglog(Ns, Tdes, 'o-', color="grey")
	f_ax2.loglog(Ns, Tdss, 'o-', color="grey")
	file.close()
	NCorrida += 1


tde = max_tde[1] / min_tde
tds = max_tds[1] / min_tds

#O(1)

f_ax1.loglog([2, max_tde[0]], [max_tde[1], max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1], max_tds[1]], '--', label="O(1)")

#O(N)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds, max_tds[1]], '--', label="O(N)")

#O(N²)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**2, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**2, max_tds[1]], '--', label="O(N²)")

#O(N³)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**3, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**3, max_tds[1]], '--', label="O(N³)")

#O(N⁴)

f_ax1.loglog([2, max_tde[0]], [max_tde[1] / tde**4, max_tde[1]], '--')
f_ax2.loglog([2, max_tds[0]], [max_tds[1] / tds**4, max_tds[1]], '--', label="O(N⁴)")

f_ax2.legend(loc="best")
plt.show()


