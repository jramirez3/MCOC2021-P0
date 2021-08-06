import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


	  	 
NCorrida = 1

fig = plt.figure()
spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
f_ax1 = fig.add_subplot(spec2[0, 0])
f_ax2 = fig.add_subplot(spec2[1, 0])

f_ax1.set_xlabel("Tamaño matriz N")
f_ax1.set_ylabel("Tiempo transcurrido (s)")
f_ax2.set_xlabel("Tamaño matriz N")
f_ax2.set_ylabel("Uso memoria (byte)")


while NCorrida <= 10:

	nombre = "Corrida N°" + str(NCorrida)
	file = open(nombre + ".txt")
	Ns = []
	dts = []
	mems = []
	
	for linea in file:

		Ni = linea.strip().split(";")
		Ns.append(int(Ni[0]))
		dts.append(float(Ni[1]))
		if NCorrida == 1:
			mems.append(int(Ni[2]))

	f_ax1.loglog(Ns, dts, 'o-')
	if NCorrida == 1:
		f_ax2.loglog(Ns, mems, 'o-')
	file.close()
	NCorrida += 1
plt.show()