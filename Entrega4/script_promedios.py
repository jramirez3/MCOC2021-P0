from numpy import average
from collections import defaultdict


romanos = ["I", "II", "III", "IV", "V", "VI", "VII"]
tipos = ["FLOAT", "DOUBLE"]

#Caso A

for romano in romanos:
	for tipo in tipos:

		Tts = defaultdict(list)

		for i in range(1, 11):
			print("abriendo ", f"{tipo}_Caso_A_{romano}" + "_corrida_N°{:0>2d}.txt".format(i))
			file = open(f"{tipo}_Caso_A_{romano}" + "_corrida_N°{:0>2d}.txt".format(i))

			for linea in file:
				linea2 = linea.strip().split(";")
				linea2[0] = int(linea2[0])
				linea2[1] = float(linea2[1])

				Tts[linea2[0]].append(linea2[1])

			file.close()

		file = open(f"{tipo}_Caso_A_{romano}_PROMEDIOS.txt", 'w')

		for N in Tts:
			file.write(f"{N};{average(Tts[N])}\n")

		file.close()

#Caso B I

Tts = defaultdict(list)

for tipo in tipos:
	for i in range(1, 11):
		print("abriendo ", f"{tipo}_Caso_B_I" + "_corrida_N°{:0>2d}.txt".format(i))
		file = open(f"{tipo}_Caso_B_I" + "_corrida_N°{:0>2d}.txt".format(i))

		for linea in file:
			linea2 = linea.strip().split(";")
			linea2[0] = int(linea2[0])
			linea2[1] = float(linea2[1])

			Tts[linea2[0]].append(linea2[1])

		file.close()

	file = open(f"{tipo}_Caso_B_I_PROMEDIOS.txt", 'w')

	for N in Tts:
		file.write(f"{N};{average(Tts[N])}\n")

	file.close()


#Caso B II - V

booleanos = ["True", "False"]

for romano in romanos[1:5]:
	for tipo in tipos:
		for booleano in booleanos:

			Tts = defaultdict(list)

			for i in range(1, 11):
				print("abriendo ", f"{tipo}_Caso_B_{romano}_overwrite_a_{booleano}" + "_corrida_N°{:0>2d}.txt".format(i))
				file = open(f"{tipo}_Caso_B_{romano}_overwrite_a_{booleano}" + "_corrida_N°{:0>2d}.txt".format(i))

				for linea in file:
					linea2 = linea.strip().split(";")
					linea2[0] = int(linea2[0])
					linea2[1] = float(linea2[1])

					Tts[linea2[0]].append(linea2[1])

				file.close()

			file = open(f"{tipo}_Caso_B_{romano}_overwrite_a_{booleano}_PROMEDIOS.txt", 'w')

			for N in Tts:
				file.write(f"{N};{average(Tts[N])}\n")

			file.close()