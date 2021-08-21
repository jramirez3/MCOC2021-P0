import matplotlib.pyplot as plt

romanos = ["I", "II", "III", "IV", "V", "VI", "VII"]
tipos = ["FLOAT", "DOUBLE"]


#Solver
fig = plt.figure("Solver")
ax = fig.add_subplot()
ax.set_ylabel("tiempo transcurrido (s)")
ax.set_xlabel("tamaño matriz (N)")
fig.suptitle("Solver")



for romano in romanos:
	for tipo in tipos:
		file = open(f"{tipo}_Caso_A_{romano}_PROMEDIOS.txt")

		Ns = []
		Tts = []

		for linea in file:
			linea2 = linea.strip().split(";")
			Ns.append(int(linea2[0]))
			Tts.append(float(linea2[1]))

		file.close()
		ax.loglog(Ns, Tts, 'o-', label=f"Caso {romano}, {tipo}")

ax.legend(loc="upper left")
plt.show()


#Eigh
fig = plt.figure("Eigh")
ax = fig.add_subplot()
ax.set_ylabel("tiempo transcurrido (s)")
ax.set_xlabel("tamaño matriz (N)")
fig.suptitle("Eigh")

for tipo in tipos:
		file = open(f"{tipo}_Caso_B_I_PROMEDIOS.txt")

		Ns = []
		Tts = []

		for linea in file:
			linea2 = linea.strip().split(";")
			Ns.append(int(linea2[0]))
			Tts.append(float(linea2[1]))

		file.close()
		ax.loglog(Ns, Tts, 'o-', label=f"Caso I, {tipo}")


booleanos = ["True", "False"]

for romano in romanos[1:5]:
	for tipo in tipos:
		for booleano in booleanos:
			file = open(f"{tipo}_Caso_B_{romano}_overwrite_a_{booleano}_PROMEDIOS.txt")

			Ns = []
			Tts = []

			for linea in file:
				linea2 = linea.strip().split(";")
				Ns.append(int(linea2[0]))
				Tts.append(float(linea2[1]))

			file.close()
			ax.loglog(Ns, Tts, 'o-', label=f"Caso {romano} overwrite_a {booleano}, {tipo}")

ax.legend(loc="upper left")
plt.show()

