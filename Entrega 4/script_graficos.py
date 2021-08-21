import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


romanos = ["I", "II", "III", "IV", "V", "VI", "VII"]

#Caso A

for romano in romanos:
	  	 
	NCorrida = 1

	fig = plt.figure()
	spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
	f_ax1 = fig.add_subplot(spec2[0, 0])
	f_ax2 = fig.add_subplot(spec2[1, 0])

	f_ax1.set_xlabel("Tamaño matriz N")
	f_ax1.set_ylabel("Tiempo transcurrido (s)")
	f_ax2.set_xlabel("Tamaño matriz N")
	f_ax2.set_ylabel("Uso memoria (byte)")
	fig.suptitle(f"FLOAT Caso A {romano}")


	while NCorrida <= 10:

		nombre = "FLOAT_Caso_A_" + romano + "_corrida_N°{:0>2d}.txt".format(NCorrida)
		file = open(nombre)
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

	fig = plt.figure()
	spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
	f_ax1 = fig.add_subplot(spec2[0, 0])
	f_ax2 = fig.add_subplot(spec2[1, 0])

	f_ax1.set_xlabel("Tamaño matriz N")
	f_ax1.set_ylabel("Tiempo transcurrido (s)")
	f_ax2.set_xlabel("Tamaño matriz N")
	f_ax2.set_ylabel("Uso memoria (byte)")
	fig.suptitle(f"DOUBLE Caso A {romano}")

	NCorrida = 1


	while NCorrida <= 10:

		nombre = "DOUBLE_Caso_A_" + romano + "_corrida_N°{:0>2d}.txt".format(NCorrida)
		file = open(nombre)
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



#Caso B I

NCorrida = 1

fig = plt.figure()
spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
f_ax1 = fig.add_subplot(spec2[0, 0])
f_ax2 = fig.add_subplot(spec2[1, 0])

f_ax1.set_xlabel("Tamaño matriz N")
f_ax1.set_ylabel("Tiempo transcurrido (s)")
f_ax2.set_xlabel("Tamaño matriz N")
f_ax2.set_ylabel("Uso memoria (byte)")
fig.suptitle(f"FLOAT Caso B I")


while NCorrida <= 10:

	nombre = "FLOAT_Caso_B_I_corrida_N°{:0>2d}.txt".format(NCorrida)
	file = open(nombre)
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

fig = plt.figure()
spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
f_ax1 = fig.add_subplot(spec2[0, 0])
f_ax2 = fig.add_subplot(spec2[1, 0])

f_ax1.set_xlabel("Tamaño matriz N")
f_ax1.set_ylabel("Tiempo transcurrido (s)")
f_ax2.set_xlabel("Tamaño matriz N")
f_ax2.set_ylabel("Uso memoria (byte)")
fig.suptitle(f"DOUBLE Caso B I")

NCorrida = 1


while NCorrida <= 10:

	nombre = "DOUBLE_Caso_B_I_corrida_N°{:0>2d}.txt".format(NCorrida)
	file = open(nombre)
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
#Caso B II - V

overwrite_as = ["True", "False"]

for romano in romanos[1:5]:
	for overwrite_a in overwrite_as:  	 
		
		NCorrida = 1

		fig = plt.figure()
		spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
		f_ax1 = fig.add_subplot(spec2[0, 0])
		f_ax2 = fig.add_subplot(spec2[1, 0])

		f_ax1.set_xlabel("Tamaño matriz N")
		f_ax1.set_ylabel("Tiempo transcurrido (s)")
		f_ax2.set_xlabel("Tamaño matriz N")
		f_ax2.set_ylabel("Uso memoria (byte)")
		fig.suptitle(f"FLOAT Caso B {romano} overwrite_a={overwrite_a}")


		while NCorrida <= 10:

			nombre = "FLOAT_Caso_B_" + romano + f"_overwrite_a_{overwrite_a}" + "_corrida_N°{:0>2d}.txt".format(NCorrida)
			file = open(nombre)
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

		fig = plt.figure()
		spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
		f_ax1 = fig.add_subplot(spec2[0, 0])
		f_ax2 = fig.add_subplot(spec2[1, 0])

		f_ax1.set_xlabel("Tamaño matriz N")
		f_ax1.set_ylabel("Tiempo transcurrido (s)")
		f_ax2.set_xlabel("Tamaño matriz N")
		f_ax2.set_ylabel("Uso memoria (byte)")
		fig.suptitle(f"DOUBLE Caso B {romano} overwrite_a={overwrite_a}")

		NCorrida = 1


		while NCorrida <= 10:

			nombre = "DOUBLE_Caso_B_" + romano + f"_overwrite_a_{overwrite_a}" + "_corrida_N°{:0>2d}.txt".format(NCorrida)
			file = open(nombre)
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
